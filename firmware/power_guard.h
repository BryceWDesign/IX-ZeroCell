#ifndef IX_ZEROCELL_POWER_GUARD_H
#define IX_ZEROCELL_POWER_GUARD_H

#include <stdint.h>
#include <math.h>

namespace zerocell {

inline bool finite_value(float value) { return !isnan(value) && !isinf(value); }

struct Limits {
    uint8_t cells = 4;
    float bank_capacitance_lower_f = 1.5f; // ZC-D10: 2.5 F nominal, conservative aging/tolerance allowance
    float minimum_cell_v = 1.0f;
    float restart_cell_v = 2.0f;
    float maximum_cell_v = 2.6f; // software trip, below required >=2.7 V cell rating
    float voltage_error_bound_v = 0.03f; // assumed acquisition bound, must be calibrated
    float maximum_spread_v = 0.15f;
    float maximum_temperature_c = 60.0f;
    float minimum_temperature_c = -20.0f;
    float maximum_output_w = 10.0f;
    float maximum_bank_current_a = 8.0f;
    float bank_resistance_upper_ohm = 0.24f; // declared conservative bound, must be measured
    float output_efficiency_lower = 0.8f;
    float controller_power_upper_w = 0.1f;
    float emergency_reserve_j = 5.0f;
    uint32_t maximum_age_ms = 1500;
};

struct Sample {
    uint32_t timestamp_ms = 0;
    float cell_v[4] = {0, 0, 0, 0};
    uint8_t cells = 4;
    float bank_v = 0;
    float temperature_c = 25;
    bool instrumentation_ok = false;
    bool hardware_permit = false;
};

enum class Reason : uint8_t {
    Ready, EnergyReserve, LowVoltage, OutputLimit, InvalidRequest,
    Configuration, Clock, Telemetry, Stale, Interlock, Temperature,
    Overvoltage, Imbalance, VoltageMismatch, CurrentLimit
};

struct Decision {
    bool enable = false;
    bool tripped = false;
    float available_j = 0;
    Reason reason = Reason::Ready;
};

class PowerGuard {
public:
    explicit PowerGuard(const Limits& limits = Limits()) : limits_(limits) {}

    Decision update(uint32_t now, const Sample& sample, float requested_w,
                    float duration_s, bool emergency = false) {
        Reason fault = check_sample(now, sample);
        const uint32_t elapsed = now - previous_ms_;
        if (have_time_ && (elapsed == 0 || elapsed > 0x7fffffffUL)) fault = Reason::Clock;
        previous_ms_ = now;
        have_time_ = true;
        if (fault != Reason::Ready) trip(fault);
        if (!finite_value(requested_w) || requested_w < 0 || !finite_value(duration_s) || duration_s <= 0)
            trip(Reason::InvalidRequest);
        if (tripped_) return result(false, true, 0, trip_reason_);
        float lowest = sample.cell_v[0];
        for (uint8_t i = 1; i < limits_.cells; ++i)
            if (sample.cell_v[i] < lowest) lowest = sample.cell_v[i];
        lowest -= limits_.voltage_error_bound_v;
        if (lowest < 0) lowest = 0;
        if (lowest <= limits_.minimum_cell_v) awake_ = false;
        if (lowest >= limits_.restart_cell_v) awake_ = true;
        // Using the weakest cell gives a conservative series-bank energy screen.
        const float conservative_v = lowest * limits_.cells;
        const float minimum_v = limits_.minimum_cell_v * limits_.cells;
        float available = 0.5f * limits_.bank_capacitance_lower_f *
            (conservative_v * conservative_v - minimum_v * minimum_v);
        if (available < 0) available = 0;
        if (!awake_) return result(false, false, available, Reason::LowVoltage);
        if (requested_w > limits_.maximum_output_w)
            return result(false, false, available, Reason::OutputLimit);
        const float bus_w = requested_w / limits_.output_efficiency_lower +
                            limits_.controller_power_upper_w;
        // Worst-case current at the cutoff, including declared DC resistance.
        const float r = limits_.bank_resistance_upper_ohm;
        const float discriminant = minimum_v * minimum_v - 4 * r * bus_w;
        if (discriminant <= 0) return result(false, false, available, Reason::CurrentLimit);
        const float current = 2 * bus_w / (minimum_v + sqrtf(discriminant));
        if (current > limits_.maximum_bank_current_a)
            return result(false, false, available, Reason::CurrentLimit);
        const float required = (bus_w + current * current * r) * duration_s +
                               (emergency ? 0 : limits_.emergency_reserve_j);
        if (required > available) return result(false, false, available, Reason::EnergyReserve);
        return result(requested_w > 0, false, available, Reason::Ready);
    }

    bool reset(uint32_t now, const Sample& sample) {
        const uint32_t elapsed = now - previous_ms_;
        if (!tripped_ || check_sample(now, sample) != Reason::Ready ||
            (have_time_ && (elapsed == 0 || elapsed > 0x7fffffffUL))) return false;
        tripped_ = false;
        awake_ = false;
        trip_reason_ = Reason::Ready;
        previous_ms_ = now;
        have_time_ = true;
        return true;
    }

private:
    Limits limits_;
    bool tripped_ = false, awake_ = false, have_time_ = false;
    uint32_t previous_ms_ = 0;
    Reason trip_reason_ = Reason::Ready;

    static Decision result(bool enabled, bool tripped, float energy, Reason reason) {
        Decision d; d.enable = enabled; d.tripped = tripped;
        d.available_j = energy; d.reason = reason; return d;
    }

    void trip(Reason reason) { tripped_ = true; awake_ = false; trip_reason_ = reason; }

    bool valid_limits() const {
        const float values[] = {limits_.bank_capacitance_lower_f, limits_.minimum_cell_v,
            limits_.restart_cell_v, limits_.maximum_cell_v, limits_.voltage_error_bound_v,
            limits_.maximum_spread_v,
            limits_.maximum_temperature_c, limits_.minimum_temperature_c,
            limits_.maximum_output_w, limits_.maximum_bank_current_a,
            limits_.bank_resistance_upper_ohm, limits_.output_efficiency_lower,
            limits_.controller_power_upper_w, limits_.emergency_reserve_j};
        for (unsigned i = 0; i < sizeof(values) / sizeof(values[0]); ++i)
            if (!finite_value(values[i])) return false;
        return limits_.cells > 0 && limits_.cells <= 4 &&
            limits_.bank_capacitance_lower_f > 0 && limits_.minimum_cell_v > 0 &&
            limits_.minimum_cell_v < limits_.restart_cell_v &&
            limits_.restart_cell_v <= limits_.maximum_cell_v &&
            limits_.voltage_error_bound_v >= 0 && limits_.maximum_spread_v >= 0 &&
            limits_.minimum_temperature_c < limits_.maximum_temperature_c &&
            limits_.maximum_output_w > 0 && limits_.maximum_bank_current_a > 0 &&
            limits_.bank_resistance_upper_ohm >= 0 && limits_.output_efficiency_lower > 0 &&
            limits_.output_efficiency_lower <= 1 && limits_.controller_power_upper_w >= 0 &&
            limits_.emergency_reserve_j >= 0 && limits_.maximum_age_ms > 0 &&
            limits_.maximum_age_ms < 0x80000000UL;
    }

    Reason check_sample(uint32_t now, const Sample& sample) const {
        if (!valid_limits()) return Reason::Configuration;
        if (sample.cells != limits_.cells || !sample.instrumentation_ok ||
            !finite_value(sample.temperature_c) || !finite_value(sample.bank_v) || sample.bank_v < 0)
            return Reason::Telemetry;
        if (now - sample.timestamp_ms > limits_.maximum_age_ms) return Reason::Stale;
        if (!sample.hardware_permit) return Reason::Interlock;
        if (sample.temperature_c < limits_.minimum_temperature_c ||
            sample.temperature_c >= limits_.maximum_temperature_c) return Reason::Temperature;
        float sum = 0, lowest = sample.cell_v[0], highest = lowest;
        for (uint8_t i = 0; i < limits_.cells; ++i) {
            const float value = sample.cell_v[i];
            if (!finite_value(value) || value < 0) return Reason::Telemetry;
            if (value + limits_.voltage_error_bound_v >= limits_.maximum_cell_v) return Reason::Overvoltage;
            if (value < lowest) lowest = value;
            if (value > highest) highest = value;
            sum += value;
        }
        if (highest - lowest > limits_.maximum_spread_v) return Reason::Imbalance;
        if (fabsf(sum - sample.bank_v) > 0.1f) return Reason::VoltageMismatch;
        return Reason::Ready;
    }
};
}
#endif

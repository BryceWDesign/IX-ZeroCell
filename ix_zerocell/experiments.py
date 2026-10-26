"""Reproducible assumption-based emergency-power scenarios and counterexamples."""

from dataclasses import asdict
import math
from .power import Bank, Bus, Source
from .sources import pv_power, kinetic_power, rf_power, recirculating_net_power
from .validation import number, positive


def run_scenario(name, bank, source_function, requested_w, duration_s,
                 initial_v=0, start_v=8, step_s=1, controller_active_w=.01,
                 controller_sleep_w=.00001, direct_source_allowed=False,
                 direct_startup_s=5, output_limit_w=10):
    positive(duration_s, "duration_s")
    positive(step_s, "step_s")
    number(requested_w, "requested_w")
    number(start_v, "start_v")
    number(direct_startup_s, "direct_startup_s")
    if type(direct_source_allowed) is not bool:
        raise ValueError("direct_source_allowed must be boolean")
    if duration_s / step_s > 1_000_000:
        raise ValueError("scenario exceeds one million integration steps")
    if not bank.cutoff_v < start_v <= bank.max_v:
        raise ValueError("invalid scenario timing/thresholds")
    bus = Bus(bank, initial_v, output_limit_w=output_limit_w)
    enabled = False
    total = {"input_j": 0.0, "output_j": 0.0, "unmet_output_j": 0.0,
             "leakage_j": 0.0, "curtailed_j": 0.0}
    max_residual, on_seconds, first_on = 0.0, 0.0, None
    total_requested, t = requested_w * duration_s, 0.0
    samples = []
    while t < duration_s - 1e-9:
        dt = min(step_s, duration_s - t)
        if bus.voltage <= bank.cutoff_v:
            enabled = False
        elif bus.voltage >= start_v:
            enabled = True
        sources = source_function(t)
        direct = (direct_source_allowed and t >= direct_startup_s and
                  sum(s.bus_w for s in sources) >=
                  requested_w / bus.output_efficiency + controller_active_w)
        serving = enabled or direct
        load = requested_w if serving else 0.0
        r = bus.step(sources, load, dt,
                     controller_active_w if serving else controller_sleep_w)
        for key in total:
            total[key] += getattr(r, key)
        max_residual = max(max_residual, abs(r.residual_j))
        if r.output_j >= requested_w * dt * 0.99 and requested_w > 0:
            on_seconds += dt
            if first_on is None:
                first_on = t
        power = round(r.output_j / dt, 6)
        if (not samples or int(t // 600) != int((t - dt) // 600)
                or abs(power - samples[-1]["output_w"]) > .001
                or t + dt >= duration_s - 1e-9):
            samples.append({"time_s": round(t + dt, 3), "bank_v": round(r.end_v, 6),
                            "output_w": round(r.output_j / dt, 6)})
        t += dt
    return {"name": name, "origin": "simulation_assumptions", "battery_count": 0,
            "bank": asdict(bank), "initial_bank_v": initial_v,
            "duration_s": duration_s, "step_s": step_s,
            "controller_active_w": controller_active_w,
            "controller_sleep_w": controller_sleep_w,
            "direct_source_allowed": direct_source_allowed,
            "direct_startup_s_assumption": direct_startup_s,
            "output_limit_w": output_limit_w,
            "requested_load_w": requested_w,
            "first_99_percent_load_s": first_on, "seconds_at_99_percent_load": on_seconds,
            "output_wh": total["output_j"] / 3600,
            "offered_input_wh": total["input_j"] / 3600,
            "requested_but_not_served_wh": max(0, total_requested - total["output_j"]) / 3600,
            "end_bank_v": bus.voltage, "max_step_residual_j": max_residual,
            "hardware_validated": False, "samples": samples}


def campaign(step_s=1):
    field = Bank()
    sentinel = Bank(series=2, cell_f=1, cutoff_v=2.2,
                    cell_dc_resistance_ohm=1, leakage_bank_a=0.000001,
                    max_charge_a=0.02, max_discharge_a=0.02)
    legacy = Bank(series=3, cell_f=1000, cutoff_v=5.5,
                  leakage_bank_a=0.001)
    starter = Bank(series=2, cell_f=100, cutoff_v=2.2,
                   cell_dc_resistance_ohm=.02, leakage_bank_a=.0001,
                   max_charge_a=1, max_discharge_a=1)
    expanded = Bank(max_discharge_a=6)
    scenarios = [
        run_scenario("20W_panel_daylight_1W_light", field,
                     lambda t: [Source("solar", pv_power(20, 800), .90, 20)],
                     1, 7200, start_v=8, step_s=step_s),
        run_scenario("20W_panel_priority_direct_path_1W_light", field,
                     lambda t: [Source("solar", pv_power(20, 800), .90, 20)],
                     1, 7200, start_v=8, step_s=step_s, direct_source_allowed=True),
        run_scenario("50W_panel_priority_direct_path_20W_DC", expanded,
                     lambda t: [Source("solar", pv_power(50,800), .90, 50)],
                     20, 7200, start_v=8, step_s=step_s, direct_source_allowed=True,
                     output_limit_w=20),
        run_scenario("20W_DC_solar_loss_after_one_hour", expanded,
                     lambda t: [Source("solar", pv_power(50,800) if t<3600 else 0,.90,50)],
                     20, 7200, initial_v=10, start_v=8, step_s=step_s,
                     direct_source_allowed=True,output_limit_w=20),
        run_scenario("charged_field_bank_dark_5W_USB", field,
                     lambda t: [], 5, 7200, initial_v=10, start_v=8, step_s=step_s),
        run_scenario("large_bank_5W_generator_10min_cold_start_negative_control", field,
                     lambda t: [Source("human_generator", 5 if t < 600 else 0, .85, 5)],
                     1, 10800, start_v=5.0, step_s=step_s),
        run_scenario("starter_bank_5W_generator_10min_then_1W_light", starter,
                     lambda t: [Source("human_generator", 5 if t < 600 else 0, .85, 5)],
                     1, 3600, start_v=3.5, step_s=step_s),
        run_scenario("RF_only_large_bank_negative_control", field,
                     lambda t: [Source("RF", rf_power(-20, .4), .8, .001)],
                     1, 3600, start_v=8, step_s=step_s),
        run_scenario("no_input_empty_bank_negative_control", field,
                     lambda t: [], 1, 3600, start_v=8, step_s=step_s),
        run_scenario("microharvester_small_bank_sensor", sentinel,
                     lambda t: [Source("PV_micropower_assumed", .003, .7, .003)],
                     .0001, 7200, start_v=3.5, step_s=step_s,
                     controller_active_w=.000005, controller_sleep_w=.000001),
    ]
    return {
        "schema": "1", "hardware_validated": False,
        "authority": "fixed_parameter_sizing_model_not_hardware_or_weather_prediction",
        "legacy_corrections": {
            "three_1000F_series_equivalent_f": legacy.capacitance_f,
            "three_cells_at_2_7V_full_energy_wh": .5 * (1000 / 3) * 8.1 ** 2 / 3600,
            "three_cells_8_1_to_5_5V_ideal_usable_wh": .5 * (1000 / 3) * (8.1 ** 2 - 5.5 ** 2) / 3600,
            "99_times_0_288W_without_gain_w": 99 * .288,
            "series_or_parallel_can_multiply_voltage_and_current_together": False,
        },
        "physical_screens": {
            "moving_0_1kg_at_2m_s_once_per_s_50pct_w": kinetic_power(.1, 2, 1, .5),
            "RF_minus_20dBm_40pct_rectifier_w": rf_power(-20, .4),
            "10W_drive_80pct_recovery_net_w": recirculating_net_power(10, .8),
            "field_bank_10_to_4_5V_ideal_usable_wh": field.usable_wh,
            "field_bank_5W_ideal_runtime_h_at_88pct_no_parasitics": field.usable_wh * .88 / 5,
            "required_capacitance_f_for_1kW_1h_10_to_4_5V_88pct_no_parasitics":
                2 * 1000 * 3600 / (.88 * (10 ** 2 - 4.5 ** 2)),
        },
        "scenarios": scenarios,
    }

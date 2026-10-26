"""First-principles screening ceilings, not promises of available field power."""

import math
from .validation import number, positive


def pv_power(nameplate_w, irradiance_w_m2, derating=0.8):
    """Linear STC screen, capped at nameplate; no weather prediction or MPPT model."""
    number(nameplate_w, "nameplate_w")
    number(irradiance_w_m2, "irradiance_w_m2")
    number(derating, "derating", 0, 1)
    return nameplate_w * min(irradiance_w_m2 / 1000, 1) * derating


def kinetic_power(mass_kg, velocity_m_s, strokes_per_s, efficiency=0.5):
    """Single moving mass fully replenished on every stroke by external work.

    Multiple coils sharing the same moving magnet do not multiply this budget.
    This is a ceiling for the declared work model, not a transducer prediction.
    """
    for name, value in [("mass_kg", mass_kg), ("velocity_m_s", velocity_m_s),
                        ("strokes_per_s", strokes_per_s)]:
        number(value, name)
    number(efficiency, "efficiency", 0, 1)
    return 0.5 * mass_kg * velocity_m_s ** 2 * strokes_per_s * efficiency


def teg_power(open_circuit_v, resistance_ohm, hot_k, cold_k, heat_flow_w):
    """Matched Thevenin load, also bounded by the Carnot heat-flow ceiling.

    hot_k/cold_k refer to module faces under load. A temperature difference
    without heat-flow and thermal-interface data does not establish power.
    """
    number(open_circuit_v, "open_circuit_v")
    positive(resistance_ohm, "resistance_ohm")
    positive(hot_k, "hot_k")
    positive(cold_k, "cold_k")
    number(heat_flow_w, "heat_flow_w")
    if hot_k < cold_k:
        raise ValueError("hot_k must be >= cold_k")
    if hot_k == cold_k and open_circuit_v != 0:
        raise ValueError("nonzero TEG voltage at zero gradient is inconsistent")
    return min(open_circuit_v ** 2 / (4 * resistance_ohm),
               heat_flow_w * (1 - cold_k / hot_k))


def rf_power(received_dbm, efficiency):
    """Power measured at the antenna terminal, NOT guessed from urban location."""
    number(received_dbm, "received_dbm", -300, 60)
    number(efficiency, "efficiency", 0, 1)
    return 1e-3 * 10 ** (received_dbm / 10) * efficiency


def recirculating_net_power(drive_w, recovery_efficiency, auxiliary_w=0):
    number(drive_w, "drive_w")
    number(recovery_efficiency, "recovery_efficiency", 0, 1)
    number(auxiliary_w, "auxiliary_w")
    return drive_w * recovery_efficiency - drive_w - auxiliary_w


def thermal_temperature(initial_c, ambient_c, dissipated_w, resistance_k_w,
                        capacity_j_k, seconds):
    """Exact one-node RC solution with a fixed ambient, not hardware qualification."""
    number(initial_c, "initial_c", -273.15)
    number(ambient_c, "ambient_c", -273.15)
    number(dissipated_w, "dissipated_w")
    positive(resistance_k_w, "resistance_k_w")
    positive(capacity_j_k, "capacity_j_k")
    number(seconds, "seconds")
    equilibrium = ambient_c + dissipated_w * resistance_k_w
    return equilibrium + (initial_c - equilibrium) * math.exp(
        -seconds / (resistance_k_w * capacity_j_k))

"""Battery-free, two-direction capacitor accounting with explicit conversion losses.

Each step assumes constant capacitor current, using the exact capacitor
energy change and I^2 R loss over that step. Sources connect to a common
conditioned bus; charge/discharge converters have declared fixed efficiencies.
The model is a sizing screen, not a switching-circuit or cell-imbalance solver.
"""

from dataclasses import dataclass, asdict
import math
from .validation import integer, number, positive


@dataclass(frozen=True)
class Bank:
    series: int = 4
    parallel: int = 1
    cell_f: float = 3000
    cell_max_v: float = 2.5
    cutoff_v: float = 4.5
    cell_dc_resistance_ohm: float = 0.0003
    leakage_bank_a: float = 0.005
    max_charge_a: float = 2
    max_discharge_a: float = 3

    def __post_init__(self):
        integer(self.series, "series")
        integer(self.parallel, "parallel")
        for key in ("cell_f", "cell_max_v", "max_charge_a", "max_discharge_a"):
            positive(getattr(self, key), key)
        for key in ("cutoff_v", "cell_dc_resistance_ohm", "leakage_bank_a"):
            number(getattr(self, key), key)
        if self.cutoff_v >= self.max_v:
            raise ValueError("cutoff must be below maximum bank voltage")

    @property
    def capacitance_f(self):
        return self.cell_f * self.parallel / self.series

    @property
    def resistance_ohm(self):
        return self.cell_dc_resistance_ohm * self.series / self.parallel

    @property
    def max_v(self):
        return self.cell_max_v * self.series

    def energy_j(self, voltage):
        number(voltage, "voltage", 0, self.max_v)
        return 0.5 * self.capacitance_f * voltage ** 2

    @property
    def usable_wh(self):
        return (self.energy_j(self.max_v) - self.energy_j(self.cutoff_v)) / 3600


@dataclass(frozen=True)
class Source:
    name: str
    input_w: float
    efficiency: float
    max_bus_w: float

    def __post_init__(self):
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("source name required")
        number(self.input_w, "input_w")
        number(self.efficiency, "efficiency", 0, 1)
        number(self.max_bus_w, "max_bus_w")

    @property
    def bus_w(self):
        return min(self.input_w * self.efficiency, self.max_bus_w)


@dataclass(frozen=True)
class Step:
    input_j: float
    source_loss_j: float
    source_rejected_j: float
    output_j: float
    output_loss_j: float
    controller_j: float
    leakage_j: float
    capacitor_resistance_loss_j: float
    charge_conversion_loss_j: float
    curtailed_j: float
    storage_change_j: float
    unmet_output_j: float
    controller_unmet_j: float
    end_v: float

    @property
    def residual_j(self):
        return self.input_j - self.storage_change_j - sum((
            self.source_loss_j, self.source_rejected_j, self.output_j, self.output_loss_j,
            self.controller_j, self.leakage_j, self.capacitor_resistance_loss_j,
            self.charge_conversion_loss_j, self.curtailed_j))

    def to_dict(self):
        return {**asdict(self), "residual_j": self.residual_j}


class Bus:
    def __init__(self, bank=Bank(), initial_v=0, charge_efficiency=0.9,
                 output_efficiency=0.88, output_limit_w=10):
        self.bank = bank
        self.energy = bank.energy_j(initial_v)
        self.charge_efficiency = positive(charge_efficiency, "charge_efficiency")
        self.output_efficiency = positive(output_efficiency, "output_efficiency")
        if self.charge_efficiency > 1 or self.output_efficiency > 1:
            raise ValueError("efficiency cannot exceed one")
        self.output_limit_w = number(output_limit_w, "output_limit_w")

    @property
    def voltage(self):
        return math.sqrt(max(0, 2 * self.energy / self.bank.capacitance_f))

    def step(self, sources, requested_w, seconds, controller_w=0):
        number(requested_w, "requested_w")
        positive(seconds, "seconds")
        number(controller_w, "controller_w")
        if len({s.name for s in sources}) != len(sources):
            raise ValueError("duplicate source names can double count input")
        b, dt = self.bank, seconds
        c, r = b.capacitance_f, b.resistance_ohm
        before = self.energy
        # Exact constant bank-leakage current, clamped at zero stored energy.
        v0 = self.voltage
        v_after_leak = max(0, v0 - b.leakage_bank_a * dt / c)
        self.energy = b.energy_j(v_after_leak)
        leakage = before - self.energy
        v = v_after_leak
        source_j = sum(s.bus_w for s in sources) * dt
        input_j = sum(s.input_w for s in sources) * dt
        processed_j = sum(s.bus_w / s.efficiency if s.efficiency else 0 for s in sources) * dt
        wanted_output = min(requested_w, self.output_limit_w) * dt
        house_j = controller_w * dt
        need_j = wanted_output / self.output_efficiency + house_j
        esr_j = charge_loss = curtailed = 0.0
        delivered_bus = source_j
        if source_j < need_j and v > b.cutoff_v:
            # Terminal work = V0 I dt - I^2 (R dt + dt^2 / 2C).
            a, bb = r * dt + dt ** 2 / (2 * c), v * dt
            current_ceiling = min(b.max_discharge_a,
                                  c * (v - b.cutoff_v) / dt, bb / (2 * a))
            max_terminal = max(0, bb * current_ceiling - a * current_ceiling ** 2)
            terminal = min(need_j - source_j, max_terminal)
            disc = max(0, bb ** 2 - 4 * a * terminal)
            current = 0 if terminal == 0 else 2 * terminal / (bb + math.sqrt(disc))
            esr_j = current ** 2 * r * dt
            self.energy -= terminal + esr_j
            delivered_bus += terminal
        elif source_j > need_j:
            available = (source_j - need_j) * self.charge_efficiency
            a, bb = r * dt + dt ** 2 / (2 * c), v * dt
            current = 2 * available / (bb + math.sqrt(bb ** 2 + 4 * a * available))
            current = min(current, b.max_charge_a, c * (b.max_v - v) / dt)
            stored = bb * current + current ** 2 * dt ** 2 / (2 * c)
            esr_j = current ** 2 * r * dt
            used = (stored + esr_j) / self.charge_efficiency
            charge_loss = used - stored - esr_j
            self.energy += stored
            curtailed = max(0, source_j - need_j - used)
            delivered_bus = need_j
        house_served = min(house_j, delivered_bus)
        output_bus = min(wanted_output / self.output_efficiency,
                         max(0, delivered_bus - house_served))
        output = output_bus * self.output_efficiency
        # Tolerate only roundoff; never silently repair meaningful energy creation.
        ceiling = b.energy_j(b.max_v)
        if not -1e-8 <= self.energy <= ceiling + 1e-8:
            raise ArithmeticError("capacitor state outside physical energy bounds")
        self.energy = min(ceiling, max(0, self.energy))
        result = Step(input_j, processed_j - source_j, input_j - processed_j,
                      output, output_bus - output,
                      house_served, leakage, esr_j, charge_loss, curtailed,
                      self.energy - before, max(0, requested_w * dt - output),
                      house_j - house_served, self.voltage)
        if abs(result.residual_j) > 1e-7 * max(1, input_j, before):
            raise ArithmeticError("energy conservation failed")
        return result

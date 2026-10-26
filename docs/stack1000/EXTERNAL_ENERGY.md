# External energy qualification, including RF and static electricity

The selected 1 kW configuration is powered by sunlight. A different harvester can replace a source only after its conditioned output meets the same voltage, current, daily energy and availability requirements. Supply the matching input stage; never attach an antenna, high-voltage electrostatic collector, AC generator or thermoelectric element directly to a converter input based only on an open-circuit voltage.

## RF

For a known incident power density S and non-double-counted effective collecting area A, the idealized DC budget is `Pdc = max(0, S×A×efficiency - auxiliaries)`. Effective area depends on frequency, antenna gain, polarization, mutual coupling and field geometry. Do not multiply the same intercepted energy by the number of closely packed antennas. Multiple frequencies require non-overlapping spectral power accounting and measured rectifier response at actual input levels.

To illustrate units only: at an **assumed** 0.01 W/m² and 50% conversion efficiency, collecting 1,000 W before system losses would require 200,000 m² effective area. This is an arithmetic example, not a measured ambient density or a universal harvesting limit. No RF watts are included in the stack's baseline. A dedicated transmitter's power is an external energy input; include it in end-to-end efficiency.

## Static/electrostatic

A repeatedly discharged capacitor yields at most `0.5×C×(Vhigh²−Vlow²)` per cycle before losses. Average DC power is that energy times actual recharge-event frequency times efficiency, minus auxiliaries. For illustration, 1 nF charged to 10 kV stores only 0.05 J. Ten genuinely replenished cycles per second at 50% efficiency yield 0.25 W. These are assumed example values. Without recharging, this is a finite stored-energy discharge, not continuous generation. Never count mechanical work or externally supplied field energy as free internal feedback.

## Other abundant sources

A qualified water turbine, wind generator or maintained thermal gradient could supply external energy. Their collector, rectifier, regulation, thermal/mechanical assembly and source availability are separate designs. This release does not add an unbuilt fusion reactor or claim heat rejected by the same unit as net new input.

## Admission protocol

1. Define the collector boundary, dimensions, location and source ownership/operating conditions. Record all test-equipment energy injection, including RF generators and instrument bias feeds.
2. Measure loaded voltage/current and energy with calibrated instruments. Open-circuit voltage and peak pulses are insufficient. Characterize startup, minimum usable input, impedance and conversion efficiency over the real source spectrum/time series.
3. Meter auxiliary consumption and distinguish instantaneous output, average power and stored-energy discharge. Repeat with collector blocked/disconnected and with empty storage. Measure self-discharge separately.
4. For each stack channel, demonstrate the declared conditioned power/time envelope or rerun the sizing against measured data. A few seconds of peak RF power does not establish eight hours of replenishment.
5. Preserve raw traces, uncertainty, calibration, apparatus photos and protocol. Independent review must confirm the energy boundary and repeatability before claiming a rating.

`ix_zerocell.stack.rf_budget` and `static_budget` are unit-explicit calculators with negative controls. They are not field measurements. Primary background: Sharma et al., *Nanoscale spin rectifiers for harvesting ambient radiofrequency energy*, https://arxiv.org/abs/2408.01160. That work concerns weak-signal harvesting and does not validate the ZeroCell kilowatt claim.

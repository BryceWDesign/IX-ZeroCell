# Executed proof of concept and its boundary

The delivered proof of concept is computational and behavioral. There are no physical ZeroCell measurements in this package.

## Independent twenty-bank energy accounting

`python scripts/run_stack_campaign.py` executes the original repository's `Bus` energy solver once per channel, using actual constant-current capacitor work and I²R loss per step. The stack wrapper adds independent bank states and source profiles. It accounts for efficiency, leakage, local controls, charge-current limits, curtailed/rejected energy and unmet load. It does not treat sunshine at one channel as energy available to another.

The normal run starts all banks at 45.5 V, requests the conservative 60 W channel budget, and repeats sixteen hours without source plus eight with the qualified source, three times. Additional runs include four channels at only 20% source, forty-eight hours of darkness, empty storage without input and one bank below the capacitance requirement. The latter cases must report unmet load. Summaries, per-channel endpoints, reduced hourly traces and conservation residuals are stored in `results/stack1000/`.

The normal run proves only that the declared numerical envelope closes. A measured solar trace is not included. The 60 W energy stress run is intentionally separate from the output-current model; it is not a claim that the physical converter delivers 60 W at every bus voltage.

## Output-port circuit

`python scripts/run_stack_spice.py` runs ngspice on twenty current-limited behavioral regulator ports, physical 1.2 ohm ballast elements, generic nonlinear blocking diodes, feeder resistance and a common capacitor. It applies a load step and evaluates five cases:

| Case | Required outcome |
|---|---|
| Twenty nominal channels, 1,050 W internal demand | 46.5–50.5 V maintained |
| Nineteen low-current-limit channels, full demand | Must fail the voltage window |
| Nineteen channels, 1,000 W internal / 950 W useful target | Voltage window maintained |
| Twenty channels, 1,300 W overload | Must fail the voltage window |
| Zero energized sources | No useful output energy |

The negative-case load folds back below 40 V to avoid an infinite constant-power demand at zero volts. It may still dissipate power at a collapsed voltage; that is not successful 1,000 W service. These cases do not model the final hardware load-disconnect timing.

Regulator behavior and current limits are assumed output-port laws, not vendor LT8705 transistor models. The generic diode is not an ST-qualified model. The explicit simulated test supplies provide all circuit energy; no ambient source power is inferred. Storage and circuit screens have distinct boundaries and do not together establish switching-loop stability, thermal suitability or fault clearing. Circuit logs and traces are kept under `results/stack1000/spice/`.

## Repeatability and falsification

Run `python scripts/verify.py` for unit tests, native C++ advisory/fault logic and energy campaigns. Run both SPICE scripts with an installed ngspice. Run `python scripts/build_avr.py --fetch` on supported Linux to compile the retained small-build Uno monitor. `scripts/verify_release.py` coordinates the full set and records current status; it never reports hardware as verified.

The measurements reviewer requires twenty distinct bank records, actual capacitances, calibration/protocol artifacts, integrity hashes, uncertainty and timestamps. It rejects synthetic data as evidence of a measured result. A declared measured origin and passing arithmetic still produce only a review candidate, never hardware certification.

The physical proof remains the one-channel to five-channel to twenty-channel sequence in ASSEMBLY.md and BENCH_PROTOCOL.md. Green software CI is useful for reproducibility; it cannot close those physical gates.

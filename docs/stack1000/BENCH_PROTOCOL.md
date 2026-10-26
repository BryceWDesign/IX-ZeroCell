# Physical measurement protocol

No measured rows have been supplied. `measurements/stack1000/samples-header.csv` is a header-only acquisition format, not simulated or fabricated bench data.

Record synchronized time, all external input power, useful external load power, externally injected auxiliary/test power, output voltage, and all twenty independent bank voltages. The auxiliary column means externally injected energy, not the internal parasitic loads already drawn from the banks. Estimate storage change as the sum of twenty individual 0.5 C(Vfinal²−Vinitial²) terms. Squaring an average bank voltage is not equivalent.

Use independently characterized bank capacitances and bounded voltage/power errors. Identify all twenty channel assemblies and all instruments. Store actual calibration evidence and the signed experiment protocol alongside the samples, and hash the exact artifacts. Hashes detect byte changes, not fabricated measurements.

The `stack-1` metadata JSON requires exactly these fields:

- `schema`: `stack-1`; `origin`: `measured` or `synthetic`.
- `serial_numbers`: twenty distinct nonempty channel assembly IDs.
- `capacitance_f`: twenty measured equivalent bank capacitances in matching order.
- `capacitance_relative_error`, `voltage_error_v`, `power_relative_error`, `power_error_w`: conservative bounds.
- `max_gap_s`: at most one second for this screening protocol; higher-bandwidth transient acquisition is separately required.
- `instrument_ids`: nonempty instrument ID list.
- `artifacts`: `samples`, `calibration`, `protocol`, each with relative `path` and actual `sha256`.

Run `python scripts/review_stack_measurements.py path/to/bundle.json`. No ready-to-pass metadata or invented instrument IDs are included. Use the actual build data. Synthetic fixtures exist only inside unit tests and are explicitly rejected as proof.

For the 16-hour no-input review, the software checks at least 57,600 seconds, output power minus uncertainty at least 1,000 W at each sample, output voltage plus/minus error inside 46.5–50.5 V, initial bank voltage minus error at least 45.5 V, and bank operating bounds. It screens for detectable external power and energy closure, allowing bounded losses. A 1,000.0 W reading with nonzero uncertainty does not by itself prove a guaranteed 1,000 W floor.

No sampled-data reviewer establishes behavior between samples. Capture startup, switchover, load steps, reverse current and protective trips separately with sufficient bandwidth. Independently review thermal records, individual module voltage/leakage data, source availability and all fault tests. The three-cycle recharge test and site-weather qualification are additional requirements, not implied by a single no-input trace.

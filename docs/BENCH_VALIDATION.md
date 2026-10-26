# Physical validation record for the ZC-D10 reference build

There are no measured ZeroCell results in this release. No sample fixture is labeled as a real experiment. Do not deploy this prototype as someone's only emergency power source.

## First milestone

Use the complete assembly in `docs/build/ASSEMBLY_GUIDE.md` and its declared
stock bank: four 10 F cells in series, 2.5 F equivalent at 10 V. The first test
is regulated 5 V / 1 W service from a known source, followed by a brief metered
input interruption. Qualify 5 W and 10 W sustained source-fed service next.
The 20 W point is a separate unit-specific test, not an already measured rating.

The stock nominal bank has 125 J total energy and 113.75 J ideal between 10 and
3 V. It provides seconds at useful high loads, not hours. Do not use the former
large-bank sizing examples as the storage specification of the released kit.
The source-off interruption time, actual capacitor state and losses must all be
measured. No 60-second/1 W source-off result is assumed for the stock assembly.

## Required apparatus and metering boundaries

- Current-limited bench supply first; a panel or generator is introduced only after supply tests pass.
- Independently metered input connector power, regulated output power, and all auxiliary input paths (including USB/serial/debug power).
- Individual cell voltage, independently checked bank voltage, bank temperature, output voltage and the actual load waveform.
- Calibrated capacitance/DC resistance and a leakage test after the manufacturer's stabilization/soak procedure. Count balancing, divider, LED, regulator and telemetry consumption.
- A load with known power and source-disconnect switching rated for the bank's fault energy. Use independent hardware voltage/current/thermal cutoffs, a correctly selected DC fuse near storage, insulated terminals and a controlled discharge path. Low voltage does not eliminate capacitor short-circuit hazards.

All instruments' ranges, calibration dates, uncertainty bounds and sample synchronization must be recorded. Set the sample interval to resolve the fastest relevant load/source event; the CSV tool cannot detect a spike between samples. Record oscilloscope captures for switching and transients separately from average-power logs.

## Required tests

| Test | Required observation |
|---|---|
| Empty buffer, zero source | No useful output; no unexplained charge rise. |
| Known DC source, empty buffer | Record cold-start time, inrush, all cell voltages and actual input energy. |
| Source removed | Measured useful output is bounded by the decrease in stored energy after all losses. |
| 1 W for 60 seconds | Regulated output stays within the predeclared range, and all samples meet the load target after uncertainty. |
| 5 W service extension | Repeat metering with the intended converter, connectors and bank; no inference from the 1 W test. |
| Temperature/imbalance faults | Independent hardware cuts power; software trips; recovery requires explicit reset and valid fresh data. |
| Lost/stale/malformed telemetry | Load-enable defaults off; an external watchdog also removes permission if the MCU hangs. |
| Optional source removal/reconnection | No backfeed, unstable restart loop or unbounded inrush. |
| 20 W DC extension | Dedicated converter/current/connector review, hot and cold source tests, measured efficiencies and fault tests. The default AVR configuration does not authorize 20 W. |

## Measurement bundle format

Create `experiment.json` beside `samples.csv`, a real calibration record and a predeclared protocol file. Artifact SHA-256 values are computed from those actual files. The schema is defined by `ix_zerocell/evidence.py`; its required metadata fields are listed below.

`schema` is `"1"`; `origin` is `"measured"` only for actual instrument acquisitions. `instrument_ids` identifies `input`, `output` and `storage`. `artifacts` identifies `samples`, `calibration` and `protocol`, each by a relative `path` and matching `sha256`.

Numeric fields are `capacitance_f`, `capacitance_relative_error`, `voltage_absolute_error_v`, `power_relative_error`, `power_absolute_error_w`, `max_sample_gap_s`, `target_load_w`, `minimum_duration_s`, `output_voltage_min_v`, `output_voltage_max_v`, and `max_unmetered_loss_w`. Set them from instrument capability, a defined experiment and a physically justified loss bound. An operator can falsify metadata; the program does not authenticate an experiment.

Exact CSV columns:

```csv
time_s,input_w,output_w,auxiliary_w,bank_v,output_v
```

`input_w` is the sum of **all external electrical input power**, including an independently powered debug/USB connection when present. `output_w` is useful load power. `auxiliary_w` is **internal housekeeping power consumed**, already supplied by those inputs or the capacitor, and excludes the useful load. It is not an additional external input. Do not count a current twice. Initial capacitor energy is recorded through `bank_v`, not labeled as newly harvested input.

```powershell
python -m ix_zerocell review path/to/experiment.json
```

The tool integrates actual input/output/auxiliary power and capacitor energy change, rejects broken hashes/paths/times, and applies declared conservative uncertainty bounds. A successful result is only `MEASUREMENT_REVIEW_CANDIDATE`. It always leaves `hardware_validated` false and requires independent review. Synthetic test fixtures never qualify. Qualification also needs reviewed schematics, part tolerances, electrical/thermal testing and the intended environmental tests.

## Twenty-channel profile

The larger ZC-S1000 target has separate assembly/release requirements in `stack1000/ASSEMBLY.md`, `stack1000/BENCH_PROTOCOL.md` and `stack1000/RELEASE_GATES.md`. Use the twenty-bank measurement schema; a single-bank averaged-voltage review cannot establish its storage change. Do not apply the small-build output/current limits to the stack.

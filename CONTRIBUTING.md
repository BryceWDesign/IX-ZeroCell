# Contributing to IX-ZeroCell

Read the current README, docs/RESEARCH_AND_DECISIONS.md and
docs/BENCH_VALIDATION.md. Code changes must pass python scripts/verify.py;
firmware changes also need the actual AVR build in CI.

Label model parameters as assumptions. Physical claims require raw instrument
traces, calibration, declared uncertainty and independent review. Do not
restore the withdrawn historical output/compliance claims or describe a
simulation pass as physical power generation. Preserve attribution and the
Apache-2.0 license. Do not import code under incompatible or unresolved donor
licenses into this package.

Useful contributions include qualified source/charger interfaces, capacitance
and leakage measurements, reviewed protection circuits, verified schematics,
source-loss tests, and calibrated load profiles. The next physical target is
stated in docs/BENCH_VALIDATION.md.

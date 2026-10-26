# Hardware overview, v0.2.0

Two distinct configurations are supplied:

- **ZC-D10**: specified populated-module reference assembly, nominal 5 V / 10 W design target and short interruption buffering. See `hardware/reference_build/` and `docs/build/`. It has a complete module-level guide, but no measured ZeroCell rating.
- **ZC-S1000-B**: twenty-channel solar/supercapacitor architecture targeting 1,000 W useful output at nominal 48 V. See `hardware/stack1000/` and `docs/stack1000/`. Uses 60 panels, 80 populated converter boards and 1,200 EDLC modules. Its control/protection and installation release gates remain open.

Do not merge the small board's 5 V wiring, 2.5 F bank or firmware limits into the 1 kW installation. The original RF/static construction notes under archive are withdrawn and not current build instructions. The prior 50 W PDF and stack concept A are traceability documents; revision B controls current stack quantities/settings.

Source conditions and losses determine output. Nothing here is a physically demonstrated self-sustaining generator. The latest machine-readable hardware status is false, independent of software CI.

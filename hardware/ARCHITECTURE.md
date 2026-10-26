# Active architectures

For the small ZC-D10 reference, use `reference_build/BOM.md`, `reference_build/WIRING.md` and `../docs/build/ASSEMBLY_GUIDE.md`.

For ZC-S1000 revision B, use `stack1000/design.json`, `stack1000/BOM.md`, `stack1000/WIRING.csv` and `../docs/stack1000/DESIGN.md`. The stack combines protected converter outputs, not raw capacitor banks. Source and storage quantities are explicit; 60 W/channel is a conservative storage calculation allowance, not a measured individual output rating.

The active 1 kW design requires 60 parallel capacitor modules per channel and twenty channels. Original active-droop concept A and the standalone 50 W design are superseded where their values differ. Do not execute archived 2025 assembly instructions. No full stack construction release is asserted.

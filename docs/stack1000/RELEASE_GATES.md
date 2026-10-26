# Construction release gates

These are unresolved engineering tasks, not completed tests or disguised optional enhancements. The machine-readable register is `hardware/stack1000/release_gates.json`. All are open in this delivery. An engineer should not purchase the full 1,200-module bank on the basis of a passing software badge.

| Gate | Required evidence to close |
|---|---|
| G01, protection implementation | Complete schematic/netlist/layout or selected populated assembly for independent OV, alarm continuity, thermal latch, A5 gate, K1 driver and fault-priority reset. Verify power-up/down fail states and all auxiliary fuses. |
| G02, output stage | Modified DC1924A operates across 21–51 V input, stays within current limits, output sharing envelope and 85% path efficiency floor; includes startup, weak source, thermal soak and measured switch overshoot. |
| G03, capacitor branch protection | DC fuse/resistor/terminal/wire coordination, resistor pulse energy, maximum credible fault study including failure of blocking devices and faults upstream of branch resistors. |
| G04, storage acceptance | Actual per-module capacitance, leakage, ESR, temperature behavior and individual voltages meet sizing bounds; records identify serial numbers and conditioning time. |
| G05, combiner and load protection | Selected section/main disconnects, two-ended feeder protection, bus precharge, bus capacitance, independent overvoltage/load shutdown, fault interrupt ratings and limited-energy fault testing. |
| G06, mechanical and source installation | Real rack drawings, module restraints, floor/anchorage calculations, conductor schedules, outdoor PV design, thermal management and site solar time-series qualification. |
| G07, physical power demonstration | Metered 1,000 W external load, sixteen hours without PV after full solar charge; at least three replenishment cycles; startup/transfer/one-channel-failure tests. Account for all auxiliary/test power and measurement uncertainty. |

Gate closure needs linked, reviewed artifacts, not a boolean edited by hand. Software output never changes `hardware_validated` to true. No schematic approval, certification, safe-short-circuit claim or procurement release is implied by the component schedule.

This release materially advances the design by replacing the unspecified custom sharing converter with a concrete populated-board modification and passive-sharing circuit, supplying a complete *assembly-scope inventory*, and executing source/storage and output-port models. It does not supply a completed production control PCB or a proven working device. The remaining work is stated directly rather than filled with fictional parts or measurements.

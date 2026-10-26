# Claim authority, version 0.2.0

| Statement | Evidence/status |
|---|---|
| Battery-free everyday DC power from external energy is the mission | Design objective |
| ZC-D10 module-level construction documents exist | Retained 10 W target assembly package; physical unit unverified |
| ZC-S1000 targets 1,000 W useful DC output | Twenty-channel design, not a measured rating |
| Sixteen-hour no-input target closes under declared bounds | Calculation and numerical simulation; requires full starting charge and qualified components |
| Twenty channels share a bus in the supplied model | Executed generic behavioral SPICE and steady-state screen, not complete vendor switching simulation |
| Full assembly-scope inventory and staged walkthrough exist | Delivered; unreleased protection/mechanical assemblies remain explicitly identified |
| Complete fabrication-ready 1 kW hardware package | **Not delivered**: G01–G06 in RELEASE_GATES.md remain open |
| Physical 1,000 W source and three daily cycles demonstrated | **Not performed**: G07 remains open |
| Current local software checks pass | See results/verification.json and results/release_verification.json |
| Hosted CI for this update is green | Unknown until pushed and run; badge is live, never hardcoded green |
| Original 1,120–1,370 W RF/static output was measured | Withdrawn; no supporting raw evidence supplied |
| RF/static harvesting itself is impossible | Not claimed; availability, collecting area and losses must establish any proposed output |
| Feedback/resonance creates net energy | No such credit allowed |
| Safe fault clearing, certified enclosure/installation or compliance | Not established by this repository |

Computed output, behavioral simulation, code execution, physical measurement and independent review remain separate evidence classes. A measurement label or hash cannot authenticate a physical test. A hardware rating requires the actual test records and completed protection design.

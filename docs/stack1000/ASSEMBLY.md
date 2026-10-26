# ZC-S1000 staged assembly and commissioning walkthrough

Read DESIGN.md, BOM.md, WIRING.md and RELEASE_GATES.md together. The channel consists of purchased populated power boards plus rework and **unreleased protection assemblies**. This is a staged engineering assembly procedure; it is not authorization to energize a full capacitor bank before those assemblies and fault studies are complete. The existing ZC-D10 guide is a separate small reference build, not a scale-model validation of this installation.

## A. Establish the build record

1. Assign assembly identifiers CH01–CH20 and module identifiers C01–C60 within each channel. Record actual manufacturer model, revision, serial number and supplier provenance.
2. Print the current revision-B BOM and route schedule. Mark all seven release gates open. Do not substitute earlier 56-module quantities or the 12 V Traco output from the prior PDF.
3. Obtain the manufacturer documents listed in SOURCES.md. Check component ratings and exact board revision against the delivered components.
4. Build and characterize one output-board prototype first. Do not purchase/install 1,200 storage modules merely because the computation passed.
5. Establish a current-limited bench area with a suitably rated electronic load, calibrated meters, differential voltage probes and temperature logging. Bench supplies are external energy inputs. No oscilloscope ground clip is permitted on a floating capacitor tap.
6. Design and review racks, floor loading, access, guarded terminals, protective bonding, PV mounting and cooling before bulk mechanical assembly. Retain inspection and torque records. Use manufacturer torque limits for actual lugs and terminals, not guessed universal values.

## B. Modify and qualify the populated converter boards

7. Remove all power and discharge onboard capacitors according to the manufacturer's instructions. Confirm zero voltage with a suitable meter immediately before rework.
8. Label four boards per channel A1 through A4. Photograph both sides and identify R11/R14, R13/R16, R49, R53/R54, R55 and JP1 using the actual schematic. Do not infer designators from a different board revision.
9. Fit the A1 fixed/trim parts from DESIGN.md. Remove R55 and populate the R53/R54 input-regulation divider. Keep the existing power-stage components and sense shunts unless a separately reviewed change is required.
10. Fit A2/A3 charging settings. Each board has its own input fuse and reverse-blocking output diode. Do not assume the two chargers' currents are equal without measuring them.
11. Fit A4 settings: output divider for 50.0 V, adjustable current resistor calibrated to 1.17 A and the 294 kohm/20 kohm input-UVLO divider. Retain default R55; leave R53/R54 unpopulated for A4. Insulate trim assemblies, mechanically secure them and seal only after calibration.
12. Set all four JP1 jumpers to the documented DCM position. Verify continuity, polarity and absence of solder bridges under magnification.
13. Test each board individually from a bounded supply. Start disabled with TP5 tied to ground, connect VIN at TP1/TP3 and the controlled load at TP2/TP4, then follow the vendor startup procedure. Set the supply current high enough for the intended bounded test, not for an uncontrolled short.
14. Calibrate A1 to 49.5 V and approximately 1.99 A limit. Calibrate A2/A3 to 46.5 V and nominal 4.96 A; qualify each within 4.5–5.5 A. Verify input-power priority and source-voltage regulation.
15. Calibrate A4 to 50.0 V. Sweep 21, 22, 32, 45.5 and 51 V input and progressively load from zero to its current limit. Require current limit within 1.14–1.20 A and acceptable startup/restart. Do not infer the low-input result from ADI's 36 V full-load efficiency curve.
16. Scope switching/output overshoot using the proper probe setup. Demonstrate margin to the original board's 60 V output MOSFET ratings, output-capacitor ratings and every protection-device limit. Check thermal soak and ripple at the actual mounting arrangement.
17. Record complete-path input/output energy. The design needs at least 85% useful-output-path efficiency including source OR, gate, A4, ballast, blocking diode and local feeder losses. Reject or recalculate if that bound fails anywhere in the operating envelope.

## C. Validate two-channel sharing on limited-energy supplies

18. Mount one 1.2 ohm ballast per A4 on its rated metal support. Mount D5 with appropriate cooling, joining its two anodes and orienting its cathode toward the common bus.
19. Fit local and bus-end output protection. Route matched output/return feeders. Use the 5,790-route CSV as a topology checklist; G01/G05 entries are logical interfaces until the gate assemblies have actual approved pinouts.
20. Characterize the assembled branch at 0.8, 1.0 and 1.14 A. Fit the local load-line and verify E = 49.4–49.6 V and R = 1.23–1.27 ohm across input and temperature. Record nonlinear residuals; if the affine envelope does not bound the branch, the analysis must use the measured curve instead.
21. Combine two channels through their blocking paths. Sweep shared load, startup order, input removal and recovery. Record circulating/reverse current and current sharing. An equal-current display at one operating point is insufficient.
22. Test channel shutdown while the shared bus stays energized. Verify no uncontrolled charge path into the disabled converter or bank. Check failure hypotheses for an open/shorted diode and loss of the hardware permit on a bounded fixture.
23. Complete G02 before extending this output circuit to more channels. The generic ngspice output model is not a substitute for these measurements.

## D. Complete independent protections before attaching large storage

24. Complete the G01 protection schematic and assembly. The independent 47 V charge cutoff must latch, interrupt source power and inhibit conversion even if the logger is absent or wedged. Establish fault-priority reset behavior and a defined de-energized state.
25. Implement and test the A5 input gate with the revised load current/inrush, pass-FET SOA and UVLO/restart settings. The old 50 W timer/shunt values are not automatically approved for this larger path. Verify cold start without repeated foldback.
26. Fit and coordinate all auxiliary fuses and the PV-only coil driver. Measure total standby/night control power at no more than 4 W per channel and daylight auxiliary allocation at no more than 10 W. Budget any fans explicitly.
27. Inject OV, UV, thermal, module-alarm, cable-open, sensor-fault and power-loss conditions. A disconnected alarm cable must not silently report healthy. Establish the module-alarm pull-up and sink limits from Eaton's manual.
28. Complete G03 branch fuse/resistor coordination, including maximum credible fault energy and upstream unprotected terminal segments. Use a bounded fixture; do not perform a direct-short demonstration on a fully charged bank.
29. Complete G05 common-bus overvoltage, undervoltage/load shutdown, precharge, feeder backfeed protection and section/main interrupt ratings. Confirm precharge does not rely on an unspecified bus capacitor value. The external load stays disconnected until the bus and channel permits are valid.

## E. Characterize and install storage

30. Characterize each isolated module's capacitance, ESR and conditioned leakage over the declared temperature range. Require at least 132.8 F effective capacitance, no more than 10 milliohm ESR and no more than 10 mA leakage under the declared protocol. Preserve raw traces and actual conditioning time, not just pass labels.
31. Check each module's voltage immediately before handling. Follow Eaton's controlled discharge procedure. Do not short terminals, use an ammeter as a discharge wire, or assume an open isolator has removed stored energy.
32. Install fifteen restrained modules per rack, four racks per channel. Maintain access to labels, alarms and insulated terminals. Qualified engineering must approve floor loads and anchorage.
33. Install each local positive-terminal fuse as close as practicable to its module, followed by its individual 2.2 ohm resistor and protected lead to CB+. Connect each negative independently to B0. Protect the unfused terminal segment mechanically.
34. Equalize modules within 0.1 V before making parallel connections with chargers and loads isolated. Verify polarity, branch continuity, resistance and terminal retention. Do not connect a charged module to an empty bank and expect the resistor/fuse to perform routine equalization safely.
35. Compare every branch to WIRING.csv. Confirm that no wire bypasses its resistor and no busbar ties positive storage buses from different channels together.
36. Install temperature switches, alarms and supervised harnesses from the completed G01 drawings. Verify all sixty module alarm paths and cable-open detection individually.

## F. Integrate source and output

37. Connect three PV modules in parallel per channel using the selected branch and main fuses and compatible connectors. Keep panels covered/disconnected during wiring. Never connect these panels in series into the 80 V boards.
38. Verify worst-case cold open-circuit voltage for the actual site/panel tolerance. The earlier model used about 70.73 V at -40 °C for the selected panel, below the 80 V nominal board input ceiling; surge/transient protection still needs its own study.
39. Route K1 switched PV power to A1–A3. Route A1 through D1 to SUPPLY+; A2/A3 through D2/D3 to the channel bank; gated bank through D4 to SUPPLY+. Route SUPPLY+ through its fuse to A4.
40. Route A4 through ballast/D5/local protection to the bus-end fuse, then its section. Connect returns to the assigned star. Follow the approved bonding plan; do not rely on chassis mounting as a current-return conductor.
41. Establish the PV-only auxiliary feed before K1 and the separately fused bank auxiliary feed. Meter both; a hidden mains-powered controller invalidates a battery-free autonomous energy test.
42. Demonstrate daylight direct-load service with storage isolated. Verify that weak PV causes charging to yield before the load collapses, and that inadequate input leads to controlled shutdown rather than repeated uncontrolled restarts.
43. Charge a qualified bank while measuring every module voltage. Demonstrate zero/low-voltage charging under the accepted charger limits. Log initial charge duration, which can span more than one day.
44. Confirm ready status only when every module meets the minimum 45.5 V initial condition. Startup reserve is not free energy; it must have been accumulated from measured input.

## G. Scale and prove

45. Complete one-channel source-loss and recharge tests first. Use a metered load and all real auxiliaries. Record temperature, bank/module voltage, input/output power and protection events.
46. Commission a five-channel section. Repeat startup sequencing, load-step, sharing and controlled branch removal. Verify feeder drop and section protection.
47. Commission four sections into twenty-channel service with the external load initially open. Test limited load levels before 1,000 W. Check each branch's current and temperature; aggregate output can hide a failing channel.
48. At the external terminals, establish 1,000 W with voltage staying 46.5–50.5 V and common losses/auxiliaries within 50 W. Test constant-power load behavior as well as resistive loading.
49. After measured solar charging to ready, remove the solar input and run sixteen hours. Meter any alternative input or test-equipment injection. Use the stack measurement schema, calibration records and independent review; supply uncertainty margin above the nominal 1,000 W reading.
50. Repeat at least three source/no-source cycles with the stipulated real source envelope. Require no downward trend in usable stored energy and no hidden external charging. Perform a separate site-weather analysis before making seasonal uptime claims.
51. Remove one channel and command no more than 950 W useful service. Demonstrate load reduction before bus undervoltage. The current supervisor is advisory code, so this needs the completed real load-control hardware.
52. Test prolonged darkness, insufficient PV, unequal banks, failed telemetry and overload. Record failures and trips, not just successful curves. Do not claim unlimited no-sun continuity or N+1 operation from this twenty-channel design.
53. Close gates only with linked, reviewed measurements and drawings. Until G01–G07 are closed, label the equipment **engineering prototype, unqualified**, and keep public output claims at the design-target level.

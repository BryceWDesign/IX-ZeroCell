# IX-ZeroCell™ Full Build Guide

**Author:** Bryce Wooster  
**License:** Apache 2.0  
**Version:** v1.0  

---

## Table of Contents
- [Overview](#overview)
- [Tools Required](#tools-required)
- [Part 1: Mechanical Assembly](#part-1-mechanical-assembly)
- [Part 2: Electrical Wiring](#part-2-electrical-wiring)
- [Part 3: Capacitor Bank & Rectifier Assembly](#part-3-capacitor-bank--rectifier-assembly)
- [Part 4: RF Harvester Integration](#part-4-rf-harvester-integration)
- [Part 5: Enclosure Integration](#part-5-enclosure-integration)
- [Part 6: First Power-Up Test](#part-6-first-power-up-test)
- [Part 7: Troubleshooting](#part-7-troubleshooting)

---

## Overview

The IX-ZeroCell is a no-battery ambient-powered energy harvesting system using:

- 99 linear shake flashlight generator tubes
- Supercapacitor storage
- High-voltage rectifiers and regulators
- RF energy harvesting subsystem

**Estimated Build Time:**  
Approx. 20–25 hours (solo builder)  
Approx. 10–12 hours (2-person team)

**Footprint Size Estimate:**  
Roughly similar to a medium trash can or mini fridge.  
Approx. 60cm x 60cm x 90cm (subject to enclosure choice).

---

## Tools Required

- Soldering iron + solder  
- Heat shrink tubing and heat gun  
- Wire stripper + cutter  
- Screwdriver set  
- Epoxy glue or 3D-printed brackets (optional)  
- Multimeter  
- Drill (for enclosure prep)  

---

## Part 1: Mechanical Assembly

1. **Tube Frame Build**  
   - Build a 11×9 grid (99 total) using aluminum or acrylic rails.
   - Leave 2–3 cm spacing between each tube.
   - Secure each flashlight tube using brackets, zip ties, or custom mounts.

2. **Tube Orientation**  
   - Ensure all magnets can freely move inside tubes.
   - Tubes should be vertically aligned with magnets resting at the bottom when idle.

3. **Vibration Tuning (Optional)**  
   - Attach the frame to rubber mounts or a spring suspension if mobile deployment is planned.

---

## Part 2: Electrical Wiring

1. **Tube Coil Outputs**  
   - Harvest AC from each coil tube.
   - Group wires in bundles of 11–12 for easier routing.

2. **Rectification**  
   - Connect all tube outputs to ultra-fast diode bridge rectifiers (rated for min. 500V 5A).
   - Parallel outputs after rectification.

3. **Voltage Regulation**  
   - Route rectified DC through appropriate buck converter modules.
   - Target output: 12V DC stable, adjustable as required.

4. **Wiring Specs**  
   - Use 16 AWG silicone wire for main bus lines.
   - Use heat shrink at all soldered joints.

---

## Part 3: Capacitor Bank & Rectifier Assembly

1. **Supercapacitor Bank**  
   - Install a bank of 6–12 supercapacitors rated minimum 16V, 500F total combined.
   - Include balance boards if capacitors are in series.

2. **Charging Circuit**  
   - Link rectified/regulator output directly into the capacitor bank with appropriate current-limiting resistor.

3. **Output Bus Setup**  
   - From capacitors, output to terminal block or USB/DC output modules.

---

## Part 4: RF Harvester Integration

1. **Antenna Placement**  
   - Install 4–6 RF antenna loops or telescoping whips.
   - Mount externally or inside enclosure top, clear of metal obstructions.

2. **RF to DC Modules**  
   - Connect RF modules in parallel to the capacitor bank input.
   - Verify no backfeed occurs from capacitor to antenna.

3. **Tuning Check**  
   - Use RF sniffer or scope to verify effective signal harvesting.
   - Adjust loop diameter or whip length as needed.

---

## Part 5: Enclosure Integration

1. **Housing Options**  
   - Use a weatherproof plastic storage bin or custom 3D-printed shell.
   - Ensure venting for heat and airflow.

2. **Cable Routing**  
   - Route all input/output cables through rubber grommets or cable glands.

3. **Mounting**  
   - Bolt unit down if placed in a mobile or outdoor environment.

---

## Part 6: First Power-Up Test

1. **Initial Check**  
   - Verify all connections with multimeter before powering up.

2. **Shake Test**  
   - Shake or vibrate unit gently and confirm charging activity on capacitor bank.

3. **RF Harvesting Verification**  
   - Monitor capacitor voltage rise while idle (ambient RF only, no shaking).

4. **Load Test**  
   - Connect small 12V load (LED strip, small fan).
   - Verify stable operation.

---

## Part 7: Troubleshooting

| Issue                          | Possible Cause               | Fix                                |
|--------------------------------|-----------------------------|------------------------------------|
| No voltage output              | Loose wire, bad rectifier   | Re-check wiring, replace parts     |
| Capacitors not charging        | Bad regulator, bad diode    | Swap modules, test separately      |
| RF harvesting ineffective      | Poor antenna placement      | Re-tune antennas, adjust position  |
| Overheating regulators         | Underrated buck converters  | Upgrade to higher-rated modules    |
| Spark/arcing                   | Improper insulation         | Re-solder, re-insulate connections |

---

**End of Build Guide**  
IX-ZeroCell™ by Bryce Wooster, 2025  
Licensed under Apache License 2.0


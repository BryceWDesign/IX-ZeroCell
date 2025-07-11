# IX-ZeroCell™ Wiring Diagram Notes  
**Author: Bryce Wooster**

---

## Purpose
This file provides contextual notes and specifications regarding the IX-ZeroCell™ system’s wiring diagrams as referenced in schematics and CAD drawings.

---

## Core Wiring Architecture Overview

1. **Magneto-Induction Array:**
   - **Wire Type:** AWG 20 copper enamel magnet wire.
   - **Configuration:** 99 coil tube assemblies in series-parallel hybrid layout.
   - **Total Length (Per Coil Tube):** 15 meters.

2. **Energy Harvesting Antenna Feeds:**
   - **Primary Input Wire:** Silver-plated RF coaxial, RG316 or equivalent.
   - **Connection Method:** Soldered with EM-shielded heat shrink.

3. **Grounding System:**
   - **Wire Type:** AWG 16 stranded copper with braided shielding.
   - **Connection Points:** Chassis ground, coil array negative terminals, external earth ground.

4. **Control Circuit Feed Lines:**
   - **Type:** Low-noise silicone insulated wire, AWG 22.
   - **Purpose:** Power monitoring module and shutdown trigger circuit.

---

## Color Code Standard

- **Positive Power Output:** Red
- **Negative Power Return:** Black
- **Control/Signal:** Yellow
- **Ground:** Green

---

## Practical Layout Notes

- **Loop Avoidance:** No wiring loop exceeding 30 cm in diameter should exist to prevent unwanted inductive feedback.
- **Distance Spacing:** Maintain 5 mm minimum spacing between parallel power and control wires.
- **Insulation Clearance:** High-temperature insulation mandatory for all coil wires to handle potential heating.

---

## Maintenance and Safety Inspection Points

- **Visual Checks:** Monthly inspection of all exposed wiring for signs of heat damage or insulation wear.
- **Continuity Tests:** Use a digital multimeter to check each coil segment during initial build and every 6 months thereafter.
- **Re-torque Check:** Verify terminal screws and grounding connections hold their specified torque values annually.

---

## Compliance Notes

- Wiring and assembly must comply with IEC 60204-1:2016 (Electrical equipment of machines — Part 1: General requirements) where applicable.

---

## Revision History
- **v1.0** — July 2025 — Initial release by Bryce Wooster.

---

© 2025 Bryce Wooster. Licensed under the Apache License 2.0.

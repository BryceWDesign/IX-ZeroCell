# IX-ZeroCell™ — Full Master BOM  
**Configuration:** 99 Magnetic Induction Tubes  
**Author:** Bryce Wooster  
**License:** Apache 2.0  

> 📦 All parts are based on real, commercially available components. Costs are estimated in USD per unit as of 2025.

---

## ✅ SECTION 1 — Magnetic Induction System

| Qty | Part                             | Specs                             | Est. Unit Cost | Notes                         |
|-----|----------------------------------|-----------------------------------|----------------|-------------------------------|
| 99  | Magnetic Shake Flashlight Tube   | 1.5–2V peak AC, 6"–9" length       | $3.50          | Harvested for neodymium magnet + coil |
| 99  | Neodymium Magnets (in-tube)      | N42 Grade, 10mm x 30mm            | Included       | Extracted from flashlight tube |
| 99  | Copper Coil (in-tube)            | 26–28 AWG, 1000 turns             | Included       | From flashlight tube           |
| 1   | Central Tube Array Frame         | Non-metallic, modular housing     | $30.00         | 3D printed or laser-cut       |
| 3   | ABS Mounting Rails               | 18–24" support rails              | $12.00         | Holds vertical tube stacks     |

---

## ✅ SECTION 2 — Energy Conditioning & Storage

| Qty | Part                             | Specs                             | Est. Unit Cost | Notes                        |
|-----|----------------------------------|-----------------------------------|----------------|------------------------------|
| 12  | Bridge Rectifier Modules         | KBPC5010 or similar               | $1.00          | 8A 1000V full bridge per 8–10 tubes |
| 3   | Supercapacitors (Banks)          | 2.7V 500F (x6) series banks       | $18.00         | Total ~16V 80F after series config |
| 3   | Supercap Balancing Boards        | Passive or active, 6-cell         | $4.00          | One per supercap bank        |
| 1   | Output Voltage Regulator Board   | Buck converter, 12–24V input      | $3.00          | Set for 5V, 12V, or USB-C out |
| 1   | Schottky Diode Pack              | 1N5822 or equivalent              | $5.00 (bulk)   | For reverse current protection |

---

## ✅ SECTION 3 — RF/VLF Ambient Harvesting

| Qty | Part                             | Specs                             | Est. Unit Cost | Notes                         |
|-----|----------------------------------|-----------------------------------|----------------|-------------------------------|
| 2   | Ferrite Rod Antennas             | 100–200kHz, 4"–6"                 | $2.50          | For VLF harvesting            |
| 1   | Wideband Passive RF Antenna      | 3MHz–1GHz coverage                | $7.00          | Indoor or rooftop mount       |
| 2   | RF-to-DC Harvesting Boards       | LTC3588-based or similar          | $4.00          | Converts weak ambient RF      |
| 1   | Grounding Rod (optional)         | 1.5ft copper                      | $3.00          | For better noise floor        |

---

## ✅ SECTION 4 — Structural / Enclosure

| Qty | Part                             | Specs                             | Est. Unit Cost | Notes                         |
|-----|----------------------------------|-----------------------------------|----------------|-------------------------------|
| 1   | Main Enclosure Box               | 24"x18"x12" plastic/composite     | $25.00         | Weatherproof recommended       |
| 1   | Acrylic Display Window (optional)| 8"x6", 3mm thick                   | $6.00          | For visual demonstration        |
| 12  | Mounting Brackets / Bolts        | M3/M4 size                        | $4.00          | General structural mounting     |
| 1   | Wiring Harness / JST Kit         | 100 pcs assorted                  | $8.00          | Solderless where possible       |

---

## ✅ SECTION 5 — Tools & Assembly (Not included in BOM cost)

- **Soldering iron**  
- **Multimeter / Oscilloscope (for testing)**  
- **Wire strippers, cutters, zip ties**  
- **Epoxy or mounting adhesive (optional)**  
- **3D printer or access to laser cutter (optional)**

---

## ✅ TOTAL ESTIMATED COST

| Component Group              | Est. Cost |
|-----------------------------|-----------|
| Induction System (99 tubes) | $346.50   |
| Energy Storage / Regulation | $82.00    |
| RF Harvesting Hardware      | $21.00    |
| Structural & Wiring         | $43.00    |
| **Total Build**             | **$492.50** USD

---

## ✅ BUILD TIME ESTIMATE

| Task                            | Time Estimate |
|---------------------------------|---------------|
| Disassembling 99 flashlight tubes | 3–4 hours     |
| Coil interconnection & routing    | 2–3 hours     |
| Supercap & rectifier wiring       | 1.5 hours     |
| RF subsystem installation         | 1 hour        |
| Final housing & test             | 2 hours       |
| **Total Build Time**             | **~10–12 hours** (1–2 people)

---

## ✅ Power Applications (Realistic)

- 24/7 BLE beacon or wireless sensor nodes  
- LED strips, small logic circuits, Arduino, ESP32  
- 5V USB device charging (slow trickle, not burst)  
- Low-powered shortwave/ham receiver  
- Grid-free field deployment sensors  
- Educational demonstration kits

---

## 🧠 Final Notes

This BOM assumes ambient EM noise floor and coil motion is harvested passively, not through continuous mechanical actuation. Output is suitable for **low and ultra-low power systems**. Scaling beyond this requires additional stages or kinetic input (manual crank, etc).

If you're looking to pair this with more active magnetic piston drivers or Tesla-style resonance harvesting: start a fork and build v2.

---


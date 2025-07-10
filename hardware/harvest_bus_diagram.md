# IX-ZeroCell – Harvest Bus Diagram (Node A Integration)

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Provide a comprehensive visual and descriptive map of all energy harvesting inputs and how they merge safely into the MPPT system via Node A

---

## 🧲 Inputs to the System

All ambient or motion-based harvesters feed into a unified bus node (**Node A**), where their outputs are:

1. **Rectified (if AC or HV pulse)**
2. **Clamped/protected (TVS, Schottky)**
3. **Filtered**
4. **Steered via diode to prevent backfeed**

---

## 📐 Textual Diagram Layout

```txt
                    +-------------------------+
                    |     Kinetic Coils (99x) |
                    |     — Handshake Tubes   |
                    +------------+------------+
                                 |
                           +-----v------+
                           | Bridge AC/DC|
                           +-------------+
                                 |
                                 +---> [Schottky] ----+
                                                       |
+---------------------+                               |
| Piezo / Tribo Pads  |---> Bridge -- TVS -- R100Ω ----+
+---------------------+                               |
                                                       +---> NODE A (Unified Harvest Rail)
+---------------------+                               |
| RF Rectifier Paths  |---> Matching → Diodes --------+
+---------------------+                               |
                                                       |
+---------------------+                               |
| TEG Modules (3+)    |----> Series → Diode -----------+
+---------------------+                               |
                                                       |
                                                  +----v-----+
                                                  | BQ25570  |
                                                  | MPPT IC  |
                                                  +----------+
                                                       |
                                                  [Supercap Bank]
                                                       |
                                               Regulated Output Stages
                                             (USB-A, USB-C, Raw DC, etc.)
```

---

## 🧠 Integration Logic

- Each input is **modular** and **independently protected**
- All inputs share a **single convergence rail (Node A)**
- BQ25570 handles:
  - Cold start (≥330mV)
  - MPPT tracking
  - Energy transfer to supercaps

---

## 🛡️ Key Protection Notes

| Input Source | Rectifier Type | Clamp Type | Diode Type |
|--------------|----------------|------------|------------|
| Kinetic      | Full bridge    | None       | Schottky   |
| Piezo/Tribo  | Full bridge    | TVS        | Schottky   |
| RF           | HSMS-2850      | None       | Native     |
| TEG          | Native DC      | Schottky   | Optional   |

---

## 🔌 Node A Specs

- **Voltage range:** 0V – 5.5V (input to MPPT)
- **Capacitance:** ~100µF local smoothing + 0.1µF ceramic
- **Current handling:** Up to 300mA pulse tolerated
- **Wiring:** 22–28 AWG OK, twisted pair preferred for noise-prone sources

---

## ✅ Summary

- Node A serves as **the hub** of IX-ZeroCell's harvesting front end  
- All input types are preconditioned for safe, efficient energy transfer  
- Supports modular debugging and expansion (e.g. add new harvesters later)


# IX-ZeroCell Power Tree Schematic (Logical Flow)

This document provides a schematic-level overview of how power flows through the system, including routing from multiple energy harvesting modules to storage and regulated outputs.

---

## 🔋 Primary Inputs

1. **Kinetic Induction Array**
   - Output: AC voltage from 99-stage coil array
   - Rectified via full bridge (Schottky or ultra-fast diodes)
   - Fed into MPPT charging controller

2. **RF Ambient Harvester**
   - Output: DC from wideband rectenna
   - Bypasses coil circuit, connects directly to MPPT controller

3. **TEGs / Tribo / Piezo Modules**
   - Output: Pulsed or continuous DC depending on motion/temperature
   - All routed through diode-isolated summing bus into MPPT

---

## 🔁 Stage 1: Power Conditioning

- All inputs are passed through **ESD protection** (TVS diodes)
- Then into a **diode-mixed bus** tied to:
  - **Input Capacitor Bank (1000µF, low ESR)**
  - **Input to MPPT Boost Converter**

---

## ⚙️ Stage 2: MPPT Charging & Routing

- IC: **BQ25570** (Texas Instruments)
- Key Functions:
  - Tracks optimal input voltage/current for harvesting
  - Charges supercapacitor bank via programmable profile
  - Handles undervoltage lockout, hysteresis thresholds

### MPPT Parameters
- VIN Range: 80mV – 5V
- VOUT Programmable: 1.8V to 5.5V
- Cold-start: 330mV

---

## 🔋 Stage 3: Storage

- **3x Supercapacitors** in series-parallel
  - Nominal bank voltage: ~8.1V
  - Total capacity: 1000F effective
- Includes:
  - 100Ω balancing resistors
  - Passive bleed resistors for safe discharge
  - Optional Zener or TVS overvoltage protection

---

## 🔄 Stage 4: Boost and Regulation

- Boost output from BQ25570:
  - Stepped to **5V regulated rail**
  - Supports 10W peak bursts (via supercap discharge)
- Output filtered with 220µF + 0.1µF ceramic caps for noise reduction

---

## 🔌 Stage 5: Outputs

| Port         | Voltage | Current | Notes                       |
|--------------|---------|---------|-----------------------------|
| USB-A        | 5V      | ~1.5A   | Standard regulated output   |
| USB-C PD     | 5V–9V   | ~2.5A   | Optional, with PD handshake |
| Raw Terminal | 8.1V    | Up to 3A | Direct from supercap bank   |

---

## 🔁 Isolation & Safety

- Output rails have **reverse current blocking**
- Fused at 2.5A polyfuse per output
- Ground isolation maintained between harvester inputs and load outputs

---

## 🔧 Optional Expansions

- Solar PV input (via dedicated MPPT pin)
- Wireless Qi coil (not included in alpha version)
- Charge indicator LEDs (via comparator or digital pin on MCU)

---

## 📉 Flow Diagram

```plaintext
[Energy Inputs]
 ├── 99 Coil Induction (AC) ──> [Rectifier]
 ├── RF Harvester (DC) ───────┐
 ├── TEGs / Piezo / Tribo ────┘
       ↓
   [Input Bus] ─> [MPPT IC] ─> [Supercap Bank]
                                      ↓
                          [Boost Converter → Output Rail]
                                      ↓
            ┌───────────────┬──────────────┬─────────────┐
            ↓               ↓              ↓
         [USB-A]        [USB-C PD]     [Raw DC Terminal]
```

---

## 📦 Component Placement Notes

- Keep MPPT and supercap bank as close as possible
- Separate RF front-end physically from boost converter to avoid EMI coupling
- Use thick traces or bus bars for supercap output path

---

*Designed and documented by Bryce Wooster — IX-ZeroCell, 2025.*


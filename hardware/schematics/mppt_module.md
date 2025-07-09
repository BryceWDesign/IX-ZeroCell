# MPPT Module – BQ25570 Wiring and Configuration

This document outlines the detailed schematic and component layout of the **MPPT (Maximum Power Point Tracking)** module used in IX-ZeroCell, based on the Texas Instruments **BQ25570** energy harvesting IC.

---

## 🔧 Component Overview

| Component | Value / Part #         | Function                            |
|-----------|------------------------|-------------------------------------|
| U1        | BQ25570                | MPPT + Boost + LDO                  |
| R1/R2     | 4.7MΩ / 1.0MΩ          | Sets VBAT_OV and VBAT_OK thresholds |
| R3/R4     | 3.3MΩ / 1.0MΩ          | MPPT set-point voltage divider      |
| R5        | 10kΩ                   | LDO enable pull-up                  |
| C1        | 10µF Ceramic (X7R)     | VIN capacitor                       |
| C2        | 22µF Ceramic (X7R)     | VSTOR capacitor                     |
| C3        | 0.1µF                  | Reference stability cap             |
| L1        | 22µH, 1.5A Inductor    | Boost converter inductor            |
| D1        | Schottky Diode (SS14)  | Output rectifier                    |
| TVS1      | 5.5V TVS Diode         | VSTOR overvoltage protection        |

---

## 🧠 Key Functional Pins

| Pin      | Function                            | Wiring Notes                                |
|----------|-------------------------------------|---------------------------------------------|
| VIN_DC   | Primary input from harvester        | Connect to rectified kinetic + RF bus       |
| GND      | System ground                       | Common ground plane                         |
| VBAT     | To supercapacitor bank              | Includes bleed/balance resistors            |
| VSTOR    | Regulated output to boost converter | Also monitored for undervoltage cutoff      |
| VOUT_EN  | Output enable                       | Tied high through 10k pull-up               |
| LBOOST   | Boost converter control             | To inductor L1 and diode D1                 |
| VOC_SAMP | MPPT sampling input                 | Connected through R3/R4 to VIN_DC           |
| LDO      | Optional 1.8V LDO output            | Can be ignored if unused                    |

---

## ⚙️ Voltage Threshold Configuration

- **VBAT_OV (Overvoltage cutoff):**  
  Set by: `V = 1.2V × (1 + R1/R2)`  
  Using 4.7MΩ / 1MΩ → VBAT_OV ≈ 6.84V

- **MPPT Set Point (VOC_SAMP):**  
  Typically set to **80%** of open-circuit voltage  
  Divider: R3 = 3.3MΩ, R4 = 1.0MΩ → VOC_SAMP ≈ 0.75 × V_OC

---

## 📐 Schematic Block (Text Representation)

```plaintext
         +-------------------------+
    IN → | VIN_DC           VSTOR | → Boost Converter IN+
         |    |                |   |
         |   R3               C2  |
         |    |                |  |
         |   R4               GND |
         +-------------------------+
             |               |
             ↓               ↓
         VOC_SAMP         Supercap Bank
```

---

## 🛠️ Assembly Tips

- Use a 2-layer PCB with short traces between VIN_DC, inductor, and VBAT
- Isolate RF harvesting front-end from MPPT circuit using grounded copper pour
- Use ceramic capacitors with low ESR for stability
- For through-hole test builds, add pin headers for VSTOR, VBAT, GND, VIN_DC

---

## 🔍 Verification

1. Power up with simulated input (DC bench power supply, ~3V)
2. Observe VSTOR rising slowly — confirm VBAT begins charging
3. Use oscilloscope to verify MPPT pulsing behavior on LBOOST pin
4. Monitor supercap voltage until it reaches VBAT_OV (≈6.8V)

---

IX-ZeroCell, 2025.*


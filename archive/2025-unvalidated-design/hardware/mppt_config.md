> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – MPPT Configuration & Tuning Guide

**Author:** Bryce Wooster
**License:** Apache-2.0
**Component:** Texas Instruments BQ25570
**Purpose:** Guide for setting MPPT behavior, cold-start thresholds, and voltage regulation tuning

---

## 📦 MPPT Chip Overview

- **Part:** BQ25570 (TI)
- **Function:** Ultra-low-voltage boost converter with MPPT, cold-start, supercap charging, and regulated 3.3V LDO output
- **Typical Startup:** 330 mV cold-start; 100 mV post-startup operation
- **Ideal For:** Piezo, TEG, solar, kinetic AC → DC harvesting

---

## 🔩 Key Configuration Pins

| Pin     | Function                     |
|---------|------------------------------|
| VIN_DC  | Energy input (post diode)    |
| VSTOR   | Output to supercaps          |
| VBAT_OK | Signals minimum voltage met  |
| VOUT    | Regulated 3.3V for logic     |
| VOC_SAMP| Sets MPPT sample ratio       |
| V_OK_PROG | Sets OK voltage threshold  |

---

## 🔧 MPPT Ratio Resistor Divider (VOC_SAMP)

Sets **how much of open-circuit voltage** (VOC) is tracked as the MPPT setpoint.

### Target MPPT: ~75% of VOC
- Choose **R1 + R2 = 10MΩ to 20MΩ total** (higher = less current drain)
- Example:
  - `R1 = 8.25MΩ`
  - `R2 = 2.75MΩ`
  - MPPT ratio = R2 / (R1 + R2) ≈ 25%
  - Device then tracks 75% VOC

**Recommendation:**
```txt
R1 = 8.2MΩ (top)
R2 = 2.7MΩ (bottom)
→ Gives MPPT = 75.0% VOC (ideal for kinetic + RF + solar)
```

> Use precision 1% resistors if possible

---

## 🧊 Cold Start Threshold (VBAT_OK and V_OK_PROG)

Sets when the system is considered "alive" for logic circuits and downstream switching.

### Desired Supercap "ready" voltage: 5.0V

Use a divider from VSTOR → GND, tap to V_OK_PROG:

```txt
R3 = 4.7MΩ
R4 = 1.3MΩ
→ Trip point ≈ 5.0V
```

Once VSTOR > 5.0V, `VBAT_OK` goes HIGH → MCU can begin normal ops

---

## 🧠 LDO Notes (VOUT Pin)

- Outputs 3.3V, 50mA max
- Only use for **MCU**, not for powering output ports
- MCU may go to sleep or use watchdog to save power

---

## 📐 Board Layout Tips

- Keep resistor divider paths short
- Use 0402 or 0603 SMT resistors
- Place MPPT as close to input bulk cap as possible
- Decouple with ceramic caps (1µF, 10µF, 100nF)

---

## 🛒 Sourcing Notes

- **MPPT IC**: BQ25570RGTT (LQFN-20, 4mm x 4mm)
- **Recommended Breakout Board:** SparkFun BQ25570 Evaluation Board (DEV-15041)
- **Resistors**: Vishay or Yageo 1% SMD 0603
- **Startup Cap**: 10µF X7R ceramic on VIN_DC to stabilize cold-start

---

## ✅ Summary

- MPPT Ratio: 75% VOC
- Cold Start Trigger: ~5.0V
- All passive values chosen for ultra-low-leakage standby
- Divider resistors >1MΩ to minimize idle draw

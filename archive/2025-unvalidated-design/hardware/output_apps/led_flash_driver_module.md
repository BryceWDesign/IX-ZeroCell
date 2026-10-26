> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – LED Flash Driver Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Provide a brief flash of high-brightness LED using cap bank energy, optionally triggered by motion or logic control

---

## 💡 Overview

This module provides an **ultra-bright LED flash** — a short pulse triggered by either:

- Motion detection
- Time interval
- Manual input (test button)

This validates energy harvest, adds visibility, and optionally signals a charge-ready state.

---

## ⚙️ Design Diagram

```txt
[Cap Bank] → [Gate Switch] → [LED Series Array] → [GND]
                     ↓
                 [Trigger Input]
                 (motion, timer, GPIO)
```

---

## 🧱 Components

| Component         | Specs / Notes                                |
|--------------------|----------------------------------------------|
| Supercap Bank      | 5.5V, 15–25F
| High-Power LED     | 1W–3W (e.g. Cree XPE or Luxeon)
| Current Limiting R | ~4–10Ω (based on LED Vf & current target)
| N-Channel MOSFET   | IRLZ44N / IRFZ44N or similar
| Trigger Input      | Manual button, motion sensor, or MCU GPIO
| Bleed Resistor     | 1kΩ across cap to safely drain after flash
| Flyback Diode      | (optional) for inductive pulse suppression

---

## 🔌 Wiring Notes

1. Cap is pre-charged by IX-ZeroCell’s ambient harvesters
2. Trigger signal activates gate on MOSFET
3. Cap dumps into LED array with limited current
4. LED flashes briefly (~100ms–1s depending on cap voltage & R)

**Optional Enhancements:**

| Feature           | Benefit                             |
|---------------------|--------------------------------------|
| PWM Pulse Control | Flash duration control
| Multi-LED Array    | Multi-direction flash
| RGB LED            | Flash with color indication
| Recharge Lockout   | No retrigger until cap is recharged
| Motion + Flash     | Flash only when movement is detected

---

## ⚡ Current Example

**Assumptions:**

- 5.5V cap, 10Ω resistor, 3.2V LED Vf
- Current: (5.5V - 3.2V) / 10Ω ≈ 0.23A
- Power: ~0.74W
- Visible flash duration: 0.2–0.8s typical

---

## 🔋 Power Budget

| Source Cap Bank | LED Flash Time | Notes                      |
|------------------|----------------|----------------------------|
| 5.5V 15F         | ~2–3 seconds total (1 flash per second x3)
| 5.5V 25F         | ~5–7 seconds total
| Recharge Time    | Depends on harvester strength

---

## 📏 Physical Layout Tips

- Mount LED on aluminum heatsink pad
- Use thick wire for cap output to minimize drop
- Shield MOSFET gate line from noise (add 1kΩ resistor)
- Add small 10uF bypass cap across LED to prevent flicker

---

## ✅ Summary

- Converts stored ambient energy into visible LED flash
- Can signal motion, charge readiness, or user input
- Entirely passive-safe — no constant power required
- Works with off-the-shelf parts and IX-ZeroCell’s existing power structure

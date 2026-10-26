> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Audio Pulse Beeper Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Emit a short audio chirp using stored energy when a triggering condition occurs (e.g. cap charge complete, motion detected, manual test)

---

## 🔊 Overview

This module produces a **brief beep or pulse tone** to indicate system action — e.g.:

- **Capacitor full**
- **Motion detected**
- **Manual test initiated**

It uses a **low-power piezo buzzer** or magnetic beeper driven by a pulse from the IX-ZeroCell cap bank, gated via MOSFET or directly via GPIO if using an MCU.

---

## 🧱 Components

| Component        | Specs / Notes                             |
|-------------------|-------------------------------------------|
| Piezo Buzzer      | 3–5V passive piezo or magnetic transducer
| N-Channel MOSFET  | IRLZ44N, IRF520 or any logic-level type
| Trigger Input     | Manual button, PIR, timer circuit, etc.
| Optional Cap      | 220uF cap parallel to piezo for smoothing
| Pull-down Resistor| 10kΩ on gate to avoid floating
| Series Resistor   | 100Ω to limit max drive current
| Optional MCU Pin  | Pulse via GPIO for clean timed chirp

---

## ⚡ Circuit Flow

```txt
[Cap Bank +] —+
             |
         [MOSFET]
             |
        [Piezo Buzzer +]
             |
          [GND]
```

- Trigger line activates gate
- Cap discharges just enough to emit a short audio pulse
- Resistors smooth and prevent damage from overdrive

---

## 🔈 Audio Profile

- **Tone:** Depends on piezo resonance (usually 2–4kHz)
- **Volume:** 70–85 dB @ 3–5V
- **Pulse Duration:** 100–500ms typical
- **Cap Drain:** Negligible (~1–5mC per pulse)

---

## 🎛️ Triggering Options

| Trigger Type      | Application                         |
|---------------------|--------------------------------------|
| PIR Sensor         | Motion-activated beep
| Cap Voltage Check  | Beep when charge is ready
| Manual Button      | User-initiated test
| MCU Pulse (GPIO)   | Timed chirp, precise length
| Reed Switch        | Magnetic open/close feedback

---

## 🛠️ Physical Assembly Tips

- Mount piezo directly to board or case panel
- Add foam behind to boost directional audio
- Isolate MOSFET gate from long wire runs — add gate resistor
- If using MCU, PWM may allow tonal control

---

## 💬 Usage Scenarios

| Use Case             | Description                          |
|------------------------|--------------------------------------|
| Charge Complete       | Audible confirmation
| Motion Alert          | Beep when ambient movement detected
| Power Ready Indicator | Optional sound before LED flash or motor kick
| Error Tone            | Multi-chirp for fault feedback

---

## ✅ Summary

- Adds **non-visual output** for status or trigger confirmation
- Requires very little power
- Easily triggered from existing logic lines
- Compatible with any cap bank >3V
- Simple, no-microcontroller version supported

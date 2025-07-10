# IX-ZeroCell – USB 5V Boost Output Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Convert variable capacitor bank voltage (typically 2.2V–5.5V) to a regulated 5V USB output. Powers USB-based electronics directly from IX-ZeroCell.

---

## 🔋 Overview

This module boosts the capacitor output to a **stable 5V DC** level via a high-efficiency switching regulator (step-up).

### Use Cases:
- Powering a microcontroller from the cap  
- USB accessories (fans, lights, meters)  
- Charging small 5V devices  
- Driving sensors, logic gates, etc.

---

## 🧱 Components

| Component                | Recommended Part          | Notes                           |
|--------------------------|----------------------------|----------------------------------|
| Boost Converter Module   | MT3608 / TPS61022 / PAM2401 | Input: 2V+, Output: 5V regulated  
| Capacitor                | 470µF+ (output side)       | Stabilizes USB line  
| USB-A Female Port        | Any breakout or salvaged   | 2-pin power only  
| Diode (optional)         | Schottky 1N5819             | Protects against reverse flow  
| Wires / Solder pads      | For modular plug-in        | Dupont headers OK  

---

## 🔌 Wiring Diagram

```txt
[Cap Bank +] --> [Boost IN+]  
[Cap Bank -] --> [Boost IN-]  
[Boost OUT+] --> [USB VBUS (+5V)]  
[Boost OUT-] --> [USB GND]
```

You can add a toggle switch or enable pin to cut USB line if cap voltage dips below 2.0V.

---

## 🧠 Performance Notes

- MT3608 starts boosting at **~2V** and performs well up to **5.5V**  
- Output current is typically **500–800mA** max  
- If using a logic circuit downstream, consider adding a **voltage supervisor** to avoid brownouts

---

## 🧪 Test Case

| Input Voltage | USB Output | Load Status     |
|---------------|------------|-----------------|
| 5.5V          | 5.01V      | Stable 500mA  
| 3.3V          | 5.03V      | Stable 250mA  
| 2.2V          | 4.75V      | Weak, unstable  
| 1.8V          | Fail       | Below boost threshold  

---

## ⚠️ Design Tips

- Add **output cap** close to USB port to suppress ripple  
- Use **shielded inductors** if building your own converter  
- Avoid powering motors or inductive USB loads directly  
- Include a **low-voltage cutoff** circuit if needed  
- Optional: add **LED indicator** for USB on/off status

---

## 🔋 Expansion Options

- Add a **DC barrel jack** for alternate 5V output  
- Integrate with LED cluster to show USB status  
- Combine with audio or haptic module for active “power on” cue  
- Use soft enable (transistor gate) for energy gating

---

## ✅ Summary

- Converts IX-ZeroCell energy to usable **5V USB**  
- Efficient, compact, and compatible with almost all mobile electronics  
- Adds massive real-world utility — logic, sensors, portable hardware


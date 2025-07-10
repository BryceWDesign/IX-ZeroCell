# IX-ZeroCell – LED Indicator Cluster

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Display charge percentage of IX-ZeroCell capacitor bank using an LED cluster (bar graph, single lights, or RGB scale).

---

## 💡 Overview

This module creates a **voltage-based visual feedback system** using multiple LEDs — mapped to the cap bank’s current voltage.

Use cases:
- Quick visual charge check  
- Power-on UX  
- Field diagnostics without tools  
- Human-readable % capacity  
- Visual feedback for charging/discharge rate

---

## 🔋 Design Options

### Option A: **Voltage Divider + Analog Comparators**
- Each LED triggers based on voltage threshold  
- Uses op-amps or LM3914 driver IC  
- Passive-friendly, low-power

### Option B: **MCU-Driven via ADC**
- Read cap voltage via analog pin  
- Software decides which LEDs to light  
- Highly customizable, programmable  

---

## 🧱 Component List

| Component            | Spec / Notes                           |
|------------------------|-----------------------------------------|
| LEDs x5–10             | Any color, or use RGB for spectrum  
| Resistors              | 330Ω – 1kΩ for current limiting  
| LM3914 or similar      | LED driver IC (bar/dot modes)  
| Optional: MCU (ESP32) | If you want digital ADC control  
| Wires / Dupont Cables  | Modular connection to cap read pin  

---

## 🔌 LED Mapping Example

| Cap Voltage | % Full | LED #
|-------------|--------|--------|
| 5.5V        | 100%   | All on  
| 4.8V        | ~85%   | 8/10  
| 4.0V        | ~70%   | 6/10  
| 3.3V        | ~55%   | 4/10  
| 2.7V        | ~40%   | 3/10  
| 2.2V        | ~25%   | 2/10  
| 1.8V        | ~10%   | 1/10  

(Values adjustable via resistor thresholds or software)

---

## ⚙️ Schematic Overview

### **Hardware-Only LM3914 Method:**

```txt
[Cap Bank] --> [Voltage Divider] --> [LM3914] --> [LED1–LED10]
```

- Divider brings voltage to 0–1.25V scale  
- LM3914 turns on LEDs based on matched VREF ladder  
- Simple and elegant

---

### **MCU Software Method:**

```c
// Arduino pseudo-code
float volts = analogRead(A0) * (5.0 / 1023.0);

if (volts > 5.0) { lightAll(); }
else if (volts > 4.0) { light(8); }
else if (volts > 3.0) { light(6); }
// etc.
```

You can animate the display, add warning flash, or mix with sound modules.

---

## 🎨 Aesthetic / UX Notes

- Use **RGB LEDs** to show red/yellow/green zones  
- Flash last LED if nearing empty (≤ 2.2V)  
- You can wire to a wearable or transparent housing  
- A curved LED arc adds visual elegance  

---

## ⚠️ Build Tips

- Use **constant current limiting resistors** for each LED  
- Place LEDs in a row, arc, or circle depending on enclosure  
- Avoid overdriving the LEDs — they should draw <5mA each  
- Can combine this with the Audio Pulse Module for hybrid alerts

---

## ✅ Summary

- Visually indicates charge level of IX-ZeroCell  
- Works via hardware (comparators) or MCU logic  
- Simple, modular, and user-facing  
- Great for diagnostics, style, or real-time usage feedback


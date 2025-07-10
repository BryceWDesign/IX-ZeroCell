# IX-ZeroCell – Supercapacitor Digital Monitor Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Add optional real-time voltage display for capacitor charge monitoring

---

## 🔋 Overview

This module shows the **current voltage** of the supercapacitor bank, giving:

- At-a-glance charge level  
- Confidence before deploying USB/BLE loads  
- Debug info for energy harvesting performance

---

## 🧠 Options

### 1. **3-Wire Digital Voltmeter (no MCU)**
- Low-cost modules (0.28” or 0.36” displays)  
- Read directly from cap rail  
- Self-powered from input voltage (min 2.5V start)  
- Draws ~4–10mA while active

### 2. **MCU + OLED Display**
- ATtiny85 or STM8L with SSD1306 (0.96” OLED)  
- Draws 1–5mA depending on logic  
- More customizable (percent display, warnings, etc.)

---

## ⚡ Wiring – Simple Voltmeter Module

```txt
[ Supercap Bank ]
     ↓
[ Resistor Divider ]
     ↓
[ Digital Voltmeter V+ ]
     ↓
[ GND to GND ]
```

Use a voltage divider if your voltmeter maxes out <10V. Most are good to 30V.

---

## 🧱 Component List

| Component            | Notes                               |
|----------------------|--------------------------------------|
| Digital Voltmeter    | 3-wire (red=VCC, black=GND, white=IN)  
| OLED Display (opt.)  | SSD1306 I2C, 128x64                  |
| Microcontroller (opt)| ATtiny85, STM8L, or ESP8266 (deep sleep)  
| Pull-down Resistor   | 100kΩ (for divider, if needed)       |
| Divider Resistor     | 10kΩ top / 10kΩ bottom (for 2:1 scale)  
| SPST Switch          | Optional: toggle display on/off      |

---

## 📐 Mounting Suggestions

- Attach display near cap bank with header pins  
- Use switch or momentary button to prevent constant draw  
- 3D printed bezel optional for field use  

---

## 📉 Power Consumption

| Display Type     | Active Draw   | Notes                          |
|------------------|----------------|--------------------------------|
| LED Voltmeter    | 4–10mA         | Can affect small caps if left on  
| OLED I2C         | 2–5mA (typ.)   | Depends on brightness, update rate  
| MCU Sleep Mode   | <1µA           | Only active on motion/button  

---

## 🔋 Example Readout Ranges

| Voltage Range     | Meaning                          |
|-------------------|----------------------------------|
| 0.0–1.5V          | Very low, harvest more energy     |
| 1.5–2.5V          | Minimal load possible             |
| 2.5–4.0V          | BLE broadcast, light loads OK     |
| 4.0–5.5V          | Full system use (USB, LED) OK     |

---

## ✅ Summary

- Adds essential UX feedback to energy state  
- Simple voltmeter or MCU+OLED options available  
- Low draw, battery-free operation  
- Ideal for debugging, field deployment, and charge planning  


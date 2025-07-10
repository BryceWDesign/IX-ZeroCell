# IX-ZeroCell – USB Low-Power Boost Converter Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Convert low-voltage ambient energy (from supercaps or coils) into temporary USB-level 5V output for ultra-low power devices.

---

## ⚡ Overview

This module steps up the harvested voltage (typically 0.9V–3.3V) to **5V USB power** using a dedicated low-quiescent boost converter.

Intended for:
- BLE modules (e.g., Nordic nRF52)
- ESP32-C3 microcontrollers  
- Charging small supercaps or LTO-based cells  
- USB "data sniffers" or intermittent signal processing devices

---

## 🔋 Component Requirements

| Component                 | Recommended Part                  | Notes                        |
|----------------------------|------------------------------------|------------------------------|
| Boost Converter IC         | MCP1640, LT1302, or TPS61070       | Low startup voltage  
| Input Capacitor            | 22uF ceramic (X5R/X7R)             | Prevent brownout  
| Output Capacitor           | 100uF low ESR                      | Smooth 5V output  
| Inductor                   | 4.7uH–10uH shielded, low DCR       | Based on IC datasheet  
| Schottky Diode (if needed) | SS14 or BAT54                     | Some ICs require external diode  
| USB Breakout Board         | USB-A or USB-C (female port)       | Connects to output  
| Pull-down Resistor         | 100kΩ to ground on EN pin          | Keeps converter off by default  
| Enable Trigger (optional)  | Logic or manual switch             | Cap-aware logic control  

---

## 🧰 Circuit Description

```txt
[Supercap Bank] --> [Boost Converter IC] --> [5V Rail] --> [USB Breakout Port]
                                 |
                             [EN pin] <-- manual or logic trigger
```

- When enough voltage is stored in the supercap bank, a trigger enables the boost IC  
- Output voltage stabilizes at 5V  
- USB port becomes active — only as long as the cap can sustain it

---

## 🔋 Power Output Profile

| Input Voltage | Output Voltage | Max Current | Runtime (typical) |
|----------------|------------------|---------------|---------------------|
| 0.9V–1.8V      | 5V                | ~30–100mA     | ~10–60 sec  
| 2.4V–3.3V      | 5V                | ~100–250mA    | ~15–120 sec  
| 4.0V+ (direct) | 5V                | ~500mA+ (burst)| ~5–20 sec  

*Runtime varies by cap size (e.g., 10F vs. 50F), draw load, and duty cycle.

---

## 🔌 Supported Devices (Examples)

| Device Type         | Notes                              |
|----------------------|------------------------------------|
| ESP32-C3 Dev Board  | Bootable, low-power tasks only  
| BLE Beacon (nRF52)  | Fully compatible  
| USB Data Logger     | Short active session  
| Charge LTO Cell     | Can top up up to ~2.5V  
| USB Fan / LED Strip | Not supported (too high draw)  

---

## ⚠️ Limitations

- **Not designed for USB charging of phones or tablets**  
- Peak draw must be managed to avoid converter brownout  
- Use an **enable switch or logic pin** to control when boost activates  
- Cap bank must be fully charged before triggering or converter will oscillate/fail

---

## 🛠️ Build Tips

- Keep **input/output traces short and wide**  
- Use **ceramic capacitors with low ESR** for stability  
- Mount converter IC away from noisy sources (e.g., vibration motors)  
- Heatsink pad of boost IC to ground plane if available

---

## ✅ Summary

- Enables **USB 5V output from cap-harvested energy**
- Great for low-duty-cycle embedded work  
- Can power microcontrollers without batteries  
- Works with existing IX-ZeroCell logic control  
- Adds major compatibility boost to external systems


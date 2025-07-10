# IX-ZeroCell – MCU Interface Logic

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define an optional microcontroller (MCU) logic block to monitor voltage, protect supercaps, and control output behavior of IX-ZeroCell system

---

## 🎛️ Optional MCU Role

A connected MCU can:
- Monitor **supercap voltage**
- Trigger **low-voltage cutoff**
- Perform **load throttling**
- Log data to serial / flash / BLE
- Communicate status via LED / display

---

## 📌 Recommended MCU Types

| MCU          | Voltage | Sleep µA | ADC | GPIOs Needed |
|--------------|---------|----------|-----|--------------|
| ATtiny85     | 3.3V    | ~0.5 µA  | Yes | 2–3  
| ESP32        | 3.3V    | ~10 µA   | Yes | 4+  
| STM32L0      | 3.3V    | ~0.3 µA  | Yes | 3+  
| SAMD21       | 3.3V    | ~1 µA    | Yes | 3+  

> If using 5V boost, ensure logic level shifters or divider resistors where needed.

---

## ⚡ Voltage Monitoring

### Basic Voltage Divider

```txt
[Supercap+] — R1 —┬—> A0 (MCU ADC)
                  |
                 R2
                  |
                GND
```

- R1: 1MΩ  
- R2: 330kΩ  
- ADC max = ~1.2V at full cap (5.4V input)

### Code Example (ESP32, Arduino-style)

```cpp
float vRaw = analogRead(A0);
float voltage = (vRaw / 4095.0) * 3.3 * ((1.0 + (1000000.0 / 330000.0)));
if (voltage < 2.8) {
  digitalWrite(RELAY_PIN, LOW);  // kill output
}
```

---

## 🔌 Output Control Options

- **MOSFET switch**: MCU toggles gate to enable/disable output  
- **Relay**: Less efficient, but safe for 5V control  
- **GPIO + LED**: Show power state, voltage level, or alerts  
- **PWM**: Dynamically reduce brightness on display / LED strip

---

## 🧠 Load Shedding Strategy

- Measure cap voltage every 5–10s  
- Below 3.0V → warn  
- Below 2.8V → disable USB/JST ports  
- Restore above 3.2V  
- Optional: broadcast BLE signal (LoRa or BLE status frame)

---

## 📶 UART Debug (Optional)

- TX → USB-to-serial for logs  
- Add serial monitor output for:
  - Cap voltage
  - Load current (if sense resistor used)
  - Event flags (brownout, resume, peak alert)

---

## 📐 Pin Use Suggestions

| Function             | MCU Pin      |
|----------------------|--------------|
| ADC from cap         | A0 / GPIO36  |
| Output enable (MOSFET)| GPIO12       |
| LED status           | GPIO14       |
| Debug TX             | GPIO1        |

---

## ✅ Summary

- MCU adds “smart” layer to protect against brownout  
- Easily implemented with low-cost chips (ATtiny or ESP32)  
- Enables safe shutdown, cap monitoring, and load control  
- Code remains simple and low-power  
- Optional — not required for base IX-ZeroCell operation


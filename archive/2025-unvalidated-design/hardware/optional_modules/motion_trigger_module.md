> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Motion Detection Trigger Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Optional module to detect motion or tilt, triggering other modules in IX-ZeroCell

---

## 🧭 Overview

This module lets IX-ZeroCell respond only when **motion is detected**, conserving energy.

Use cases:

- Wake up BLE beacon on movement
- Power USB only when device is tilted or handled
- Light activation only when presence is sensed
- Trigger data loggers, sensors, alarms, etc.

---

## 🚨 Sensor Options

### 1. **MEMS Accelerometer (Digital)**
| Part        | Notes                                   |
|-------------|-----------------------------------------|
| ADXL345     | 3-axis, I2C/SPI, 26µA active, 0.1µA standby
| LIS3DH      | Ultra-low power, tap/tilt/double-tap    |
| MMA8452Q    | 14-bit, configurable wake interrupt     |

### 2. **Mechanical Tilt Switch (Analog)**
| Part         | Notes                                   |
|--------------|-----------------------------------------|
| SW-200D      | No power draw, simple angle switch      |
| Mercury Tilt | Deprecated due to RoHS — avoid use      |

---

## 🔌 Electrical Interface

### Digital Accelerometer Wiring

```txt
[ Boosted 3.3V ] ─→ VCC (sensor)
[ GND ]         ─→ GND
[ SDA/SCL ]     ─→ I2C to MCU (optional)
[ INT1 ]        ─→ Interrupt pin → logic switch
```

### Analog Tilt Switch

```txt
[ 5V ] ─→ Pull-up → Tilt switch → GND
                     ↓
                 Digital input to logic controller
```

---

## 🧠 Logic Triggering Methods

- Use INT pin from accelerometer to **trigger a MOSFET** gate
- Use tilt switch to pull low an **enable pin** on downstream modules
- Add debounce (~10ms) with RC network or microcontroller logic

---

## 📐 Components List

| Component             | Notes                                 |
|-----------------------|----------------------------------------|
| Accelerometer (opt.)  | ADXL345, LIS3DH, MMA8452Q              |
| Tilt Switch (alt.)    | SW-200D or ball switch                 |
| Pull-up Resistor      | 10kΩ for analog input use              |
| Debounce Capacitor    | 0.1µF for analog switch                |
| N-channel MOSFET      | IRLML6344 or similar for switching     |
| Indicator LED         | Optional: shows trigger state         |
| Microcontroller (opt.)| ATtiny85, STM8L, etc. (for advanced logic) |

---

## 🧪 Performance Metrics

| Mode               | Power Use         | Response Time   |
|--------------------|-------------------|-----------------|
| Tilt Switch        | ~0µA (passive)    | Instant (<5ms)  |
| Accelerometer (sleep) | <1µA          | ~15ms wake      |
| Accelerometer (active)| 20–50µA        | Continuous read |

---

## ⚙️ Use Case Examples

| Application           | Sensor Type    | Trigger Action                    |
|------------------------|----------------|-----------------------------------|
| BLE beacon on motion   | ADXL345        | Wake MCU, transmit burst          |
| USB enable on tilt     | SW-200D        | Enable USB boost converter        |
| Light when moved       | LIS3DH         | PWM to LED module                 |
| Log data on bump       | MMA8452Q       | SPI trigger to EEPROM             |

---

## ✅ Summary

- Adds smart sensing to IX-ZeroCell — only power up when needed
- Saves energy in standby / idle periods
- Sensor-agnostic: supports both passive switches and digital MEMS
- Can control any downstream module (BLE, USB, LEDs, etc.)
- Fully optional, low-cost, easy to integrate

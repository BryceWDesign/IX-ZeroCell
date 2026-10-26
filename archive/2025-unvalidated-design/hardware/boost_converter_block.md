> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Boost Converter Block (Output Regulation)

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Define the voltage boost stage that converts supercapacitor voltage (1.8–5.4V) into regulated 5V or 3.3V outputs

---

## ⚡ Primary Component

### MT3608 Step-Up Converter

- Input Voltage: 2.0V – 24V
- Output Voltage: Adjustable (max 28V)
- Max Current: ~1.2A peak (600–800mA sustained)
- Efficiency: 80–90%
- Built-in thermal and overcurrent protection

---

## 🧩 Wiring Diagram (Typical)

```txt
[Supercap Array] — [L1 Inductor] — MT3608 VIN
                          |
                   [100µF + 1µF cap to GND]
                          |
                    MT3608 GND → System GND
                    MT3608 VOUT → USB Rail or DC Out
```

> Cap spacing: Electrolytic + Ceramic at input **and** output

---

## 🎯 Output Configurations

### 1. **Fixed 5V Output** (Most Common)

- Use 100kΩ + 33kΩ feedback resistor pair
- Output powers:
  - USB-A port
  - Sensors requiring 5V
  - Logic level shifting if needed

### 2. **Fixed 3.3V Output**

- Use 100kΩ + 50kΩ resistors
- Ideal for ESP32, STM32, BLE modules

---

## 🔐 Output Protections

- **Schottky diode (SS34)** after VOUT
  - Prevents external power pushback
- **100µF + 1µF output caps**
  - Stabilizes ripple under pulse loads
- **Polyfuse (optional)**
  - Trip at 800mA if needed for USB safety

---

## 🔌 USB-A / USB-C Integration

Use MT3608 output to feed USB via protection chain:

```txt
[MT3608 VOUT] — [Schottky Diode] — [USB Port VBUS]
                          |
                      [TVS Diode]
                          |
                    External Device
```

> Optional: Add LED + 1kΩ resistor between VOUT and GND for visual output status

---

## 📐 Placement + Heatsinking

- Place in airflow path if fan exists
- Copper pour around MT3608 IC helps dissipation
- Keep L1 inductor <10mm from IC
- Keep short traces between input caps and VIN pin

---

## 🧪 Load Testing Strategy

1. Charge caps to 5.4V
2. Attach 5V dummy load at 300mA
3. Watch for ripple or thermal throttling
4. Use scope or IR temp gun if available

---

## ✅ Summary

- MT3608 = efficient, compact boost converter for supercap-based systems
- Supports flexible 3.3V or 5V output
- Protects itself with thermal/current shutdown
- Use diode + caps to clean up and isolate output for USB or raw DC use

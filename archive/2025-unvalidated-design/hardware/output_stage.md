> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Output Stage (Regulated USB + DC Power)

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Define output routing, voltage regulation, and safe power limits from the supercap bank

---

## ⚡ Output Overview

The output stage of IX-ZeroCell pulls energy **after the supercapacitor bank**, regulates it to standard voltages, and distributes it through:

- USB-A (5V)
- Optional USB-C PD (if PD trigger is installed)
- Raw DC Terminal (variable voltage from supercaps)

---

## 🔋 Input Voltage Range

| Source      | Voltage Range |
|-------------|----------------|
| Supercap Bank | 3.0V – 8.1V   |

This feeds into a **5V step-up buck/boost regulator** (output constant even as supercap drains).

---

## 🔧 Voltage Regulation Modules

### Option 1 – Fixed 5V Step-Up Buck Converter

- **Chip:** MT3608 or TPS61200
- **Input Range:** 2V–9V
- **Output:** 5.0V regulated
- **Max Current:** ~1.2A peak, 600–800mA continuous
- **Output Ports:** USB-A jack + USB-C breakout (if desired)

**Wiring:**
```txt
Supercap V+ → IN+ (Regulator)
Supercap GND → IN-
Regulator OUT+ → USB VCC
Regulator GND → USB GND
```

---

### Option 2 – Programmable USB-C PD Trigger (Optional)

To get 9V / 12V via USB-C PD:
- Use PD Trigger Board with dip-switch or resistor config
- Sourced from SparkFun, Adafruit, AliExpress

**WARNING:** Only use if supercap voltage >9V and stable under load

---

### Option 3 – Raw DC Terminal Output

- Routed straight from Supercap V+ and GND
- Provides high-current raw DC for:
  - Sensor nodes
  - Wireless relays
  - Experimental subsystems

Label clearly: “⚠️ UNREGULATED DC”

---

## 📦 Suggested Components

| Use Case        | Module                        | Vendor             |
|------------------|-------------------------------|---------------------|
| 5V Regulated     | MT3608 Boost Regulator        | Adafruit, AliExpress |
| USB-C Trigger    | PD 12V/9V Board (Settable)    | SparkFun / eBay     |
| Terminal Output  | Screw Terminal Block 5.08mm   | Phoenix / WAGO      |

---

## 🔋 Output Budget Example (w/ MT3608)

| Load Device     | Voltage | Current | Notes             |
|------------------|---------|---------|--------------------|
| Arduino Nano     | 5V      | 20mA    | Powered by VOUT    |
| USB LED Light    | 5V      | 100mA   | Low brightness OK  |
| Sensor Node      | 3.3V    | 30mA    | Internal reg       |
| Total            | —       | 150mA   | Well within limits |

---

## 🧪 Testing and Protection

- Add 1000µF electrolytic cap on 5V rail to smooth surge
- Optionally add **Schottky diode** on USB VCC line to prevent backfeed
- Fuse: 1A polyfuse inline with USB power out
- Add LED indicator on 5V rail with 330Ω resistor (5V → LED → GND)

---

## ✅ Summary

- Power pulled post-cap from ~3.0V–8.1V
- Boosted to 5V stable for USB devices
- Optional PD or raw DC available for experimental loads
- Protect output with caps, diode, and fuse for safety
- Max realistic draw ~600–800mA continuous, depending on regulator used

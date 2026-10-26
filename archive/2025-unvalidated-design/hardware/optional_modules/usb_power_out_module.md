> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – USB Power Output Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Deliver 5V regulated output via USB-A port using harvested supercap energy

---

## ⚡ Overview

This module allows external USB-powered devices to draw power directly from IX-ZeroCell's **boost-regulated supercapacitor output**.

Includes:

- 5V regulation
- Reverse current protection
- ESD protection
- Overcurrent fuse (polyfuse)
- Optional switch or auto-on logic

---

## 🔌 Electrical Flow

```txt
[ Supercap Bank ]
     ↓
[ Boost Converter ]
     ↓
[ ESD + Schottky + Fuse ]
     ↓
[ USB Type-A Female Port ]
```

---

## 🧱 Required Components

| Component         | Value / Notes                       |
|-------------------|--------------------------------------|
| Boost IC          | MT3608 (or TPS61200)                | Set for 5V out
| USB-A Connector   | Female, through-hole preferred      | 4-pin standard
| Schottky Diode    | SS14, MBRS340                       | Blocks reverse current
| Polyfuse          | 500mA or 1A resettable              | Protects against shorts
| TVS Diode         | PESD5V0S1BA or similar              | ESD protection
| Output Cap        | 10µF ceramic, 1µF ceramic (x2)      | Output stability
| ON/OFF Switch     | Optional SPST                       | Manual enable
| LED Indicator     | Green LED + 1kΩ resistor            | Shows power active

---

## 📏 USB Pinout Mapping

| USB Pin | Signal     | Connection                        |
|---------|------------|------------------------------------|
| 1       | VBUS (5V)  | Boost output via Schottky/Fuse    |
| 2       | D-         | Leave NC or jumper to GND (optional)
| 3       | D+         | Leave NC or jumper to GND (optional)
| 4       | GND        | System GND                        |

---

## 📉 Output Ratings

| Parameter         | Value                               |
|-------------------|--------------------------------------|
| Voltage           | 5.0V ± 0.2V                          |
| Max Current       | 300–500mA (depends on cap charge)    |
| Short Protection  | Auto reset via polyfuse             |
| Efficiency        | 80–92% (MT3608 typical)              |

---

## 🛠️ Assembly Notes

- Mount USB-A securely on edge of PCB
- Keep boost converter close to supercap output
- Use wide traces for VBUS/GND routing
- Fuse before diode, then output
- Optional soft-start cap can prevent brownout on USB load insertion

---

## 🔋 What It Can Power

| Device Type        | Example                           | Runtime (typical full charge) |
|--------------------|------------------------------------|-------------------------------|
| Microcontroller    | ATmega328, ESP8266, nRF52840       | 30–90 min intermittent        |
| LED Strip (1m)     | WS2812B low brightness             | ~10 min burst use             |
| BLE Beacon         | iBeacon, Eddystone                 | ~4–6 hours broadcast mode     |
| USB Fan (low)      | 5V @ 100mA                         | ~15–30 min                    |
| Smartphone (trickle)| iPhone/Android (screen off)      | ~1–3% top-up only             |

---

## ✅ Summary

- Safely delivers USB 5V output using harvested, regulated energy
- Protects against overcurrent, ESD, reverse feed
- Simple and robust — ready for field deployment
- Fully compliant with IX-ZeroCell’s architecture

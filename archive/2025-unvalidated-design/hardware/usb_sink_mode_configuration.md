> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – USB-C Sink-Only Output Configuration

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Define how to wire USB-C in sink-only (power-out) mode with 5V output using passive CC pulldown resistors

---

## ⚠️ What This Is

IX-ZeroCell supports **powering** devices via USB-C.
We are NOT accepting power.
We are NOT negotiating USB PD (Power Delivery).
We just offer **5V at VBUS** like a wall wart.

---

## 🔌 USB-C Sink-Only (Type-C) Wiring

| USB-C Pin  | Purpose         | Connect to         |
|------------|------------------|---------------------|
| VBUS       | 5V Output        | Boost VOUT
| GND        | Ground           | System GND
| CC1        | Pull-down (5.1kΩ)| To GND
| CC2        | Pull-down (5.1kΩ)| To GND
| D+ / D−    | Leave floating   | Not used
| SBU1/2     | Leave floating   | Not used

> Pull-down resistors signal to the device that this is a passive 5V source
> No need for USB PD chip or controller

---

## 🧰 BOM

| Part            | Qty | Notes                               |
|------------------|-----|--------------------------------------|
| USB-C Connector  | 1   | Sink-only, 16P or 24P
| Resistor 5.1kΩ   | 2   | 1% or better, for CC1/CC2
| TVS Diode        | 1   | SMAJ6.5A or similar across VBUS
| 10µF Ceramic Cap | 1   | Bypass near VBUS pin

---

## 🧪 Output Protection (Recap)

- Add **TVS diode** from VBUS to GND
- Add **ferrite bead** between MT3608 and USB-C VBUS pin
- Polyfuse optional but recommended (e.g. MF-R050)

---

## 🧠 Notes

- Do **not** connect to a host PC while powered — it will confuse host port
- This config is for **powering** dev boards, not data
- Safe for most ESP32-C3, Feather, and Arduino-type boards

---

## 🛠️ PCB Layout Tips

- Keep CC1/CC2 resistors close to USB-C connector
- Trace VBUS from boost converter → ferrite bead → TVS → connector
- Add ground pour under connector
- Route GND pin with wide trace (1A+)
- Use mechanical support pins if present

---

## ✅ Summary

- Offers 5V output via USB-C safely and passively
- Standards-compliant sink-only config using 5.1kΩ pulldowns
- No PD controller needed
- Suitable for modern microcontroller boards, sensors, radios, etc.
- Protect with TVS + optional fuse

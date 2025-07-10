# IX-ZeroCell – Fuse and TVS Protection Layer

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Add low-profile, high-reliability protection against short circuits, surges, ESD, and reversed connections

---

## ⚠️ Why Protection Matters

Ambient energy is unpredictable.  
So are USB devices, humans, and breadboard experiments.

This protection stack prevents:

- Reverse polarity (user error)
- USB short circuits (crappy cables)
- Inductive spike injection (e.g. kinetic sources)
- ESD strikes from handling or field use

---

## 🔥 Fuses

Use **resettable polyfuses (PTC)** or **thin-film SMD fuses** on **all output rails**.

### Recommended:

| Port    | Fuse Type | Rating     | Notes                       |
|---------|-----------|------------|-----------------------------|
| USB-A   | PTC       | 500mA      | Limits downstream overload  
| USB-C   | PTC       | 500mA      | Sink-mode only  
| JST     | PTC       | 300–500mA  | Conservative current  
| VOUT rail | SMD     | 750mA–1A   | Before port breakout

> Use **Littelfuse RUE or Bourns MF-R** series  
> Use **1206 package** if space permits

---

## ⚡ TVS Diodes

Use **bidirectional TVS diodes** on all output lines and power rails.

### Example:

| Node         | TVS Part       | Clamp Voltage | Notes                         |
|--------------|----------------|----------------|-------------------------------|
| USB VBUS     | SMBJ5.0CA      | ~7V            | Prevents USB overvoltage  
| USB D+/D-    | PESD5V0S1UL    | 5V             | ESD on data lines  
| JST Output   | SMBJ5.0CA      | ~7V            | Catch inductive spikes  
| VIN (Boost)  | SMAJ6.5CA      | ~8V            | Handles startup surges  

---

## 🔄 Reverse Polarity Protection

Options:

### 1. Schottky Diode (Basic)
- Inline diode on VOUT  
- Drop = 0.3V–0.4V  
- Simple, cheap

### 2. P-MOSFET (Preferred)
- Source to VOUT rail  
- Gate to GND via resistor  
- Body diode blocks reversed current  
- **Lossless conduction when ON**

**Recommended Part:** IRF7410, SI2343, or equivalent

---

## 📦 BOM

| Component      | Value/Type      | Qty | Notes                          |
|----------------|------------------|-----|-------------------------------|
| Polyfuse        | 500mA PTC        | 3   | USB-A, USB-C, JST  
| TVS Diode       | SMBJ5.0CA        | 3   | One per power output  
| TVS (Data line) | PESD5V0S1UL      | 2   | USB data  
| P-MOSFET        | IRF7410 or equiv | 1   | Reverse polarity guard  
| Gate resistor   | 10kΩ             | 1   | Pull gate to GND

---

## 🛠️ Layout Guidelines

- Place TVS **as close to connector pins as possible**  
- Fuse sits **before** TVS on power path  
- P-MOSFET for polarity must sit directly on VOUT rail

---

## ✅ Summary

- TVS = ESD and voltage spike defense  
- PTC fuse = short circuit and overload protection  
- P-MOSFET = near-zero-loss polarity protection  
- Covers all ports: USB-A, USB-C, JST, internal power


> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – High-Gain Directional RF Rectenna Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Add-on directional antenna with rectifier for improved RF harvesting in IX-ZeroCell system

---

## 📡 Module Purpose

This module captures **ambient RF energy** more efficiently by using:

- Directional gain (up to 8–12dBi)
- Tuned antenna elements (2.4GHz or 915MHz)
- High-efficiency Schottky rectification

It connects to the IX-ZeroCell **combiner bus**, enhancing power intake from RF-heavy zones.

---

## 🔌 Electrical Chain

```txt
[ High-Gain Antenna ]
        ↓
[ Matching Network (L/C filter) ]
        ↓
[ RF Schottky Rectifier ]
        ↓
[ Output Filter Cap ]
        ↓
[ Combiner Bus → Supercap Bank ]
```

---

## 🧱 Hardware Components

| Component               | Spec / Notes                       |
|-------------------------|------------------------------------|
| Antenna (2.4GHz Yagi)   | 8–12dBi gain, 5–8 element           |
| Matching Network        | T-matching or Pi filter tuned to RF band
| RF Diode (Schottky)     | HSMS-2852, SMS7630, BAT15-04W       |
| Rectifier Config        | Full-wave or voltage doubler        |
| Filter Cap              | 10nF–100nF ceramic                  |
| PCB Substrate           | FR4 ≤ 1.6mm or Rogers if < GHz      |
| Shielded Cable          | Coaxial SMA to PCB trace            |

---

## 📡 RF Bands Supported

| Band         | Target Source            | Antenna Type     |
|--------------|--------------------------|------------------|
| 2.4GHz       | Wi-Fi, BLE, Zigbee       | Yagi or Patch    |
| 868/915MHz   | LoRa, ISM telemetry      | Helical or Dipole|
| 433MHz       | Sensors, remotes         | PCB trace or whip|

---

## ⚡ Typical Output (Real-World, Indoor)

| Environment         | Power Density | Harvested (Est.) |
|---------------------|---------------|------------------|
| Office Wi-Fi area   | ~0.1–1 µW/cm² | ~10–50 µW        |
| Server room         | ~1–10 µW/cm²  | ~100–500 µW      |
| Rooftop RF dense    | ~20 µW/cm²+   | ~1–2 mW          |

⚠️ Output is *continuous but low current*. Ideal for trickle-charging caps.

---

## 🔧 Layout Tips

- Keep rectifier close to antenna port
- Use low-loss traces or coax
- Match impedance (~50Ω) at RF input
- Isolate RF from boost inductor zones
- Antenna mounting should face strongest RF source

---

## 📈 Performance Summary

| Parameter         | Value                         |
|-------------------|-------------------------------|
| Voltage Output    | 0.6–3V (varies with gain/env) |
| Max Current       | 100–200µA typical             |
| Footprint         | ~10×3 cm (Yagi + PCB)         |
| Energy Output     | ~50µW–2mW                     |

---

## ✅ Summary

- Directional, gain-boosted RF energy harvester
- Adds power intake from EM-rich environments
- Fully passive, no batteries or control logic
- Feeds into IX-ZeroCell’s DC input rail
- Works with Wi-Fi, BLE, LTE, LoRa, sub-GHz

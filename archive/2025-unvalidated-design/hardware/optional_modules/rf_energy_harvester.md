> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – RF Energy Harvester Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Harvest ambient RF energy from Wi-Fi, mobile, and ISM bands using rectifying antenna arrays

---

## 📡 Overview

This module enables IX-ZeroCell to passively **absorb and rectify ambient radio frequency energy** from nearby sources:

- Cell towers
- Wi-Fi routers
- Broadcast radio (AM/FM/TV)
- Microwave ovens
- Bluetooth devices
- IoT clutter (Zigbee, LoRa, ISM)

---

## ⚙️ Core Concept: Rectenna

**Rectenna = Rectifying Antenna**
RF → Diode → Cap → DC Output

---

## 📶 RF Band Targets

| Band           | Freq (Hz)        | Use Source                        |
|----------------|------------------|------------------------------------|
| ISM            | 433M / 868M / 2.4G| IoT, BT, Zigbee, etc.
| Wi-Fi          | 2.4G / 5G         | Routers, phones, laptops
| Cellular       | 800M–2600M        | 4G, 5G, LTE towers
| TV/FM          | 50M–700M          | Strong in urban cores
| AM             | 500k–1.5M         | Long-range bounce

---

## 🧱 Core Components

| Component          | Notes                                 |
|--------------------|----------------------------------------|
| Patch or Dipole Antenna | Tuned to 900MHz / 2.4GHz / etc.
| Schottky Diode     | BAT62, SMS7630, HSMS-2852 = low Vf, fast switching
| Matching Network   | LC tuned for band of interest
| Storage Capacitor  | 1–100µF ceramic/polymer
| Optional Boost     | LTC3108 or S-882Z = ultralow startup
| Ground Plane       | Important for directional gain
| Optional RF switch | To toggle/stack multiple antenna bands

---

## 🔌 Example Rectenna Circuit

```txt
[ Antenna ]
     ↓
[ Matching Network ]
     ↓
[ Schottky Diode (1-way) ]
     ↓
[ Storage Capacitor ]
     ↓
[ Output to IX-ZeroCell bus ]
```

---

## 🔋 Typical Harvest Power

Ambient energy depends on proximity + transmission power:

| Environment       | Power Range        |
|-------------------|---------------------|
| Rural             | <1µW/cm²            |
| Suburban          | ~10–50µW/cm²        |
| Urban Core        | 100–500µW/cm²       |
| Near Antenna      | 1–5mW/cm² (close!)  |

Boost converter may be required to lift output above 1.8–2.2V.

---

## 🔧 Optimization Tips

- Use multiple antennas for wideband
- Stack outputs via diodes to shared cap rail
- Use directional antennas (Yagi, patch) if targeting tower
- Filter EMI from nearby switching converters
- Shield sensitive analog lines

---

## 🧠 Safety Notes

- Passive receive-only
- Cannot transmit
- Legal globally (no regulatory interference)
- Consider shielding if near sensitive RF gear (e.g., lab work)

---

## ✅ Summary

- Adds ambient energy harvesting from dense RF environments
- Works passively, 24/7, no interaction required
- Real-world yields vary: µW → mW
- Tunable, stackable, and non-intrusive
- Complements kinetic, TEG, and solar harvesters in IX-ZeroCell

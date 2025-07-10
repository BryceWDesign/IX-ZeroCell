# IX-ZeroCell – Flexible Solar Array Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Harvest low-voltage DC power from daylight via ultra-thin film solar cells designed for flexible, curved, or wearable applications

---

## 🌞 Overview

This module integrates a **flexible solar film array** to trickle-charge the IX-ZeroCell capacitor bank during daylight exposure.

Designed for:

- Curved surfaces (helmets, tubes, cylinders)  
- Wearables (backpacks, jackets)  
- Stationary low-profile applications  
- Supplemental passive charging layer

---

## 🔋 Output Characteristics

Typical specs per film strip:

| Parameter             | Value                        |
|------------------------|------------------------------|
| Voltage (open-circuit) | 5.5V                         |
| Voltage (under load)   | 4.5–5.0V                     |
| Current (full sun)     | 20–50mA per 10cm x 5cm       |
| Weight                 | ~1g per strip                |
| Thickness              | ~0.2mm                       |

> Flexible organic or CIGS film; encapsulated in PET.

---

## 🧱 Components Required

| Component             | Notes                                 |
|------------------------|----------------------------------------|
| Flexible Solar Film   | 5V rated, e.g. PowerFilm, Sunpower  
| Blocking Diode        | 1N5817 (Schottky) to prevent reverse drain  
| Optional Boost        | TPS61200 or CN3791 for 3.7–5.2V lifting  
| Mounting Adhesive     | Double-sided Kapton or thermal tape  
| Protective Sheath     | PET, acrylic, or polyimide overlay  
| Optional Array Switch | SPDT or logic MOSFET to cut array at night  

---

## 🔌 Circuit Flow

```txt
[ Solar Film Array ]
     ↓
[ Blocking Diode ]
     ↓
[ Optional Boost ]
     ↓
[ Supercap Rail / Charge Bus ]
```

---

## 🛠️ Wiring Strategy

- Connect films **in parallel** for higher current  
- Use **Schottky diodes** per film for isolation  
- Route all outputs to central cap bank via shared rail  
- Add **fuse or polyfuse** for short protection  
- Optional: disconnect at night via MOSFET or timer logic

---

## ☀️ Power Yield Estimate

| Sun Condition        | Output per 2 strips     |
|-----------------------|--------------------------|
| Full Sun              | 100mA @ ~4.8V → ~480mW  
| Overcast              | ~10–20mA @ ~3.5–4V  
| Indoor Window         | ~1–5mA @ ~2–3V  

Daily contribution: **1.5–3Wh in good conditions** depending on placement.

---

## 📎 Integration Tips

- For wearables: route flexible traces to rear-mounted rail  
- For static builds: embed between PET layers or under acrylic  
- Stackable: 2–4 films ideal per 10cm² device surface  
- Avoid shadowing — kills output drastically  
- May combine with RF and kinetic harvesting for synergy

---

## ✅ Summary

- Adds ambient daylight energy capture  
- Ultra-thin, flexible, and discreet  
- Real-world power = 50–500mW depending on sun  
- Boostable to 5V rail via TPS or CN-series chips  
- Completely passive, no software needed


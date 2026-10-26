> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Optional Solar Assist Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Integrate small solar panel to provide additional ambient power input to IX-ZeroCell's combiner rail

---

## 🌞 Module Overview

This module provides an optional **solar energy input**, designed for:

- Indoor trickle charging (office light)
- Outdoor partial exposure (sunlight or cloudy)
- Boosting energy availability during daylight

Connects directly to the **IX-ZeroCell input combiner**, with diode isolation.

---

## ☀️ Panel Specifications

| Panel Type         | Mini crystalline / amorphous
| Power Rating       | 0.5W – 1.5W
| Open Circuit (Voc) | 4.5V – 6V
| Max Output Current | 10mA – 200mA
| Size Range         | 3×5cm to 10×10cm
| Indoor Power       | ~1–5mW typical (fluorescent/LED)

---

## 🔌 Electrical Integration

```txt
[ Solar Panel (~2–6V) ]
        ↓
[ Schottky Diode (SS14) ]
        ↓
[ Combiner Bus (shared with RF, TEG, Kinetic) ]
        ↓
[ Supercapacitor Storage → Boost Stage ]
```

---

## 🧩 Required Components

| Component        | Value / Part #          | Notes                          |
|------------------|--------------------------|--------------------------------|
| Solar Panel      | See specs above          | Use low-light optimized cells
| D1 (Blocking Diode) | SS14 or SS34            | Prevents reverse current at night
| Input Cap (opt.) | 10µF ceramic             | Smoothing ripple on fast charge
| Header/JST       | 2-pin PV connector       | Detachable solar input

---

## ⚡ Performance Snapshot

| Light Source     | Power Delivered | Usable?      |
|------------------|------------------|--------------|
| Office Lighting  | ~1mW             | Slow trickle
| Window Sunlight  | ~50–100mW        | Usable charging
| Outdoor (Cloudy) | ~150mW           | Full assist
| Outdoor (Direct) | >300mW           | Rapid input

**Note:** Max input current must match cap ESR and diode rating (≤200mA typical)

---

## 📐 Mechanical Tips

- Mount panel externally or on PCB lid
- Route via 2-pin JST header or flex cable
- Tilt panel at ~30° if outdoor-mounted
- Keep panel out of shade; ambient matters

---

## ✅ Summary

- Passive solar harvesting (no MPPT needed)
- Feeds directly into IX-ZeroCell’s DC bus
- Diode-isolated, surge-tolerant
- Enables daylight-autonomous operation
- No batteries, no boost from panel — just raw ambient input

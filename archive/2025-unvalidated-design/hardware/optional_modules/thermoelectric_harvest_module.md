> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Optional Thermoelectric Harvest Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Integrate TEG (thermoelectric generator) modules into IX-ZeroCell’s input combiner for heat-based ambient power

---

## 🔥 What It Does

This module uses **Seebeck effect devices** (TEGs) to convert temperature differences (ΔT) into voltage and current. Typical use cases:

- Heat from hands/body
- Sunlight-heated surfaces
- Hot electronics
- Radiator / pipe / engine surfaces

---

## 🧱 TEG Specs (Recommended)

| Parameter         | Value / Range             |
|-------------------|---------------------------|
| TEG Model         | TEC1-12706 (common, cheap)
| Max Power Output  | ~1.5W @ ΔT = 60°C
| Usable Output     | ~10–200mW typical
| Voc               | 1V–5V
| Size              | 40×40mm or smaller

---

## 🔌 Electrical Integration

```txt
[ TEG Module (~1–5V) ]
        ↓
[ Blocking Diode (SS14) ]
        ↓
[ Input Cap (optional) ]
        ↓
[ IX-ZeroCell Combiner Bus ]
        ↓
[ Supercaps → Regulated Output ]
```

---

## 🔩 Required Components

| Component          | Value / Notes              |
|--------------------|----------------------------|
| TEG (Peltier cell) | TEC1-12706 or similar       | Use with ΔT > 5°C
| D1 (Blocking)      | SS14 or MBRS140             | Prevent backflow
| Cin (optional)     | 10µF ceramic cap            | Smooths noise
| Heatsink (hot side)| Small finned ALU or steel   | Helps gradient
| Thermal paste      | Arctic MX-4 or silicone pad | Improves ΔT
| Mounting plate     | Aluminum or copper          | Contact with heat source

---

## ⚙️ Mechanical Setup

- Cold side = ambient air
- Hot side = surface (hand, motor, sunlight)
- Secure tightly for good contact
- Optional heatsink on cold side improves efficiency
- Use thermal pad/paste to avoid air gaps

---

## ⚡ Output Profile (Real-World)

| ΔT (Temp Difference) | Voc    | Max Output | Usefulness               |
|----------------------|--------|------------|--------------------------|
| 5°C                  | ~0.6V  | ~2mW       | Bare minimum
| 10°C                 | ~1.1V  | ~5–10mW    | Begins useful
| 25°C                 | ~2.5V  | ~20–40mW   | Good charge contributor
| 50°C                 | ~4.5V  | ~100–200mW | High-performance edge

---

## ✅ Summary

- Converts heat gradient directly to DC voltage
- Feeds into IX-ZeroCell combiner via Schottky diode
- Works from hand warmth to sun-heated panels
- Adds ambient harvesting mode in thermally active spaces
- 100% battery-free

# Coil Winding Specifications – IX-ZeroCell

This document details the construction and configuration of the **99-stage electromagnetic coil array** used for kinetic energy harvesting in IX-ZeroCell. It is a core subsystem and must be built precisely to ensure uniform output and efficiency.

---

## 🧵 Wire Specification

- **Type:** Enameled Copper Wire (magnet wire)  
- **Gauge:** 30 AWG (0.25 mm diameter)  
- **Insulation:** Polyurethane (or equivalent high-temp rated)  
- **Resistance:** ~0.345 ohms/m  

---

## 📐 Winding Parameters

| Parameter             | Value              |
|-----------------------|--------------------|
| Turns per coil        | 200 turns          |
| Number of coils       | 99                 |
| Coil form diameter    | 12 mm              |
| Coil height           | 15 mm              |
| Wire length per coil  | ~6.2 meters        |
| Resistance per coil   | ~2.1 ohms          |
| Total resistance      | ~207.9 ohms        |
| Total length of wire  | ~613.8 meters      |

> ⚠️ Note: These coils are connected in series by default. If you require a different topology (e.g. 3-phase segmented), refer to the `/hardware/wiring_topology.md`.

---

## 🛠️ Winding Process

1. **Use a jig or mandrel** with 12mm diameter.
2. Anchor one end of the wire and apply light tension throughout the process.
3. Wind **200 tight, even turns**, avoiding overlap. Use a layering guide or bobbin separator if needed.
4. Secure each completed coil with heat-resistant tape or UV-set epoxy.
5. Trim and strip 5mm of insulation from each lead.

---

## 🔌 Coil Arrangement

- Arrange all 99 coils **in-line** around a non-conductive central rod or frame.
- Ensure all coils are aligned with magnetic polarity in the same direction.
- Use mounting brackets every 10 coils to prevent slippage or misalignment.
- Leave 2–3mm air gap between adjacent coils to avoid mutual inductance distortion.

---

## 🧲 Magnetic Core

- Use a single **N52 neodymium bar magnet** sized 20x10x5mm.
- Insert the magnet loosely or mechanically drive it through the coil array (e.g. via shaking, vibration, crank).

---

## 🔍 Testing Each Coil

1. Connect multimeter probes to each coil individually.
2. Move a magnet through the coil and observe the induced voltage spike.
3. Record resistance — reject any coil outside ±10% of 2.1Ω.

---

## 🧼 Maintenance Notes

- Re-check winding insulation every 6 months if used in field conditions.
- Re-epoxy or secure coils if exposed to high vibration or temperature swings.

---

*Document authored by Bryce Wooster for IX-ZeroCell – July 2025.*


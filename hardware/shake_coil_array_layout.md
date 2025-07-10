# IX-ZeroCell – Shake Coil Array Layout

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Physical arrangement and mounting logic for 99 magnetic kinetic tube coils

---

## 🔩 Coil Quantity and Objective

**Target:** 99 individual shake coils, each generating voltage pulses from axial magnetic movement  
- **Mode:** Primarily vertical alignment  
- **Goal:** Maximize per-shake kinetic-to-electrical conversion with minimal interference or resonance bleed

---

## 📏 Coil Dimensions (Assumed Standard)

| Parameter      | Value         |
|----------------|---------------|
| Tube Length    | 100mm (4")    |
| Outer Diameter | 20mm (0.8")   |
| Magnet Stroke  | 60mm travel   |
| Coil Windings  | 600–900 turns |

---

## 🧱 Array Configuration

| Layout         | Vertical Columns | Horizontal Rows | Total Units |
|----------------|------------------|------------------|-------------|
| Honeycomb Grid | 11               | 9                | 99          |

- **Staggered hexagonal pattern** for shock absorption  
- **Vertical mounting orientation** preferred for gravity assist and symmetrical stroke damping  
- Coil bases mounted on **shock-isolated rubber grommets** into a plate

---

## 📦 Footprint Estimate

| Axis | Dimension |
|------|-----------|
| Width| ~240mm    |
| Height| ~270mm   |
| Depth| ~100mm    |

This creates a **dense upright block** the size of a **small desktop tower PC** or **a slim trash can**.

---

## 🧲 Damping Strategy

- **Each coil mounted in rubber grommet** (OD 6mm, ID 3mm)  
- Prevents high-frequency ringing and mechanical fatigue  
- Tubes press-fitted or clipped into **laser-cut polycarbonate or PETG matrix tray**

---

## 🔧 Wiring Bus Strategy

| Tier           | Bus Type       | Notes                                |
|----------------|----------------|----------------------------------------|
| Individual Coil| Magneto wires  | AWG 28–30 enamel copper  
| Sub-Cluster    | 11 groups      | Each group of 9 coils in parallel  
| Main Bus       | Combiner rail  | Diodes per branch to prevent backfeed  
| Output         | To BQ25570     | Each group diode-isolated, merged via OR-ring  

All wiring routed in **braided shield sleeve** or heatshrink tunnels to prevent chafing or EM cross-talk.

---

## 🔌 Mounting Support

- Internal **3D-printed trays (PETG)** stackable  
- Spacers (3mm) between layers for airflow  
- **Screw-mount holes** on outer frame (M3 inserts)  
- Optional **foam bumpers** at outermost edge to prevent casing rattle

---

## 🧯 Safety Considerations

- **Ventilation holes** on top and bottom of casing for convective cooling  
- Avoid placing tubes adjacent to output power traces — keep at least 10mm  
- Faraday mesh shielding (optional) if RF interference detected

---

## ✅ Summary

- 99 coils in **11×9 hex-packed grid**, vertically oriented  
- Grommeted base mounting + PETG lattice frame  
- Outputs wired in 11 parallel groups → merged to power bus  
- Size: **like a narrow trash bin or slim PC tower**
- Design is mechanically sound, shock-damped, and fully scalable


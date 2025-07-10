# IX-ZeroCell – PCB Layout Guidelines

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define best practices for trace design, noise isolation, thermal relief, capacitor placement, and EMI suppression in low-power energy harvesting PCBs

---

## 🖥️ Board Stack

- Recommended: **2-layer or 4-layer PCB**
- Inner layer (if 4L): solid GND plane
- Outer layers: signal + power

---

## 🛤️ Trace Width + Routing

| Signal Type        | Min Width (1oz Copper) | Notes                       |
|--------------------|------------------------|-----------------------------|
| Harvest Input      | 0.5 mm                 | Handles low-voltage AC  
| Supercap Rail      | 1.0–1.5 mm             | High peak current  
| Boost Output (5V)  | 1.0 mm                 | Minimize resistance  
| Signal/Logic       | 0.25 mm                | For voltage sense, I2C, etc.

- Avoid **sharp 90° turns** (prefer 45° or arcs)  
- Route **short, direct traces** for capacitors  
- Keep **high-current paths wide and short**

---

## ⚡ Ground Strategy

- Use a **continuous ground plane** (fill entire bottom layer)  
- Tie all component grounds **at a single star ground** if needed  
- Avoid crossing high-speed lines over ground plane splits  
- Place vias to connect top/bottom GNDs frequently

---

## 🔋 Capacitor Placement

- **Input caps:** As close as possible to VIN pin  
- **Output caps:** Directly at VOUT pin of boost  
- **Decoupling caps:** Always within 1–2mm of Vcc pins on ICs  
- Use **X7R or C0G ceramic** types for stability  
- Avoid stacking too many ceramics on shared traces (can resonate)

---

## 🌡️ Thermal Management

- Use **thermal vias** under heat-dissipating parts (e.g. MT3608)  
- Add **copper pour zones** around hot ICs (tie to GND plane)  
- Separate boost converter from supercap bank physically if possible  
- Allow airflow if enclosed — add vent holes if passively cooled

---

## 📡 EMI/Noise Reduction

- Keep harvesting inputs **away from switch-mode output traces**  
- Use **ferrite bead (120Ω @ 100MHz)** on output line if noisy  
- Shield long RF or piezo input lines with ground trace on either side  
- Add **ground pour** around diode bridges and TVS if harvesting RF  

---

## 🧪 Test/Debug Tips

- Add **test pads** on:  
  - VIN of boost  
  - VOUT of MT3608  
  - Supercap rail midpoint  
  - MPPT VSTOR / VBAT pins

- Leave **at least 1 spare JST header** for emergency reflash/debug  
- Keep 1x USB port for serial monitor access if microcontroller is added

---

## ✅ Summary

- Wide traces for current, short for decoupling  
- Avoid EMI paths by separating input and output domains  
- Ground plane continuity is sacred  
- Use thermal pours + vias under heat components  
- Always place ceramic caps close and in correct order


# IX-ZeroCell – Mounting & Mechanical Dimensions

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define the physical size, shape, port alignment, and mounting hole specs of the IX-ZeroCell device

---

## 📏 Overall Board Dimensions

| Dimension | Value   | Notes                      |
|-----------|---------|-----------------------------|
| Width     | 120mm   | Includes USB port overhang  
| Height    | 80mm    | Matches component height zone  
| Thickness | ~16mm   | With capacitors + JST headers  

Real-world comparison: **About the size of a paperback novel**, or **1.25x the footprint of a large smartphone**, with capacitor height pushing it closer to a **thick deck of cards**.

---

## 🧱 Realistic Volume Approximation

**Stack of 99 flashlight coils + electronics = ~4.5L**

- Size class: **Small desktop speaker**, **bathroom trash bin**, **shoebox-sized enclosure**
- With 3D-printed support casing: fits in **6"x6"x12" vertical container**

Weight estimate: ~1.2–1.6 kg (mostly copper)

---

## 🔩 Mounting Hole Specs

| Hole # | X (mm) | Y (mm) | Diameter | Usage            |
|--------|--------|--------|----------|------------------|
| 1      | 4.0    | 4.0    | 3.2mm     | Top-left corner  
| 2      | 116.0  | 4.0    | 3.2mm     | Top-right corner  
| 3      | 4.0    | 76.0   | 3.2mm     | Bottom-left corner  
| 4      | 116.0  | 76.0   | 3.2mm     | Bottom-right corner  

- Hole spacing: **112mm × 72mm**
- Screw compatibility: M3 bolts (preferred), 6-32 possible

---

## 🎛️ Port Cutout Alignments

| Port    | Edge Distance | Height from Bottom | Notes                      |
|---------|----------------|--------------------|-----------------------------|
| USB-A   | Right edge: 1mm| Centered @ 25mm    | Standard plug depth: 13mm  
| USB-C   | Bottom edge: 1mm| Centered @ 60mm   | 16-pin, sink-only  
| JST-XH  | Top edge: 3mm  | Centered @ 40mm    | 2-pin sensor header  
| Header  | User-defined   | User-defined       | Prototyping access

All ports aligned **flush to board edge** for ease of enclosure cutouts.

---

## 📐 Enclosure Fit Guidance

| Type             | Min Internal Dimensions | Notes                       |
|------------------|--------------------------|------------------------------|
| Vertical shell   | 6x6x12 inches            | Vent recommended for heat  
| Desktop box      | 130x90x25mm              | For tabletop units  
| Pocketable case  | No (too thick)           | Would require redesign  
| Wearable         | Not practical            | Too bulky for clothing use

---

## 🧲 Thermal Vents

- Cut **4–6 vent slots (2mm x 10mm)** on side opposite USB  
- Passive air convection recommended  
- Avoid placing ports near vent zones

---

## 📸 Optional Silkscreen Markings

- Board edge: `IX-ZeroCell v1.0 – Bryce Wooster`  
- Mount holes: `M3` with arrows  
- Labels near USB: `OUT 5V`, JST: `OUT 3.3V`

Use white silkscreen on matte black PCB for high contrast.

---

## ✅ Summary

- Final board size: **120mm × 80mm × 16mm**  
- Mounting holes: 112×72mm grid, 3.2mm diameter  
- Port cutouts pre-aligned to board edge  
- Full size fits in a **shoebox / small trash bin / desk speaker** class enclosure  
- Thermal considerations, enclosure clearances, and labeling included


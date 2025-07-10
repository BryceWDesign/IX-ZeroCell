# IX-ZeroCell – Internal Power Bus Layout

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define the internal power routing from supercap bank through boost converter to output ports

---

## ⚡ Power Flow Path Overview

```txt
[ Supercap Bank ]
      │
      ▼
[ Soft Start FET + NTC ]
      │
      ▼
[ Boost Converter (MT3608) ]
      │
      ▼
[ Voltage Selector Divider ]
      │
      ▼
[ Output Rail ]
      │
 ┌────┼────┬─────────┐
 ▼    ▼    ▼         ▼
USB-A USB-C JST     Header
```

---

## 📐 PCB Trace Width Guidelines

| Segment                         | Max Current | Recommended Width (1oz) |
|--------------------------------|-------------|--------------------------|
| Cap Bank → Soft Start FET      | ~1.5A       | 1.5mm (60 mil)  
| FET → Boost Input              | ~1.2A       | 1.5mm  
| Boost Output → Selector        | ~1.2A       | 1.0mm  
| Selector → Fuses               | ~1.0A       | 1.0mm  
| Fuse → Output Ports            | ≤500mA      | 0.75mm (30 mil)

- **Use 2oz copper** if possible — doubles current capacity  
- **Keep all traces short and wide**, especially around the boost converter

---

## 🥇 Copper Pour Strategy

- Use **solid copper pours** for GND and VOUT planes  
- GND plane should run full bottom layer (low impedance return path)  
- VOUT pour on top layer from boost output → fuse bank → output connectors  
- Stitch pours with **via fences** every 100mil for noise and EMI suppression

---

## 📊 Power Integrity Enhancements

| Feature            | Benefit                          |
|--------------------|----------------------------------|
| Wide pours         | Lower voltage drop under load  
| Short feedback loop| Boost stability improves  
| Via stitching      | RF grounding + thermal relief  
| Ground plane       | Reduces switching noise  
| Decoupling caps    | Buffers high-speed current spikes

> Add **10µF + 0.1µF caps** near boost converter and output connectors

---

## 🧲 Keep-Out Zones

- Avoid routing under inductor of MT3608  
- No signal traces through power pour  
- Separate digital and power GNDs if MCU present

---

## 🔧 Mounting Considerations

- Leave **1.0mm clearance** around power traces for solder mask and etching tolerance  
- Place **test points** for VOUT and GND before port breakouts  
- Keep **output trace segments isolated by fuse pads** to localize shorts

---

## ✅ Summary

- Internal power path flows: Supercap → Soft start → Boost → Selector → Fuses → Ports  
- Trace widths designed for 1A+ handling  
- Ground and VOUT use dedicated copper pours with via stitching  
- Decoupling, test points, and clearance all enforced


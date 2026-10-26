> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Cooling Strategy and Thermal Management

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Document passive and optional active cooling techniques for BQ25570, boost regulator, and supercapacitor cluster under high harvest or load conditions

---

## 🌡️ Why Cooling Matters

- Supercaps can heat up from high inrush currents
- BQ25570 may warm up during rapid charge/discharge events
- Boost converters (e.g. MT3608) dissipate heat when outputting near max current (>500mA)

Proper thermal handling increases **reliability**, **efficiency**, and **safe continuous output**.

---

## 🧊 Passive Cooling Techniques

### 1. **Thermal Copper Plane Under MPPT + Boost Regulator**

- Use copper pour on PCB under ICs
- Connect to **ground plane**
- Stitch vias (min 4) for multi-layer heat dissipation

### 2. **Graphite Thermal Pad (on supercap array)**

- Cheap, ultra-light option
- Conducts heat laterally
- Prevents localized hotspots in cap pack

### 3. **Ventilation Holes + Elevation**

- Enclosure should allow **vertical convection**
- Add **vent slots** above MPPT and boost zone
- Raise board **3–6mm** from base to improve airflow

---

## 🌀 Optional Active Cooling (If Needed)

> Not required for most IX-ZeroCell use cases, but valid if:
> - Operating near hot industrial equipment
> - Unit enclosed without airflow
> - Output current remains >700mA for extended time

### Option A – 5V Micro Fan

- Part: Sunon MF25101V2
- Draws 100mA max
- Mount near MPPT + MT3608 zone

### Option B – PWM Fan (temp triggered)

- Thermistor → MCU → PWM line → Fan
- Can be added later via I2C bus

---

## 🧲 Thermal Interface Options

| Surface          | Cooling Material          | Notes                    |
|------------------|----------------------------|--------------------------|
| BQ25570           | Thermal paste or pad       | Use 0.5mm silicone pad    |
| Supercap Array    | Graphite sheet             | Avoid thick adhesive pads
| MT3608 Regulator  | Copper pad + vias          | Add ferrite bead nearby if EMI spikes

---

## 🧪 Testing for Thermal Bottlenecks

- Use FLIR or IR temp gun during:
  - Full kinetic harvest (shaking all tubes)
  - Full USB output draw (600mA–1A)
- Monitor: If any zone exceeds **65°C sustained**, consider active cooling

---

## ✅ Summary

- Most IX-ZeroCell builds can be fully passively cooled
- Simple PCB layout choices drastically improve heat dissipation
- Active cooling (5V fan) optional for sealed or high-current use cases
- Proper cooling = longer life, safer supercaps, and more stable output

# IX-ZeroCell – MPPT Intake Optimization

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Optimize intake tuning for BQ25570 using programmable MPPT to stabilize energy harvesting across kinetic + ambient sources

---

## 🔋 Component: BQ25570

Texas Instruments chip designed for ultra-low-power energy harvesting.  
Supports:
- MPPT tracking
- Boost charging from sub-100mV sources
- Energy storage in supercaps or rechargeable cells

---

## ⚡ MPPT Overview

MPPT = **Maximum Power Point Tracking**  
This dynamically adjusts intake current/voltage to extract optimal energy from sources like:

- Kinetic shake-tubes
- RF antennas
- TEG (Thermoelectric)

---

## 🔧 Tuning MPPT with Resistors

The BQ25570 determines its internal target via a resistor divider:

```txt
VMPPT = VREF * (R1 + R2) / R2
```

- VREF = 1.2V (fixed)
- VMPPT = desired input voltage at max power (set between 0.1V to 2V)

---

### 🎯 Target MPPT Voltage

We want to optimize for:

- RF harvester: ~0.5V
- Kinetic coil: ~0.6V–0.9V
- TEG module: ~0.2V–0.3V

We average this around **0.55V**

---

### 📐 Calculating Divider

To set VMPPT = 0.55V:

```txt
0.55V = 1.2V * (R1 + R2) / R2
=> (R1 + R2) / R2 = 0.458
=> R1 = (0.458 * R2) - R2 = -0.542 * R2
```

This math won’t work directly — so we **flip the configuration**:

Use **MPPTSET = VSTOR × (R1 / (R1 + R2))** mode

Let’s instead target **45% of VSTOR (typ. ~2.4V)** → VMPPT = 1.08V

Use:

- R1 = 100kΩ  
- R2 = 122kΩ

Or any combo that results in:

```txt
VMPPT ≈ VSTOR × (100 / 222) ≈ 0.45 × VSTOR
```

BQ25570 will then hold input near this value using internal comparator logic.

---

## 🔁 Periodic Sampling Mode

- BQ25570 samples MPPT target every **16 seconds**
- Uses this to adjust intake impedance automatically
- Works even if input source changes over time (e.g. wave peaks in kinetic modules)

---

## 📦 BOM – MPPT Tuning

| Component | Value   | Tolerance | Qty | Notes                        |
|-----------|---------|-----------|-----|------------------------------|
| R1        | 100kΩ   | 1%        | 1   | MPPT high side  
| R2        | 122kΩ   | 1%        | 1   | MPPT low side  
| Cap       | 0.1µF   | –         | 1   | Noise filter on MPPT pin  

---

## 🔐 Notes on Multi-Source Harvesting

- If one input (e.g. RF) surges, the MPPT adjusts globally  
- For true parallel optimization, use **diode OR-ing** and **multiple BQ25570 chips**
- Current IX-ZeroCell config uses **1 MPPT** for all inputs, tuned to middle value

---

## ✅ Summary

- MPPT tuning = key to stable intake from unpredictable ambient sources  
- Resistor divider sets percentage of VSTOR used as input target  
- Our config targets 45% of VSTOR ≈ 1.08V  
- Works with RF, kinetic, thermal sources simultaneously  
- Passive, periodic MPPT sampling ensures long-term efficiency


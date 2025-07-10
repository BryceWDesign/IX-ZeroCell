# IX-ZeroCell – Triboelectric & Piezo Harvesting Block

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define energy harvesting from high-voltage, low-current sources like tribo pads and piezo films, and how to safely steer them into the MPPT circuit

---

## 🌩️ Source Type Overview

| Source          | Typical Output | Frequency | Notes                     |
|-----------------|----------------|-----------|---------------------------|
| Triboelectric   | 100–800Vpp     | <10 Hz    | Triggered by surface contact/sliding  
| Piezoelectric   | 30–150Vpp      | 5–200 Hz  | Triggered by vibration/impact

---

## 🧪 Signal Characteristics

- **High voltage**, but **extremely low current**
- Short duration pulses
- Often AC and **very spiky**

---

## ⚠️ Direct-to-MPPT = ❌ Danger

Sending these straight to MPPT (BQ25570) would damage it. We must:

1. Rectify and clamp the voltage
2. Smooth into useful DC
3. Merge into Node A (MPPT VIN_DC)

---

## 🔧 Hardware Configuration

### 1. **Input Rectification**

| Component  | Suggested Part     |
|------------|---------------------|
| Diodes     | UF4007 (ultrafast) or 1N4007 if slower  
| Config     | Full Bridge         |
| Cap        | 10nF – 100nF ceramic across bridge output

> For extreme miniaturization: use **MMSD4148** SMD diodes or similar

---

### 2. **Clamping & Dampening**

- Add **TVS diode** across rectifier output:
  - Part: SMAJ15CA (15V bidirectional TVS)
  - Prevents spikes from exceeding MPPT input limit

- Optional: **Zener diode (12V, 1W)** in parallel for backup clamping

---

### 3. **Energy Mixing to Node A**

- After rectification + dampening:
  - Add **100Ω resistor** in series to smooth pulse edge
  - Then route into **Node A** (harvest intake junction)

> You now have safe, damped HV energy joining kinetic + RF + thermal inputs

---

## 🧩 Wiring Topology

```txt
[TRIBO PAD] → Bridge → TVS → R100Ω → Node A  
[PIEZO FILM] → Bridge → TVS → R100Ω → Node A  
```

All return lines connect to common GND near MPPT

---

## 🛡️ PCB Layout Tips

- Keep HV signal paths short  
- Use 2oz copper if placing diodes near pad/film  
- Route GND under dampening components  
- Add 0.1µF ceramic cap directly across MPPT VIN_DC and GND for final filtering

---

## 🛒 Parts List Snapshot

| Component       | Example Part     | Note                          |
|------------------|------------------|-------------------------------|
| HV Bridge Diode  | UF4007 x4        | 1A, 1000V, fast-switching     |
| TVS Clamp        | SMAJ15CA         | 600W peak surge, bidirectional  
| Smooth Cap       | 100nF X7R        | Output side of rectifier      |
| Input Resistor   | 100Ω 0.5W        | Optional surge softener       |
| Tribo Pads       | Custom polymer   | PDMS/silicone preferred       |
| Piezo Films      | Murata 7BB-20-6L | Can mount on PCB underside    |

---

## ✅ Summary

- **Rectify, clamp, and steer** all HV pulses safely  
- Use TVS and Zener for MPPT protection  
- Low-pass each input before merging to Node A  
- These sources extend uptime in shock/vibe-heavy environments — zero batteries needed


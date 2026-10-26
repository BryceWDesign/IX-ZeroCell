> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Supercapacitor Bank Expansion

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Define safe and scalable expansion methods for increasing energy storage capacity using supercapacitors in the IX-ZeroCell system

---

## ⚙️ Motivation

More capacitance = longer runtime or support for higher current bursts.
But improper scaling = fire, leaks, reverse voltage, or poor balancing.

---

## 🧪 Baseline Configuration (Recap)

| Cap Type            | Value     | Max Voltage | Notes                  |
|---------------------|-----------|-------------|------------------------|
| Supercap (EDLC)     | 2.7V      | 10F         | Common small module
| Initial Bank        | 2 or 4x   | Series      | ~5.4V or 10.8V total
| Balancing Method    | Passive   | 10kΩ bleed  | Or diode + resistor

---

## 🧰 Expansion Strategies

### 📈 Parallel Expansion

- **Increases total capacitance**
- Keeps voltage the same
- Add caps in parallel across each stage

```txt
[ Cap1 ]—+
         |
[ Cap2 ]—+——— Node A
         |
[ Cap3 ]—+
```

> Effective Capacitance = C1 + C2 + C3

### ⚠️ Watch out:
- Match ESR (equivalent series resistance) values closely
- Don’t mix new/old caps — aging = imbalance
- Add 0.01Ω–0.1Ω resistor per cap for self-limiting inrush

---

### 🔀 Series Expansion (Voltage Scaling)

- Stack more caps in series to support higher voltage rails (e.g. 9V)
- Must balance every cap **individually**
- Use **passive balancer resistors** (10kΩ typical) OR active balancers

| Total Voltage | # of Caps | Balance Required |
|---------------|-----------|------------------|
| 5.4V          | 2x 2.7V   | Yes
| 8.1V          | 3x 2.7V   | Yes
| 10.8V         | 4x 2.7V   | Yes

> Each cap charges unevenly due to leakage variance → must be corrected

---

## 🌡️ Thermal Management

- Space each cap by **at least 2–3mm**
- Avoid placing them directly next to the boost converter or MPPT IC
- Add thermal vias under hot components (MT3608, protection diodes)

---

## 🧲 Mounting + Safety

- Use **supercap holders or zip ties + silicone** if on perfboard
- Ensure **vent hole side of cap is facing up**
- Never reverse polarity — can lead to rupture
- Keep well away from RF harvesting antennae to prevent coupling noise

---

## 🧠 Smart Expansion Design Tips

- Use **same brand/batch of caps** per bank
- ESR mismatch = imbalance and heating
- Combine multiple banks with ideal diodes between them to segment energy

```txt
[Bank A] —|<|—+
              |
[Bank B] —|<|—+—— Output
```

> Prevents bank A from backfeeding bank B on imbalance

---

## 🔧 Real-World Config Example

**Goal:** 25F @ 5.4V total
**Build:** 5x 5F 2.7V caps → series/parallel combo
**Resulting Energy:**
- E = ½·C·V² = 0.5 * 25 * (5.4²) ≈ **364 joules**
- Supports up to **200mA loads for ~30+ seconds**

---

## ✅ Summary

- Add caps in **parallel** for more energy
- Add caps in **series** for higher voltage
- Always balance each cell in series
- Watch heat buildup and ESR
- Use ideal diodes for modularity
- Never mix old/new caps or brands

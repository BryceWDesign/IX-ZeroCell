# IX-ZeroCell – Supercapacitor Bank Balancer Circuit

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Prevent overvoltage across individual capacitors in 3x series 2.7V bank  
**Applies To:** Any IX-ZeroCell configuration using supercapacitor banks > 1 cell

---

## 🧠 Why Balancing Is Required

- Supercapacitors in series **do not naturally self-balance**
- If one cap hits 2.85V while others lag behind, it can **degrade or rupture**
- This happens especially during:
  - Cold-start surges
  - MPPT misfires
  - Rapid input bursts (e.g. kinetic charging)

---

## ⚙️ Configuration: 3x Maxwell 2.7V 1000F Caps in Series

- Target full bank voltage: 7.5–8.1V
- Each cap: safe operating range **2.2V – 2.7V**
- Balance ensures voltage remains <2.7V per unit even under charge

---

## Option 1 – Passive Balancer (Resistive)

### 🛠️ Schematic:

```txt
[Cap1]─[R1]─┬─[Cap2]─[R2]─┬─[Cap3]─[R3]─┬─GND
            │            │             │
           GND          GND           GND
```

### 🔧 Resistor Calculation:

Rule of thumb:  
- Use values between **470Ω and 1kΩ**  
- Lower = faster balance, more heat  
- Higher = slower balance, less heat  
- Power = V² / R per resistor

Example (1kΩ):  
- At 2.7V → 7.29mW per resistor (safe)

**Recommended:**  
```txt
R1 = R2 = R3 = 1kΩ, 1/4W
Use precision (1%) metal-film resistors
```

---

## Option 2 – Active Balancer Module (Preferred)

Use off-the-shelf **active balancing boards** with built-in ICs (e.g. LTC3300-1 or equivalents)

### 🔋 Benefits:
- Low-loss current shuttling between caps
- Works dynamically under load and during charge
- Great for environments with surging energy bursts

### 🔧 Recommended Boards:
| Name | Source | Notes |
|------|--------|-------|
| 3S Supercap Active Balancer | AliExpress, SparkFun mods | ±5mV balancing accuracy |
| DIY LTC3300-based Board | OSH Park / GitHub repos | Needs MCU config in rare cases |

---

## 🛡️ Safety Tips

- Keep all balance resistors at least 0.25W rating
- Mount on ventilated area if passive  
- If active balancer used, ensure it matches **3S config** exactly  
- Add 0.1µF ceramic decouplers across each capacitor

---

## 🧪 Testing the Balancer

After install:
1. Charge bank slowly from 0V to ~7.5V
2. Monitor each cap’s voltage with multimeter
3. All caps should stay within **±0.1V of each other**
4. If one cap climbs too fast → check connection or balancer failure

---

## ✅ Summary

| Option  | Cost | Complexity | Performance |
|---------|------|------------|-------------|
| Passive | Low  | Simple     | Good        |
| Active  | Mid  | Plug+Play  | Best        |

**Recommendation:** Use passive balancer to start; upgrade to active if high-speed or high-burst systems are used (e.g. rapid pulse harvesting)


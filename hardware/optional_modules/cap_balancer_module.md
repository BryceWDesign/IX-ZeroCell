# IX-ZeroCell – Optional Active Supercap Balancer Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Optional circuit to actively balance voltage across series supercapacitors in IX-ZeroCell

---

## 🔋 Why Use Active Balancing?

Passive balancing (via resistors) is simple but inefficient. For better:

- Supercap **lifespan**  
- Equal **voltage distribution**  
- **Higher efficiency** during harvesting  
- Safer operation in **hot environments**

Use this module when:

- Ambient temps > 40°C  
- System runs continuously  
- Harvesting exceeds 500mW  

---

## 🔌 Topology Overview

```txt
[ Supercap1 ] — [ Supercap2 ]
     ↓               ↓
 [ Op-Amp Sense ]   [ Op-Amp Sense ]
     ↓               ↓
 [ Gate Driver → MOSFET Shunt ] ←→ [ Cap ]
```

Each op-amp senses imbalance and turns on a shunt MOSFET to equalize.

---

## 🔧 Components (Per Cap)

| Component           | Example Part          | Notes                     |
|---------------------|------------------------|----------------------------|
| Op-Amp (quad)       | LM324, TL074           | One per cap (or duals)     |
| MOSFET (P-channel)  | IRF9540, SI2301        | Rds(on) < 100mΩ preferred  |
| Shunt Resistor      | 0.1–0.5Ω 1W            | Sets equalization current |
| Voltage Divider     | R1/R2 = 10kΩ/10kΩ      | For op-amp reference  
| Bypass Cap          | 0.1µF near op-amp Vcc  | Noise filter              |
| Heatsink (opt.)     | Small fin or copper tab| For high imbalance ops    |

---

## 📐 Schematic Notes

- Supply op-amps from post-boost 5V rail  
- Tie op-amp V- to GND, V+ to 5V  
- MOSFET drain → cap negative terminal  
- Shunt resistor in MOSFET source leg  
- Output tied to op-amp comparator out  

---

## 🧪 Performance Metrics

| Condition         | Passive Balancing | Active Module |
|-------------------|--------------------|---------------|
| Voltage Skew @ Full Cap | ±0.2V         | < ±0.05V      |
| Heat Loss         | Continuous         | Load-based    |
| Efficiency        | Low (80–85%)       | High (95%+)   |
| Cap Lifespan      | Moderate           | High          |

---

## 🛠️ Layout Advice

- Route op-amp traces clean and short  
- Keep balancing shunt FETs close to cap terminals  
- Shield op-amp inputs if near RF  
- Don’t exceed Vgs(max) of MOSFET  

---

## ✅ Summary

- Provides automatic, smart voltage balancing between supercaps  
- Optional upgrade to passive resistor method  
- Recommended for large cap banks or high-harvest conditions  
- Plug-in compatible with IX-ZeroCell architecture  
- Improves energy use, safety, and capacitor health


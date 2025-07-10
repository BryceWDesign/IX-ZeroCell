# IX-ZeroCell – Capacitor Bank Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Document specifications, layout, and safety considerations for building the main capacitor bank assembly for IX-ZeroCell.

---

## 💡 Why This Matters

- Capacitors are the primary energy reservoir in IX-ZeroCell.  
- Stable pulse delivery depends on quality, layout, and capacity of this module.  
- Safety margins must always be factored for high-voltage pulse discharge.

---

## ✅ Capacitor Specifications

| Attribute         | Value                             | Notes                       |
|-------------------|-----------------------------------|----------------------------|
| Capacitance Total | 1,200,000 μF (1.2 F)             | Adjustable by array size   |
| Rated Voltage     | 450V–500V DC                      | Never exceed 80% of rating |
| ESR               | < 5 mΩ                            | Lower = better performance |
| Type              | Metalized Polypropylene Film / Supercapacitor | Avoid electrolytics in pulse config |
| Lifespan          | 10,000+ cycles                    | Derate at high temps       |

---

## 🛠️ Bank Configuration Example

- **Cell Count:**  
  - 99 tubes = 99 pulse units = 99 capacitor bank cells minimum.  
- **Arrangement:**  
  - Parallel blocks of (5–10) capacitors tied to each coil module.  
  - Bus-bar style copper links preferred over simple wire.

---

## ✅ Assembly Guidelines

- Use insulated copper bus bars (minimum 2-inch wide, 5mm thick).  
- Capacitors must be secured in vibration-resistant mounts.  
- Provide clear labeling for polarity and rated voltage.  
- Allow thermal expansion gap between capacitor cells.

---

## ⚠️ Important Safety Notes

- Pre-charge circuit mandatory: Avoid direct switch-on from zero to full bank.  
- Bleed resistors must be installed on each capacitor cell (refer to Load Resistor Module).  
- Inspect all units every 6 months for bulging, leakage, or breakdown signs.

---

## ✅ Example Capacitor Models (Real-World Verified)

| Model                   | Capacitance | Voltage | Vendor Example        |
|------------------------|-------------|---------|----------------------|
| Maxwell BMOD0083 P016 B02 | 83F        | 16V      | Kemet/Maxwell         |
| Cornell Dubilier 947D  | 1200 μF      | 500V     | Digi-Key / Mouser     |
| Nichicon LGU Series    | 470 μF       | 450V     | Standard distributors |

*Note: Combine models where needed to hit total spec.*

---

## ✅ Summary

- Capacitor Bank Module = core of IX-ZeroCell pulse energy supply.  
- High-reliability parts only—no shortcuts or cheap substitutes.  
- Critical to size banks appropriately to total system coil count and expected pulse load.

---


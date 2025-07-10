# IX-ZeroCell – Load Resistor Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Provide controlled load during system testing, calibration, and failure simulation for IX-ZeroCell hardware.

---

## 💡 Why Load Resistors?

- Simulate real-world loads without risking sensitive equipment.  
- Useful for validating capacitor discharge profiles and pulse output safely.  
- Critical for tuning output parameters and verifying manual override systems.

---

## 🧱 Recommended Resistor Specifications

| Test Application        | Resistor Type        | Resistance Value | Wattage Rating    |
|------------------------|---------------------|------------------|-------------------|
| Pulse Discharge Load   | Wirewound or Ceramic | 0.5–5 Ohms       | 200W–2000W         |
| Control System Testing | Standard Power Resistor | 10–100 Ohms    | 10W–50W           |
| Capacitor Pre-Charge   | High-Ohm Bleed Resistor | 1k–10k Ohms     | 5W–20W            |

---

## ⚙️ Wiring Guide

- Mount load resistors onto heat sinks or dedicated cooling plates.  
- Use high-amp rated terminals (M6 bolts or screw terminals preferred).  
- For pulse discharge testing, use resistor arrays wired in parallel to handle necessary current.

---

## ✅ Example Resistor Array Setup

- **Configuration:**  
  - (4x) 1 Ohm, 500W Ceramic Resistors in parallel → Effective: 0.25 Ohm, 2000W  
- **Purpose:**  
  - Absorb pulse from 99 coil stack unit safely.

---

## ⚠️ Thermal Management Notes

- Always use forced air cooling for load resistor arrays above 500W.  
- Monitor temperature using IR thermometer or embedded thermistors.  
- Failure to manage heat = risk of fire or damage.

---

## 🛠️ Enclosure Suggestions

- Mount resistors in metal cages with perforated ventilation.  
- Label all terminals and load rating values clearly.  
- Ensure resistor array location allows easy visual inspection during tests.

---

## ✅ Summary

- Load Resistor Module = non-optional for safe system testing and tuning.  
- Must be sized appropriately for full coil stack and capacitor bank output.  
- Integrate into every IX-ZeroCell lab build before live-load experiments.

---


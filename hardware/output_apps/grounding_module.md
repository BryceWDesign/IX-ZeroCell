# IX-ZeroCell – Grounding Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define mandatory grounding and shielding protocols for IX-ZeroCell system deployment and testing.

---

## 💡 Why Proper Grounding?

- Protects human operators from electrical shock.  
- Reduces EMI (Electromagnetic Interference) affecting nearby electronics.  
- Stabilizes pulse discharge paths—improves consistency and performance.  

---

## ✅ Grounding Types for IX-ZeroCell

| Ground Type          | Description                                 | Connection Notes                       |
|---------------------|---------------------------------------------|---------------------------------------|
| Safety Earth Ground | Direct to facility ground or rod            | Green/yellow wire, meets IEC standards |
| Chassis Ground      | All metal enclosures tied together          | Star-grounded back to Safety Earth    |
| RF Shield Ground    | Shielding mesh tied to chassis              | Braided straps preferred              |
| Capacitor Bank Ground | Low-impedance path for pulse return      | Heavy gauge cable, copper bus bars    |

---

## ⚙️ Best Practice Layout (Text Diagram)

```
[ Earth Ground Rod ]
         |
     [ Main Panel Ground Bus ]
         |
  -----------------------------
  |            |              |
[ Chassis ] [ Shield Mesh ] [ Capacitor Bank Return ]
```

- **Important:** Keep power ground and signal ground isolated where applicable; use ground loops suppression techniques.

---

## ✅ Wire and Strap Specifications

- **Chassis Ground:** Minimum 8 AWG copper cable or equivalent strap.  
- **Capacitor Bank Return:** 2/0 AWG copper cable or 1" wide copper bar.  
- **RF Mesh Ground:** 1" wide tinned copper braid or multi-layer copper mesh wrap.

---

## ⚠️ Field Deployment Notes

- Ground rod length: Minimum 8 feet (2.4 meters) driven fully into earth.  
- Multiple rods spaced at least 6 feet (1.8 meters) apart for higher stability.  
- Avoid sharp bends in ground cables; gentle sweeps maintain low impedance.

---

## ✅ Summary

- Grounding is not optional—every IX-ZeroCell unit must be properly bonded.  
- Reduces fire, shock, and interference risks.  
- Detailed checks should be part of any system build checklist before power-on.

---


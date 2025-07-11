# IX-ZeroCell – Pulse Coil Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Document complete construction details for pulse coil array system used in IX-ZeroCell.

---

## ✅ Why It Matters

- Pulse coils form the core functional energy conversion system.  
- Must handle rapid, repeated magnetic pulses without overheating or failure.  
- Coil geometry directly affects output efficiency.

---

## ✅ Coil Specifications

| Attribute             | Value                          | Notes                          |
|----------------------|--------------------------------|--------------------------------|
| Coil Count           | 99 total                       | 1 coil per tube unit          |
| Core Material        | Air Core / Ferrite Hybrid      | Ferrite preferred for stability|
| Wire Gauge           | 12 AWG copper magnet wire      | Enamel-insulated               |
| Turns Per Coil       | 60–80 turns                    | Optimized for ~450V pulses     |
| Inductance (target)  | 1.5–2.5 mH per coil            | Verified per build             |
| Max Current Pulse    | 200–300A peak                  | Pulse duration: <10 ms         |
| Cooling              | Passive (air) + Optional forced air fans | Required beyond 30 min runtime |

---

## ✅ Physical Layout Example (Text Diagram)

```
|===|---|===|
| C | C | C |  <--- Coils mounted horizontally
| C | C | C |  <--- 99 total across multiple rows
| C | C | C |
|===|---|===|
```

- Each coil housed in PVC or ABS casing rated for 600V+.  
- Ensure coil spacings minimum **1 cm gap** to reduce inductive coupling losses.  

---

## ✅ Assembly Process Summary

1. Wind 12 AWG copper magnet wire onto form (PVC tube or ferrite rod).
2. Secure windings using high-temp epoxy resin.  
3. Label each coil with serial number and inductance value.  
4. Mount coil onto modular rail system inside main enclosure.  
5. Connect coil leads to capacitor bank using copper bus bars.  

---

## ✅ Example Real-World Coil Models

| Model               | Specs               | Vendor                |
|--------------------|--------------------|----------------------|
| Pulse Coil DIY Kit | 60 turns, 12 AWG, 2 mH | TeslaParts or similar|
| Premade Ferrite Coil | 1.8 mH, 250A rated  | Custom wind supplier |

---

## ⚠️ Warnings and Considerations

- Do not substitute with thinner wire—overheating risk increases exponentially.  
- Do not exceed pulse count beyond rated duty cycle without cooling.  
- Always verify coil inductance and resistance using an LCR meter before use.

---

## ✅ Summary

- 99 Pulse Coil Modules are the heartbeat of IX-ZeroCell.  
- Standardized construction ensures field-replaceability.  
- Quality control on every coil is non-negotiable: test, label, document each one.

---


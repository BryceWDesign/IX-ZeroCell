> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Control Panel Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Document physical control panel layout, user interface elements, and safety protocols for IX-ZeroCell operation.

---

## 💡 What This Module Does

- Provides human interface with system power and diagnostic controls.
- Manages critical safety interlocks and emergency shutdown triggers.
- Displays basic system health status using LEDs and voltmeters.

---

## ✅ Required Control Panel Components

| Component                 | Quantity | Function                            |
|--------------------------|----------|-------------------------------------|
| Emergency Stop Button    | 1        | Immediate system shutdown           |
| Keyed Power Switch       | 1        | Prevent unauthorized activation     |
| Pulse Fire Button        | 1        | Manually trigger pulse sequence     |
| Indicator LEDs (Green/Red) | 4–6    | System status, fault warnings       |
| Analog Voltmeters        | 2–4      | Capacitor bank voltage, coil bank voltage |
| Digital Display (Optional) | 1–2    | Optional pulse count or diagnostics |

---

## ✅ Panel Layout Diagram (Text Representation)

```
+-------------------------------------------------+
| [Keyed Power] [Emergency Stop]                  |
|                                                 |
| [Volt Meter 1]  [Volt Meter 2]                  |
|                                                 |
| [Green LED] [Red LED]                           |
|                                                 |
|              [ Pulse Fire Button ]              |
+-------------------------------------------------+
```

- All switches rated minimum **600V** insulation resistance.
- E-Stop wired to completely isolate capacitor bank and pulse coils.

---

## ✅ Wiring Notes

- Use shielded cables for all signal lines.
- Power lines from control panel to main bus:
  - **14 AWG minimum** for switch circuits.
  - Emergency Stop circuit wired through **latching relay** setup.

---

## ✅ Suggested Parts

| Component               | Model Example              | Vendor         |
|------------------------|---------------------------|----------------|
| Emergency Stop         | Schneider XB4BS844        | Mouser/Digi-Key|
| Keyed Switch           | IDEC HW1K-2Q4-R           | Allied Elec    |
| Indicator LEDs         | Any 12–24V DC panel mount | Local/Online   |
| Analog Voltmeter       | Yokogawa 250 Series       | Industrial supplier |

---

## ⚠️ Human Safety Considerations

- Control Panel must be mounted with at least **IP54** enclosure rating minimum.
- Labels must be engraved, not stickers, for long-term readability.
- Operator training: Only certified personnel should interact with panel.

---

## ✅ Summary

- The Control Panel is the operator’s direct control hub for IX-ZeroCell.
- Build quality = critical. Do not compromise on switch or indicator specs.
- Emergency Stop must work **independently** of software controls.

---

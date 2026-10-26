> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Manual Override Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Provide a hardware-based manual control layer for emergency shutoff, bypassing digital systems.

---

## 💡 Why Manual Override?

- Digital control systems can fail: firmware errors, sensor faults, UI lockups.
- Safety requires a guaranteed human-controlled fallback.
- Also simplifies field testing and troubleshooting.

---

## 🧱 Core Components

| Component               | Spec / Notes                               |
|-----------------------|---------------------------------------------|
| Emergency Stop Button  | 22mm Momentary Push-Lock (Industrial Standard) |
| High-Amp Mechanical Switch | DC-rated knife switch or rotary breaker  |
| Manual Pulse Trigger   | Keyed toggle switch + momentary pushbutton  |
| Status Indicator LEDs  | 12V/24V DC-rated, Red = Stop, Green = Active |
| Optional Potentiometer | Manual power level adjust override          |

---

## ⚙️ Control Flow Design (Text Diagram)

```
[ Power Source ] — [ Main Manual Switch ] — [ Pulse Control System ]
                            |
                [ Emergency Stop Button ]
                            |
                [ Manual Pulse Trigger ]
                            |
              [ Manual Power Adjust Pot ]
                            |
              [ Status LEDs and Indicators ]
```

---

## ✅ Wiring Best Practices

- Emergency Stop Button must directly cut power to pulse discharge systems, not rely on MCU or relay control.
- Use keyed switches to prevent unauthorized manual triggering.
- Label all switches clearly (English text + symbol graphics if possible).

---

## ✅ Enclosure Notes

- Mount manual override system in an external, clearly visible control box.
- Use industrial control panels or DIY metal enclosures with weather sealing for field units.
- Keep override controls separate from sensitive electronics to avoid accidental damage during emergencies.

---

## ⚠️ Build Notes

- Do not rely exclusively on manual override for regular use—it’s a fallback, not primary control.
- Test manual systems regularly under controlled conditions.
- Manual pulse triggering must include debounce logic if using digital systems in parallel (covered in software section).

---

## ✅ Summary

- Manual Override Module = critical safety layer.
- Includes emergency stop, manual pulse fire, and power level adjustment.
- Protects both operator and IX-ZeroCell hardware from unplanned behavior.

---

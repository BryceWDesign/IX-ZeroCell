> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Fuse Protection Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Provide short-circuit and overload protection for IX-ZeroCell systems using real-world electrical fuses.

---

## 💡 Why Fuses?

- Protects wiring and components from damage due to overload conditions.
- Essential in pulse capacitor discharge systems where accidental shorts can cause catastrophic damage.
- Required for compliance with electrical safety standards.

---

## 🧱 Recommended Fuse Types

| System Area            | Fuse Type          | Amperage Rating Notes                        |
|-----------------------|--------------------|---------------------------------------------|
| Main Power Input      | Blade Fuse (ATO/ATC) | 10A–100A depending on coil stack count     |
| Capacitor Banks       | High-Speed Ceramic Fuse | Pulse-rated, 400V–1000V DC, 30A–200A       |
| Control Circuitry     | Glass Cartridge Fuse | 500mA–3A depending on MCU and relay draw    |
| Fan & Pump Systems    | Standard Blade Fuse | 5A–10A                                       |

---

## ⚙️ Placement Guide

1️⃣ **Main Power Fuse:**
- Between battery bank (if present) and pulse driver circuit.
- Close to power source to minimize unprotected wiring length.

2️⃣ **Capacitor Bank Fuses:**
- Inline on each capacitor series string.
- Fuse rating = slightly above max expected pulse current.

3️⃣ **Control Circuit Fuses:**
- On low-voltage rail feeding MCU, relay drivers, fan controllers.

4️⃣ **Fan/Pump System Fuses:**
- Inline on dedicated 12V or 24V supply rail.

---

## 🛠️ Basic Protection Diagram (Text Only)

```
[ Power Source ] — [ Main Fuse ] — [ Pulse Circuit ]
                           |
                 [ Cap Bank Fuses ]
                           |
                   [ Load System ]
                           |
                [ Control Fuses ]
                           |
               [ Fan/Pump Fuses ]
```

---

## ✅ Fuse Selection Notes

- **Always choose fuse voltage rating higher than system voltage.**
- Pulse discharge fuses must be rated for DC and fast response time.
- Replace all fuses after serious fault event even if they appear intact.

---

## ⚠️ Build Notes

- Use dedicated fuse blocks with secure mounts.
- Label each fuse location for serviceability.
- Keep spare fuses on hand—build kits should include 2–3 spares per type.

---

## ✅ Summary

- Fuses are a non-optional safety layer in IX-ZeroCell.
- Protects user and system hardware from overload and fault conditions.
- Must be integrated into all hardware builds, especially capacitor-heavy modules.

---

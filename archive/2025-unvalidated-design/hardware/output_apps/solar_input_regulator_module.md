> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Solar Input Regulator Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Safely regulate voltage/current from a solar panel into IX-ZeroCell capacitor banks.

---

## ☀️ Why This Module Exists

Solar panels output variable voltage. Unregulated input can **overcharge** or **damage** the capacitor bank.

This module stabilizes:

- Voltage to **5.0V or user-defined limit**
- Current limit to prevent surge
- Optionally handles **MPPT** (Maximum Power Point Tracking)

---

## 🧱 Core Components

| Component             | Recommended Part     | Notes                             |
|----------------------|---------------------|-----------------------------------|
| DC-DC Buck Converter | LM2596 or MP1584    | Adjustable down to 5.0V
| TVS Diode            | 5.0V Clamping       | Overvoltage protection
| Solar Panel          | 6V–24V nominal      | Up to ~20W recommended
| Optional Controller  | CN3791 / BQ25504    | For MPPT regulation

---

## 🔌 Wiring Example

```txt
Solar Panel (+) --> Buck Converter VIN (+)
Solar Panel (-) --> Buck Converter GND
Buck Converter VOUT (+) --> IX-ZeroCell Cap Bank Input (+)
Buck Converter GND --> IX-ZeroCell Cap Bank Input (-)
```

---

## 🛠️ Configuration Notes

- **Pre-set voltage output** using onboard potentiometer on buck converter
- Target 5.0V–5.2V for most IX-ZeroCell builds
- Limit solar input wattage — excess power is wasted as heat if too large
- Suggested **6V 10W–20W panel** for field testing

---

## ⚙️ MPPT (Advanced Option)

For maximum efficiency:

- CN3791 Lithium Solar Charger IC
- BQ25504 Ultra-Low Power Energy Harvester
- These adjust solar panel load dynamically
- Adds **complexity** but improves charge rate

---

## 🧪 Performance Notes

- With LM2596: ~75–85% conversion efficiency
- With MPPT controller: 90%+ possible
- Cap bank charges in **~3–12 hours** depending on sun conditions

---

## ⚠️ Safety Considerations

- Always include **overvoltage protection diode**
- Confirm no reverse current from IX-ZeroCell back into solar panel
- Mount solar panel with proper UV/weather protection if outdoor

---

## ✅ Summary

- IX-ZeroCell supports solar charging via regulated input
- Easy integration using off-the-shelf buck converters
- Optional advanced MPPT circuitry for those who need it

---

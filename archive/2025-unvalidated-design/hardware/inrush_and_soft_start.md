> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Inrush Protection and Soft-Start Logic

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Prevent damage from supercap discharge surge by implementing current limiter and staged startup

---

## ⚡ Why Inrush Protection?

- Supercaps dump **huge surge current** at turn-on
- This can:
  - Blow out traces
  - Trip boost converters
  - Damage microcontrollers or sensitive loads
  - Trigger false brownout resets

---

## ✅ Goal

- Allow smooth ramp-up from VSTOR to MT3608 VIN
- Limit inrush to <250mA peak
- Add optional **manual bypass or auto relay shorting** after delay

---

## 🧰 Design 1: NTC Thermistor + Delay Short

### Components:

- **NTC thermistor**: limits current at cold start
- **P-MOSFET** + **delay RC**: shorts thermistor after delay to improve efficiency

```txt
VSTOR ──NTC──┬── VIN (MT3608)
             │
           [P-MOSFET]
             │
            GND (via RC delay)
```

---

### Example Values:

| Component     | Value            | Purpose                       |
|---------------|------------------|-------------------------------|
| NTC Thermistor| 10Ω @ 25°C       | Limits inrush to ~200mA
| P-MOSFET      | IRF9540 or similar| Bypasses NTC after delay
| R_delay       | 1MΩ              | Controls timing
| C_delay       | 10µF             | Controls gate charge slope

> RC = 1M × 10µF = ~10s delay before MOSFET activates

---

## 🧰 Design 2: Constant Current Source (Advanced)

- Use op-amp-based constant current limiter (e.g. LM317 CC config)
- More precise, but higher part count and complexity

---

## 🔌 PCB Notes

- Route VIN trace wide (≥1mm)
- Place NTC physically close to VSTOR node
- Gate pull-down on P-MOSFET to prevent latch-up
- C_delay should be ceramic, X7R-rated

---

## 🔄 Optional: Manual Soft Start

Add **tactile push-button** to charge MT3608 input rail slowly.
Good for debug or non-auto boot modes.

---

## ✅ Summary

- Supercaps need controlled discharge into boost converters
- NTC thermistor + delayed MOSFET bypass = efficient and safe
- Optional push-button or advanced op-amp current limiter
- Prevents damage to downstream electronics and erratic boost behavior

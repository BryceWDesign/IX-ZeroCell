> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Thermal & Overcurrent Protection

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Define safe electrical and thermal protection mechanisms to prevent overloads, overheating, or dangerous discharge from the IX-ZeroCell system

---

## 🔥 Protection Objectives

- Stop **short circuits** from damaging boost converters or caps
- Prevent **thermal runaway** from overcurrent drain
- Avoid **deep discharge** of supercaps
- Protect attached loads (sensors, MCUs, radios)

---

## ⚡ Current Limiting – Passive

### 🔹 Series Polyfuse (Resettable Fuse)

- **Type:** PPTC (e.g. MF-R050, MF-R100, MF-R200)
- **Trip Current:** Choose based on output target

| Fuse Model | Hold Current | Trip Current | Resistance (cold) |
|------------|--------------|--------------|-------------------|
| MF-R050    | 0.5 A        | ~1.0 A       | ~0.3Ω
| MF-R100    | 1.0 A        | ~1.9 A       | ~0.2Ω
| MF-R200    | 2.0 A        | ~3.8 A       | ~0.12Ω

> Place between boost output and USB/JST header
> Auto-recovers after cooling (~15s)

---

### 🔹 Output Resistor (Soft Current Clamp)

- Add a **low-value resistor (e.g. 0.22Ω – 1Ω)** in series to limit peak inrush
- Also useful for current sensing via MCU ADC

---

## 🧯 Thermal Monitoring

### 🔸 NTC Thermistor Placement

- Type: 10kΩ @ 25°C NTC
- Glue to MT3608 or cap bank with thermal epoxy
- Connect in divider:

```txt
VCC — 10kΩ — A0 — Thermistor — GND
```

- ADC monitors voltage drop → calculate temp
- Shutdown boost if temp exceeds safe range (e.g. >70°C)

### 🔸 Passive Ventilation

- Use **vent holes** above supercap bank if enclosed
- Place copper pours around heat-generating parts

---

## 🚨 Output Kill Switch (Active)

If MCU is present (see `/hardware/mcu_interface_logic.md`):

- Connect GPIO to P-channel MOSFET or load switch
- Cut output if:
  - Cap voltage < 2.8V
  - Cap temp > 70°C
  - Load current > setpoint

### MOSFET Example Circuit

```txt
Boost Vout —> P-MOSFET —> USB V+
                    ^
                  GPIO (pull LOW to enable)
```

---

## 🔄 Short Circuit Detection (Advanced)

- Optional shunt resistor + op-amp comparator
- MCU senses high dI/dt (current spike) → disable load

### Simpler Alternative

- Use **TVS diode** + **polyfuse** to catch spikes
- Add **0.1Ω shunt** and monitor via ADC for current

---

## 🧠 Best Practices Summary

| Method               | Mandatory | Notes                         |
|----------------------|-----------|-------------------------------|
| Polyfuse             | ✅ Yes    | Always include at output
| NTC Thermistor       | Optional  | If boost runs warm
| Output resistor      | ✅ Yes    | Controls surge and sense
| Active cutoff (MCU)  | Optional  | Great if adding smarts
| TVS diode            | ✅ Yes    | Prevents voltage overshoot

---

## ✅ Summary

- Every output rail is protected from shorts and excessive load
- Polyfuses + series resistors handle most passive cases
- Optional MCU logic gives smarter protection
- Thermal monitoring adds robustness for long-life reliability
- All components are low-cost, widely available, and non-proprietary

> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Thermal Harvesting Block (TEGs)

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Harvest ambient or direct thermal differential using TEG modules and safely feed regulated voltage into MPPT

---

## 🌡️ What Are TEGs?

**Thermoelectric Generators** produce voltage when one side is hotter than the other.

- Based on the **Seebeck effect**
- Output is **low voltage, moderate current**
- Silent, solid-state, long lifespan

---

## 🔋 Typical Output Range

| ΔT (Temp Difference) | Output (per TEG) |
|-----------------------|------------------|
| 20°C                  | ~150mV           |
| 50°C                  | ~400mV           |
| 100°C                 | ~0.8–1.2V        |

Multiple TEGs can be wired **in series** to raise voltage, or **in parallel** to increase current.

---

## 🧩 Recommended TEG Modules

| Part Number     | Vendor        | Specs                     |
|------------------|---------------|----------------------------|
| TEC1-12706       | Adafruit, eBay | 4cm x 4cm, 6A peak         |
| CP2015Z          | AliExpress    | 1.5cm, ultra-thin          |

---

## 🔧 Wiring Configuration

### Option 1 – Series (preferred for MPPT)

- Increases voltage
- Needed to exceed MPPT cold-start threshold (~330mV)

```txt
[TEG1]+ → [TEG2]+ → [TEG3]+ → MPPT VIN_DC
[TEG1]- [TEG2]- [TEG3]- → MPPT GND
```

> Minimum: **3x TEGs in series** for startup reliability

---

### Option 2 – Parallel (if high ΔT)

- Increases current
- Requires voltage already above ~330mV
- Better for post-boot operation

```txt
[TEG1]+
[TEG2]+ → MPPT VIN_DC
[TEG3]+

[TEG1]-
[TEG2]- → MPPT GND
[TEG3]-
```

---

## 🔒 Voltage Protection

- TEGs usually output <2V but clamp anyway
- Add **Schottky diode (e.g. 1N5819)** between TEG and MPPT to block reverse current
- Add 100µF electrolytic + 1µF ceramic in parallel at MPPT input to smooth TEG ripple

---

## 🧪 Mounting Tips

- Attach hot side to heatsink or warm pipe
- Cool side faces ambient or fan
- Use **thermal paste** or **thermal pad** to ensure full contact
- Avoid temps >125°C to prevent long-term damage

---

## 🛠️ PCB/Inline Design Notes

- Route TEG input through diode, cap, and into **Node A**
- Label all connectors clearly — TEGs are polarity sensitive
- Inline thermal break (thermal switch or PTC) optional if overheat risk exists

---

## 🔁 Integration with MPPT

- All TEG output routes to **Node A**
- Cold-start is handled if combined series voltage ≥ 330mV
- Boost converter handles ripple via capacitor network

---

## ✅ Summary

- Series configuration of 3+ TEGs ideal for startup
- Always use Schottky + smoothing caps
- Feed directly to Node A
- Ideal for warm surfaces, server rooms, engines, or skin-worn devices

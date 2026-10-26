> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Supercapacitor Array Design

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Define the zero-battery energy storage subsystem using low-ESR supercapacitors, with proper balancing, protection, and thermal spacing

---

## 🧠 Why Supercaps?

- No chemical degradation
- High cycle life (>500,000)
- Rapid charge/discharge support
- Safer than lithium-ion in most field conditions
- Great fit for zero-battery, energy-harvesting systems

---

## 🔋 Recommended Supercaps

| Cap Type    | Capacitance | Voltage | ESR     | Notes                      |
|-------------|--------------|----------|---------|----------------------------|
| EDLC (Radial)| 10F – 100F   | 2.7V     | <50mΩ   | Panasonic, Maxwell, AVX
| Ultracap (Coin) | 0.1F – 1F | 5.5V     | ~1Ω     | Compact, low energy apps

> Choose caps with **low ESR** and **long rated life** at 65°C+

---

## 🧮 Series Configuration

Because each cap is rated ~2.7V, you'll need to **series-connect** to store usable energy for 3.3–5V output.

### Minimum Working Configuration

- **2x 10F caps in series = 5.4V, 5F equivalent**
- Capacitance halves in series:
  \( C_{total} = \frac{C}{n} \)

---

## ⚖️ Balancing Between Series Caps

Unbalanced caps can overvoltage and fail.

### Passive Balancing (Simple)

- Resistors across each cap
- Typical: **1kΩ – 10kΩ, 1/4W**

```txt
[Cap1]+ — R1 — GND
[Cap2]+ — R2 — GND
```

### Active Balancing (Optional)

- Balancing ICs (e.g. LTC3350)
- Not needed unless >4 caps or ultra-precision required

---

## 🔁 Diode Bypass (Optional)

- Add **Schottky diodes (SS14)** in **reverse parallel** across each cap
- Prevents sudden voltage reversals from damaging cells

---

## 🌡️ Thermal Management

- Space caps at least **3mm apart**
- Add **thermal vias** under cap pads if on PCB
- Use **graphite sheet** under array for lateral heat spread

---

## 📐 Real-World Array Size

| Cap Count | Cap Value | Total Cap | Voltage | Footprint         |
|-----------|------------|------------|---------|-------------------|
| 2         | 10F        | 5F         | 5.4V    | ~30mm x 20mm      |
| 3         | 22F        | 7.3F       | 8.1V    | ~50mm x 20mm      |
| 4         | 25F        | 6.25F      | 10.8V   | ~60mm x 25mm (PCB or stacked)

> Most IX-ZeroCell applications will do well with a **2-cap 5.4V / 5F** bank.

---

## 🧪 Mounting Options

1. **Inline on PCB** (horizontal radial)
2. **Stacked via headers** (if height available)
3. **External via JST or Molex** (removable packs)

> Caps should be near BQ25570 output and boost converter input

---

## ✅ Summary

- Use **2+ supercaps in series** for voltage range
- Add **balancing resistors** to each stage
- Use **low-ESR, long-life parts only**
- Allow for **thermal spacing** and optional bypass diodes

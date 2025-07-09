# Wiring Topology – IX-ZeroCell

This document outlines the recommended wiring configurations for the coil array, harvesting inputs, and supercapacitor storage system in IX-ZeroCell. It is designed to balance output stability, safety, and harvesting efficiency.

---

## 🔗 Coil Array Configuration

### 🔄 Default: Series Configuration

- All 99 coils are connected in **pure series**, forming a single long wire.
- This maximizes voltage output under kinetic induction.
- Peak output can exceed 12V during strong motion input.

#### Series Wiring Diagram (ASCII)

```plaintext
[Coil1]—[Coil2]—[Coil3]—...—[Coil99] → to Boost Converter Input +
                                     |
                                     → to Ground (Input -)
```

- Total resistance: ~207.9Ω
- Recommended for moderate-to-strong kinetic movement scenarios

---

### 🧩 Optional: Segmented Coil Banks

If power draw needs to be split or voltage must be regulated per module:

- Create **three groups of 33 coils each**
- Wire each group in series internally
- Combine outputs in **parallel** for a lower voltage / higher current profile

#### Segmented Bank Topology

```plaintext
[Group A: Coil1–33] →|
                    |→ Merge at boost converter input
[Group B: Coil34–66]→|
                    |→ Merge at input ground
[Group C: Coil67–99]→|
```

- Final output: ~4.5V under load, higher current, faster supercap charging
- Use **diodes or low-resistance FETs** to prevent backflow between banks

---

## 🔋 Supercapacitor Bank

- Three **2.7V 1000F** supercapacitors
- Connected as: **(2S1P)** — Two in series, third in parallel across one branch
- Balanced using 100Ω resistors + TVS diodes

#### Cap Wiring Diagram

```plaintext
[Cap1: +]───┐
            ├───[To Boost Converter IN+]
[Cap2: +]───┘
[Cap1: -]───┬───[To Boost Converter GND]
[Cap2: -]───┘
```

- Add 2W, 100Ω balancing resistors between each series node
- Include 5.1V Zener or TVS diode across each cap for overvoltage protection

---

## 🧠 Signal Flow

```
[Harvest Inputs] → [MPPT Circuit] → [Supercap Bank] → [Boost Converter] → [USB/DC Out]
```

- Use shielded wire on RF harvesting inputs to avoid noise pollution
- Keep all high-current paths under 6" in length where possible
- Twist paired wires for inductive paths to reduce EMI

---

## ⚠️ Safety Tips

- Always discharge caps before rewiring
- Use silicon grommets or heat-shrink at every connection point
- Triple check polarity before applying boost converter

---

*Topology authored by Bryce Wooster – IX-ZeroCell, July 2025.*


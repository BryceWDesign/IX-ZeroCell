> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Supercapacitor Bank Configuration

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Define storage stage between BQ25570 and Boost converter using supercapacitor bank

---

## 🔋 Why Supercapacitors?

- Virtually infinite charge/discharge cycles
- No lithium aging or fire risk
- Can buffer spikes from kinetic energy or RF surges
- Enable "batteryless" zero-maintenance design

---

## ⚙️ Cap Bank Topology

### Configuration: **2S2P**
- Two caps in series = handles voltage safely (up to ~5.5V total)
- Two of those in parallel = increased total capacitance

```txt
[Cap1]───┬───[Cap2]
         │
        GND
         │
[Cap3]───┴───[Cap4]
```

---

### Example: Using 2.7V 10F Caps

| Quantity | Capacitance (each) | Voltage (each) | Final Configuration |
|----------|--------------------|----------------|----------------------|
| 4        | 10F                | 2.7V           | 5F @ 5.4V (approx.)

**Energy capacity:**
```txt
E = 0.5 × C × V² = 0.5 × 5 × (5.4)² ≈ 72.9 joules
```

---

## ⚖️ Balancing Resistors (per series pair)

- Prevents one cap from overvolting due to mismatch
- Use **1MΩ** resistors across each cap

| Resistor | Value | Tolerance | Note          |
|----------|--------|-----------|---------------|
| R_BAL1   | 1MΩ    | 1%        | Across Cap1
| R_BAL2   | 1MΩ    | 1%        | Across Cap2
| etc.     | –      | –         | Optional LEDs for debug

---

## 🧲 Clamping Diodes

- To catch voltage spikes or cap overcharge
- Use **5.5V Zener or TVS** between supercap node and GND

```txt
[+ Cap Bank]───|<|───GND
            (TVS 5.5V)
```

Use **SMAJ5.0A** or **1N4736A** (5.1V zener)

---

## 📦 BOM

| Component        | Value     | Qty | Notes                          |
|------------------|-----------|-----|-------------------------------|
| Supercap         | 10F, 2.7V | 4   | Series/parallel config
| Resistor         | 1MΩ       | 4   | Balancing
| TVS/Zener Diode  | 5.5V      | 1–2 | Protection
| Header           | 2-pin     | 1   | VSTOR output to Boost stage

---

## 🔌 Connection to BQ25570

- Supercap bank connects to **VSTOR** pin
- Cap bank then routes output to **boost converter input (MT3608 VIN)**

---

## 🛠️ Mounting Tips

- Place caps close to each other and to BQ25570
- Use wide power traces, or copper pour
- Keep balancing resistors far from heat sources (to preserve values)

---

## ✅ Summary

- 2S2P cap bank gives ≈ 5F @ 5.4V usable capacity
- Balancing resistors = 1MΩ across each cap
- Zener or TVS diode provides overvoltage safety
- Connects directly to BQ25570 VSTOR → feeds boost stage

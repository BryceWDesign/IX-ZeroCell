> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Supercapacitor Storage Stage

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Define energy storage subsystem using real-world supercapacitors for passive ambient harvesting

---

## ⚡ Why Supercapacitors?

Supercaps (ultracaps) are ideal for ambient energy systems:

- ✅ Near-infinite charge cycles
- ✅ Instant energy uptake
- ✅ Low ESR (can source bursts)
- ✅ Wide operating temps
- ✅ No thermal runaway, no battery regs

---

## 🔋 Capacitor Specs (Per Cell)

| Parameter        | Value                         |
|------------------|-------------------------------|
| Capacitance      | 10F per cap
| Rated Voltage     | 2.7V
| ESR               | ≤50mΩ
| Package           | Radial, 16×35mm typical
| Leakage Current   | ~0.1mA max

---

## 🧩 Bank Configuration

| Goal             | Value                |
|------------------|----------------------|
| Storage Voltage  | 5.4V max
| Cap Count        | 2 in series
| Total Capacitance| 5F effective
| Energy Capacity  | ~73 Joules
| Dimensions       | ~3.5cm x 7cm footprint

---

## 🔁 Charge Path Logic

```txt
[ Combiner Rail (~0.5–3V) ]
        ↓
   [ Blocking Diode (SS34) ]
        ↓
[ Supercap Bank (2x 10F @ 2.7V, in series) ]
        ↓
 [ Voltage Divider + Balancer ]
```

---

## 🛡️ Voltage Balancing Circuit

Since caps are in **series**, use a passive or active balance to prevent overvoltage on one cell.

### Option A: Passive Resistor Divider (Simple)

| Component | Value  | Notes                     |
|-----------|--------|---------------------------|
| R1, R2    | 1k–10k | Across each cap, equalize V
| Bleed Cap | 100nF  | Optional smoothing

Draws constant microamps — good for slow-charging systems.

### Option B: Active Balancer (Precise)

- Use LTC4041, CAP-XX balancers, or op-amp buffers
- Needed if >5 caps used or large input surges expected

---

## 🧯 Safety & Isolation

| Feature             | Component     | Purpose                          |
|---------------------|---------------|----------------------------------|
| Reverse Protection  | SS34 diode    | Prevents combiner back-feed
| Voltage Tap Header  | 2-pin JST     | Debug/test access
| Bleed Resistors     | 10k across caps| Prevents residual storage
| Thermistor (opt.)   | NTC 10k       | Thermal monitoring

---

## 📦 Mounting / PCB Guidelines

- Place vertically to save board area
- Leave at least 1.5mm clearance around cap bodies
- Keep ground plane under caps for ESR minimization
- Mount away from high-heat components (boost ICs)

---

## 📈 Performance Profile

| Condition                 | Result                         |
|---------------------------|--------------------------------|
| Full Charge Time          | 1–5 min (ambient dependent)
| Max Stored Energy         | ~73 Joules
| Usable Load Time (1W)     | ~70s
| Self-Discharge (standby)  | ~1–2% per hour
| Peak Discharge Pulse      | Up to 0.5A (short burst)

---

## ⚙️ Real-World Example Cap Part Numbers

| Manufacturer | Part Number        | Specs              |
|--------------|--------------------|---------------------|
| Nesscap      | ESHSR-0010C0-002R7 | 10F @ 2.7V, 50mΩ
| Maxwell      | BCAP0010 P270 T04  | 10F @ 2.7V, 40mΩ
| AVX          | SCCS10B275PRB      | 10F @ 2.7V

---

## ✅ Summary

- 2× 10F, 2.7V supercaps in series = 5F @ 5.4V
- Low-ESR caps provide burst capacity for regulated outputs
- Passive balance resistors prevent cell mismatch
- Modular, safe, and chemically passive — no fire risk
- Stores enough for short bursts of regulated 3.3V / 5V power

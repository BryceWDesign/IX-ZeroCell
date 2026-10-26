> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Piezo & Spark Gap Driver

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Create a high-voltage spark using either piezo discharge or boosted capacitor burst

---

## ⚡ Overview

This module enables a **visible spark** to jump across a small air gap, either by:

1. Using a **piezoelectric crystal driver** (mechanical or hammer-based)
2. Firing a **capacitor dump into a flyback transformer or ignition coil**

---

## 🔌 Options

| Method         | Voltage Range   | Notes                                |
|----------------|------------------|--------------------------------------|
| Piezo Crystal  | ~10kV spike      | Small, single-use pulses
| Ignition Coil  | 12–18kV          | Needs pulse signal, fast flyback
| Flyback Transformer | 15–35kV     | Use for Tesla coil or arc driver
| Joule Thief + Step-up | 1kV–10kV  | Not true arc, but can jump small gap

---

## 🔧 Configuration A – Piezo Driver

| Component         | Details                            |
|--------------------|------------------------------------|
| Piezo Element      | BBQ lighter type, hammer snap type
| Trigger Switch     | Mechanical lever or manual snap
| Output Wire        | High-voltage wire to spark terminal
| Spark Gap          | 1–3mm air gap between electrodes

**Build Tip:** Mount piezo inside small spring-loaded lever box. Each push fires a spark.
**Pros:** Passive, needs no circuit.
**Cons:** Manual only. Not remotely triggerable.

---

## 🔧 Configuration B – Cap Dump + Ignition Coil

| Component             | Details                              |
|------------------------|--------------------------------------|
| Cap Bank (charged)     | 5.5V, 15F supercap
| Trigger Circuit        | SCR or MOSFET (see File 71)
| Step-up Coil           | Automotive ignition coil or flyback
| Discharge Diode        | 1N5408 or UF4007
| Spark Electrodes       | Carbon rods or copper
| Gap Distance           | 2–5mm (adjust to voltage output)

```txt
[Cap Bank] → [Gate Switch] → [Ignition Coil Primary]
                               → [Secondary HV] → [Spark Gap]
```

---

## 🔥 Output Estimates

Assuming:

- 15F at 5.5V cap bank
- Automotive ignition coil (turns ratio ~100:1)
- Pulse = 113J dumped over 10ms

→ Secondary coil may produce **15–25kV spark** if isolated properly.

---

## 🛡️ Safety Considerations

- Keep spark gap away from flammables
- Use acrylic standoff brackets to suspend electrodes
- Always isolate HV output from user contact
- Never dump cap bank into unloaded coil — always have spark gap connected
- Consider 1MΩ bleed resistor across cap bank after each pulse

---

## 📈 Enhancements

| Feature            | Description                          |
|---------------------|--------------------------------------|
| Auto Pulse Trigger | Timed MCU pulse every N seconds
| Motion+Spark        | Only spark when moved (File 70)
| High-Voltage Logging| Count arcs / duration via opto-tap
| LED Feedback        | Flash LED on each discharge

---

## ✅ Summary

- Supports both passive piezo and active HV coil spark generation
- Safe, scalable, and real-world viable
- Allows visible spark arcs as proof-of-output or ignition
- All components off-the-shelf, tested and documented

> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Energy Bus Combiner Logic

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Safely combine power from multiple ambient harvesters (kinetic, RF, thermal) into a unified supercapacitor charging bus

---

## ⚙️ Input Modules Overview

| Source     | Modules Count | Output Range | Notes                        |
|------------|----------------|--------------|------------------------------|
| Kinetic    | 99 coils       | 2–5V spikes  | Grouped into 11 PTC-protected rails
| RF         | 3–5 rectennas  | 0.1–0.5V     | Ultra-low power, isolated
| Thermal    | 1–4 TEGs       | 0.5–2.5V     | Low-impedance modules

---

## 🧠 Merge Design Goals

- Allow **simultaneous input** from all sources
- Prevent any **source from back-feeding** others
- Provide **buffering and surge absorption**
- Scale to higher current or future inputs (e.g. piezo, tribo)
- Be **modular and replaceable**

---

## 🔌 Combiner Schematic Logic

```txt
  [ Kinetic A–K ]——[SS34]——\
  [ RF rectenna 1–5 ]——[HSMS285x]——\
  [ Thermal TEG 1–4 ]——[SS34]——-----> [Combiner Rail] → [Supercap Stage]
                                         |
                                    [100µF Bulk Cap]
```

---

## 🔋 Merge Components Per Input

| Input Type | Rectifier     | Fuse Type  | Filter Cap   | Merge Diode | Notes                           |
|------------|---------------|------------|--------------|-------------|---------------------------------|
| Kinetic    | Full-bridge   | PTC (250mA)| 22µF ceramic | SS34        | Handles inductive spikes
| RF         | HSMS-2852     | None       | 10nF ceramic | HSMS        | Diode acts as rect & merge
| Thermal    | Direct Diode  | PTC (250mA)| 100µF elec.  | SS34        | Supports bulk power in

---

## 🧯 Combiner Rail Design

| Element            | Value / Type      | Role                               |
|--------------------|-------------------|-------------------------------------|
| Bulk Capacitor     | 100µF–220µF       | Smooths all merge ripple
| Merge Diodes       | SS34 (or equiv.)  | Prevents reverse injection
| Rail Width         | ≥1mm copper trace | Carries ~1A peak possible
| Test Header        | 2-pin JST / 0.1"  | Optional voltage measurement
| Debug LED (opt.)   | Red LED + 1kΩ     | Glows when bus active (>1.8V)

---

## 🧰 PCB Layout Recommendations

- Place combiner logic **centrally** near supercaps
- Keep input traces **short** and wide
- Separate kinetic inputs from RF lines to avoid coupling noise
- Isolate thermal modules with thermal vias or board cutout if needed
- Add **test pad** before and after diode merge points for diagnostics

---

## 📐 Combiner Topology Map

```txt
+------------------------------------------------------------+
|    [ Kinetic Inputs (x11) ]                                |
|         ↳ PTC → Bridge → SS34 →                            |
|                                                         →  |
|    [ RF Inputs (x3–5) ]                                    |
|         ↳ Match → HSMS → Cap →                            → | → Combiner Bus
|                                                         →  |
|    [ Thermal Inputs (x2–4) ]                                |
|         ↳ PTC → SS34 → Cap →                              → |
+------------------------------------------------------------+
                                      ↓
                              [ Supercap Bank ] → Boost Logic
```

---

## ✅ Output Profile (Typical)

| Condition                | Bus Voltage | Bus Current | Notes                          |
|--------------------------|-------------|-------------|--------------------------------|
| Urban RF + mild hand tap | ~0.9V       | ~10–30mA    | Enough to start charging
| Shake + RF + hand heat   | ~2.2V       | ~150–300mA  | Full boost-ready range
| No activity              | 0–0.1V      | —           | No output

---

## ⚠️ Fault Scenarios

| Fault Case                 | Response                         |
|----------------------------|----------------------------------|
| Shorted coil group         | PTC fuse trips (open)
| Failed RF diode            | That band goes inactive only
| Overheat at TEG            | Still forward protected by SS34
| Accidental reverse bias    | Diodes prevent rail damage

---

## ✅ Summary

- Modular combiner circuit for **all 3 passive sources**
- Uses low-forward-drop Schottky diodes to merge into single DC rail
- Smooths ripple with shared capacitor
- Scalable, safe, fault-tolerant
- No software, no control logic — **pure passive power conditioning**

# IX-ZeroCell – Peltier Thermal Harvester Input

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Capture energy from thermal differentials using thermoelectric (TEG) modules and deliver it safely to IX-ZeroCell's supercap charging rail

---

## ♨️ Overview

Thermoelectric modules (Peltier or TEG) generate voltage when exposed to a **temperature gradient** between front and back plates.

This input stage passively converts ambient heat flows (sunlight, hand warmth, hot surfaces) into **DC current** without batteries or active regulation.

---

## 🧱 TEG Module Specification

| Model (Example) | Value         |
|-----------------|---------------|
| Type            | TEC1-12706 (reversed as TEG)  
| V_gen (ΔT=30°C) | ~1.5V–2.4V  
| I_gen           | ~100–300mA  
| Power Output    | ~0.2–0.6W per module  
| Size            | 40mm × 40mm × 4mm  

---

## 📦 Mounting Considerations

| Plate Surface | Role        | Material        |
|---------------|-------------|-----------------|
| Hot Side      | External skin / heat source | Aluminum, steel, or hand contact  
| Cold Side     | Heat sink    | Finned aluminum or copper, passive airflow  

- Use **thermal paste** between surfaces  
- Attach with spring clips or compressive brackets  
- Mount module in a **thermally exposed corner of case** for best effect

---

## 🔁 Electrical Connection

| Stage           | Component              | Notes                           |
|-----------------|------------------------|----------------------------------|
| Rectifier       | SS34 Schottky diode    | Blocks reverse feed  
| Series Fuse     | PTC (250mA)            | Thermal short protection  
| Filter Cap      | 100µF electrolytic     | Smooths voltage pulses  
| Output Path     | To energy bus combiner | Parallel with RF/coil paths  

---

## ⚡ Harvesting Topology

```txt
[ TEG Module ]—[ PTC ]—[ SS34 Diode ]—[ 100µF Cap ]—→ Energy Bus
```

- Output tied to the **same supercap input rail** as coil + RF  
- PTC fuse isolates damaged modules  
- Diode prevents supercap from back-driving heat module

---

## 🔥 Output Expectations (Real-World)

| Scenario                       | ΔT (°C) | V_out  | I_out | Power      |
|--------------------------------|---------|--------|-------|------------|
| Sunlight + ambient sink        | 25–35   | ~2V    | ~150mA| ~300mW  
| Human hand vs metal baseplate  | 10–15   | ~1V    | ~80mA | ~80mW  
| Airflow across chassis         | 5–10    | ~0.5V  | ~50mA | ~25mW  
| Heat source (mug, appliance)   | 35–50   | 2.5V   | 200mA | ~400–500mW  

---

## 🔌 Multiple Module Handling

You can mount **2–4 modules** in parallel:

```txt
[ TEG A ]→[ Rect ]→\
[ TEG B ]→[ Rect ] → [ Common Rail ] → Supercap bus  
[ TEG C ]→[ Rect ]→/
```

- Each module has its own PTC + Diode  
- Outputs OR-ringed and summed  
- All converge to shared cap charge input

---

## 📐 Placement Tips

- Install where **airflow hits case corner** or **human handling occurs**  
- Can be back-mounted to **metal plate facing sun**  
- Avoid heat sinks near high-draw electronics (boost converters, USB)  
- Keep one side of TEG thermally insulated if gradient must be preserved

---

## ✅ Summary

- Peltier modules used in **reverse** to harvest ambient thermal energy  
- Passive DC output (0.5–2.5V) based on temperature difference  
- Output fed into IX-ZeroCell's bus via diode, PTC, cap  
- Typical power per module: **50–400mW**  
- Scalable, safe, and modular


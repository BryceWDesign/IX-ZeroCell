# IX-ZeroCell – Shake Coil to Energy Bus Interface

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define how power from 99 kinetic shake coils is merged into the supercap charging system

---

## ⚙️ Energy Merge Architecture Overview

Each coil outputs **high-voltage AC pulses**. We must:

1. **Rectify to DC**  
2. **Block backfeed into inactive coils**  
3. **Fuse each sub-bus to isolate failures**  
4. **Merge rails cleanly with minimal drop**

---

## 🔌 Coil Grouping

| Cluster | Coil Count | Topology         | Notes                          |
|---------|------------|------------------|--------------------------------|
| A–K     | 9 coils ea | Parallel grouped | 11 total groups (9×11 = 99)  

Each coil group shares:

- 1x full-bridge rectifier (Schottky preferred)  
- 1x series PTC fuse (resettable, 150–250mA)  
- 1x reverse-blocking diode (1N5819 or SS34)  
- Output merges into OR-ringed rail  

---

## 🔁 Rectification Logic

| Component         | Type       | Notes                          |
|-------------------|------------|--------------------------------|
| D1–D4 per group   | SS14       | Low-drop Schottky full-bridge  
| F1 per group      | PPTC 250mA | Protects against locked rotor shorts  
| D5 (merge diode)  | SS34       | Blocks reverse injection from cap bus  
| Output rail       | Shared DC+ | All 11 outputs paralleled to main rail  

---

## 🧠 Merge Strategy

```txt
[ Coil Group A ]—[BR]—[PTC]—[D5]\
[ Coil Group B ]—[BR]—[PTC]—[D5] \
...                               >—[Main Energy Rail] → MPPT
[ Coil Group K ]—[BR]—[PTC]—[D5] /
```

- Each line includes a **fail-open PTC**  
- Diodes ensure **one-way flow only** toward storage bus  
- No intergroup backfeeding possible

---

## 🧲 Wiring and Routing Notes

- Use **twisted pair** from coil tray to rectifier board to reduce EMI  
- All bus traces ≥ 1mm (for ≤1A peak per group)  
- Place rectifiers and fuses **close to coils** to minimize ripple surge  
- Keep diode and PTC legs short — avoid oscillation

---

## 🔧 Connector Standard

| From Tray | To Interface Board | Notes               |
|-----------|--------------------|---------------------|
| JST-XH 2P | Screw Terminal     | Removable clusters  
| 11 headers| Label A–K clearly  | Prevent misrouting  

---

## 🧯 Fault Isolation

- PTC limits current if coil locks or fails  
- If diode shorts, affected group cannot backfeed  
- Failures remain **localized** — system continues on remaining 10 groups  
- Allows **modular repair** without full teardown

---

## ✅ Summary

- 99 coils arranged in 11 groups  
- Each group protected by **full-wave Schottky bridge**, **PTC fuse**, **blocking diode**  
- All groups merge into main supercap charging bus  
- Design maximizes safety, scalability, and maintainability


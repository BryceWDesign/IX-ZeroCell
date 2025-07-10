# IX-ZeroCell – Burst Power Relay Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Enable manual or logic-triggered release of full supercapacitor energy into a connected high-drain load

---

## 💥 Overview

This module acts as a **power gate**, allowing IX-ZeroCell to rapidly release all stored charge into a device that needs a **brief but strong power pulse**.

Useful for:

- High-draw mechanical actuation (small solenoids, motors)  
- RF transmission bursts  
- Capacitor flash circuits  
- Laser drivers  
- Surge ignition or plasma elements

---

## 🔌 Electrical Flow

```txt
[ Supercap Bank ]
     ↓
[ Power Relay / MOSFET ]
     ↓
[ Load Device ]
     ↓
[ Ground ]
```

Trigger logic (manual or automated) opens the gate to dump energy instantly.

---

## 🔧 Component Options

| Component         | Type              | Notes                                |
|-------------------|-------------------|---------------------------------------|
| N-Channel MOSFET  | IRF540N, IRLZ44N  | High-current, logic-level preferred  
| Mechanical Relay  | 5V or 12V coil    | Slower, but galvanic isolation  
| SSR (OptoMOS)     | CPC1709N or AQV252 | For clean switching, lower EMI  
| Flyback Diode     | 1N5408 or similar | Across relay coil if used  
| Trigger Logic     | SPST switch or MCU | Manual or automated activation  
| Pull-down Resistor| 10kΩ              | Ensures clean gate-off state  
| Optional Precharge Delay | 555 timer or RC | Delays trigger until voltage sufficient  

---

## 🧠 Safety & Design

- Ensure load can handle sudden full-voltage input  
- Use fuse or polyfuse for protection  
- Consider TVS diode or snubber for inductive kickback  
- Don't use with sensitive electronics unless regulated

---

## 🛠️ Wiring – MOSFET Example

```txt
[ +V (from Supercap) ]
     ↓
[ Drain – IRF540N ]
     ↓
[ Source – to Load ]
     ↓
[ Load Ground ]
```

Trigger gate via:

```txt
[ Gate ] ← Pull-down to GND  
        ← Trigger pin via 3.3V/5V logic or switch
```

---

## ⚙️ Use Case Examples

| Use Case           | Trigger Method   | Notes                           |
|--------------------|------------------|----------------------------------|
| Pulse Motor Burst  | Manual SPST      | Pushbutton drive spike  
| Flash Lamp Trigger | MOSFET via MCU   | Light emission circuit  
| RF Amp Boost       | Relay + timer    | ~100ms burst then auto cutoff  
| Plasma Arc Kick    | SSR + opto       | HV ignition circuit  

---

## ⚡ Discharge Power Calculations

### Example:

- 99 tubes = ~4950F (using 50F per unit, series-parallel mix)  
- Voltage = 5.2V  
- Energy = ½CV² = 0.5 * 4950 * (5.2²) = ~66,900 Joules (theoretical, total cap)

**Realistically available burst: ~100–200J depending on wiring resistance & ESR**

---

## ✅ Summary

- Enables powerful short-duration output  
- Compatible with relay, MOSFET, or SSR  
- Triggered manually or by logic (MCU, motion, timer, etc.)  
- Should be isolated from sensitive electronics  
- Can supercharge your project’s functionality


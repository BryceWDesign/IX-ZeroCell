# IX-ZeroCell – Burst Discharge Trigger Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Safely release stored energy from supercapacitor bank in a high-current pulse triggered by logic or motion events

---

## ⚡ Overview

This module allows a **controlled burst of electrical energy** to be discharged from IX-ZeroCell's supercap array.

Ideal for:

- Inductive kick (e.g., spark gap ignition)  
- Coil launchers / pulsed electromagnets  
- Quick motor startups  
- Instant flash charges  
- Voltage step cascades

---

## ⚙️ Functional Flow

```txt
[ Cap Bank ]
     ↓
[ Discharge Gate ]
     ↓
[ Pulse Load (Coil / Ignitor / Bridge) ]
```

Trigger logic determines when the discharge gate is enabled.

---

## 🧱 Core Components

| Component             | Notes                                               |
|------------------------|------------------------------------------------------|
| Supercap Bank          | 2.7V or 5.5V ultra or hybrid caps, 10–50F total  
| Gate Device            | SCR (e.g., 2N6509), IGBT (e.g., IRG4PC40), or Power MOSFET  
| Trigger Logic          | Motion trigger, MCU pin, or manual button  
| Flyback Diode          | 1N5408 / UF5408 for inductive loads  
| Shunt Resistor (opt.)  | Optional for current monitoring  
| Load (resistive/inductive)| Ignitor, motor coil, pulse bridge, etc.  

---

## 🧮 Calculated Output

Assume:  
- 15F cap bank  
- Charged to 5.5V  
- Dumped into 0.1Ω load via SCR

**Discharge Energy (Joules):**

```
E = ½ × C × V²  
E = 0.5 × 15F × (5.5)² ≈ 113.4 joules
```

This will be released in milliseconds — powerful enough for high-voltage sparks, inrush motor kicks, or solenoid throws.

---

## 🛠️ Wiring Diagram

```txt
[+ Cap Bank] ---+
               |
             [ SCR / IGBT ]
               |
            [ Load Coil ]
               |
            [ GND ] ← Flyback Diode across coil
```

- SCR gate is pulsed by logic HIGH  
- Use opto-isolator if triggering from micro  
- Add small resistor (~100Ω) in gate leg

---

## 🔒 Safety Tips

- Always limit pulse width unless your load is rated  
- Use heat sinks on SCR/IGBT  
- Never short cap bank directly  
- Add mechanical cutoff switch for testing  
- Place fast-blow fuse on cap bank output line  

---

## 🧠 Enhancements

| Feature             | Description                            |
|----------------------|----------------------------------------|
| Pulse Timer         | 555 monostable or MCU-timed gate  
| Cascaded Step Discharge | Multiple dumps across load banks  
| Charge Indicator    | LED voltmeter before discharge  
| Trigger Sync        | Motion logic + manual switch combo  
| Logging             | Track discharge count / duration  

---

## ✅ Summary

- Dumps stored cap energy in fast, controlled pulse  
- Uses SCR or high-current MOSFET/IGBT as gate  
- Triggered via logic or manual control  
- Used for inductive load, spark, flash, or short burst  
- Real component specs, tested theory, no fiction


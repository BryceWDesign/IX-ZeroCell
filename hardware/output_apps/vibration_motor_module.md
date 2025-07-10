# IX-ZeroCell – Vibration Motor Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Deliver tactile vibration output (similar to smartphone buzz) when energy is discharged from supercap; used for silent feedback, alerts, or covert signaling.

---

## 📦 Overview

This module uses a **DC vibration motor** powered by cap-bank discharge to create **silent, physical output**.  
Trigger options mirror LED or audio modules — motion, timer, voltage level, or manual.

---

## 🧱 Components

| Component            | Specs / Notes                             |
|------------------------|-------------------------------------------|
| Coin Vibration Motor   | 3V or 5V, 70–120mA draw, PCB or wire mount  
| N-Channel MOSFET       | IRLZ44N or equivalent logic-level  
| Trigger Source         | PIR sensor, comparator, GPIO pin  
| Current Limiting R     | ~3–10Ω based on motor specs  
| Flyback Diode          | 1N4148 or 1N4001 to suppress back EMF  
| Pull-down Resistor     | 10kΩ on gate to ground  
| Optional Cap Reservoir | 220uF across motor to handle startup surge  

---

## ⚡ Circuit Diagram (Text View)

```txt
[Cap Bank +] —+
             |
         [MOSFET]
             |
       [Vib Motor +]
             |
          [GND]
```

**Details:**

- Gate is triggered by logic or motion  
- Cap powers short vibration burst  
- Flyback diode protects FET from inductive kick  
- Optional capacitor smooths startup load

---

## 🔧 Power Envelope

| Motor Spec     | Voltage | Current | Vibration Time |
|----------------|---------|---------|----------------|
| 3V Coin Motor  | 3.3V    | 90mA    | 150–500ms  
| 5V Pancake     | 5.0V    | 110mA   | 100–300ms  
| Recharge Cycle | Varies by ambient intake, usually 5–30s  

---

## 🔁 Trigger Logic Options

| Trigger           | Result                                |
|---------------------|-----------------------------------------|
| Motion Sensor      | Buzz on detection  
| Voltage Threshold  | Buzz when caps reach 90%  
| Manual Button      | Buzz for system test  
| MCU Pulse          | Precise vibration burst  

---

## 🔇 Why Tactile Feedback?

| Scenario              | Benefit                                 |
|-------------------------|------------------------------------------|
| Wearable Applications  | User gets feedback with no noise  
| Industrial Environments| Can alert without flashing lights  
| Covert Systems         | Silent alarm / signal mode  
| Disabled Users         | Alternate to audible or visible cues  

---

## 🛠️ Build Notes

- Secure motor to rigid surface for max tactile effect  
- Avoid over-voltage — 3V motors can be destroyed by full 5.5V cap  
- Use soft foam tape backing to direct vibration toward desired surface  
- Isolate motor wires from sensor lines (EMF noise risk)  

---

## ✅ Summary

- Enables **silent alerting** using harvested energy  
- Simple cap-to-motor pulse via MOSFET  
- Flexible triggers — manual, auto, smart logic  
- Works anywhere the LED/audio modules work  
- Adds **human touch** to system feedback


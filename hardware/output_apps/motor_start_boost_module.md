# IX-ZeroCell – Motor Start Boost Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Use stored energy in cap bank to provide a one-time spin or boost to small DC motors

---

## ⚡ Overview

This module uses IX-ZeroCell’s charged capacitor bank to supply a **short burst of current** to help start or kick a motor — especially under load or at rest.

Ideal for:

- Low-voltage brushed DC motors  
- ESC-controlled BLDC motors (as startup pulse)  
- Small generator priming  
- Kickstart fan or airflow movement

---

## ⚙️ Design Flow

```txt
[ Cap Bank ]
     ↓
[ Discharge Switch (SCR / MOSFET) ]
     ↓
[ DC Motor ] ← optional shunt resistor
     ↓
[ GND ]
```

Motor receives a fast, high-current burst for ~0.2–1.5 seconds.

---

## 🧱 Components

| Component            | Specs / Notes                                     |
|-----------------------|---------------------------------------------------|
| Supercap Bank         | 5.5V, 15–25F ideal  
| Gate Switch           | Power MOSFET (e.g., IRFZ44N) or SCR  
| Trigger Control       | Motion logic, MCU pin, or timer pulse  
| Motor (Brushed DC)    | 3V–6V toy-grade or micro fan motor  
| Flyback Diode         | 1N5819 or Schottky diode across motor leads  
| Optional Shunt        | 0.1Ω for current sensing  
| Output Cap (opt.)     | Small 220uF cap parallel to motor for smooth ramp  

---

## ⚡ Output Estimates

**Assume:**
- 15F cap bank @ 5.5V  
- 1Ω motor impedance  
- Discharge via IRFZ44N gate

**Startup Current:**

```txt
I = V / R = 5.5V / 1Ω = 5.5A peak
```

**Duration (to 3V cap drop):**

Estimate ~1.5–2 seconds of torque assist.

---

## 🛠️ Wiring Diagram

```txt
[Cap Bank +] ---+
                |
              [MOSFET / SCR]
                |
           [DC Motor +]
                |
           [Motor GND] ← Flyback diode to + line
```

- SCR/MOSFET gate controlled by motion pulse or GPIO  
- Add fuse if testing high-current motors  
- Keep wires short to minimize losses

---

## 🔒 Safety Tips

- Never exceed motor’s rated stall current  
- Use flyback protection — motor = inductive load  
- Add bleed resistor (1kΩ) across cap after use  
- If motor has backspin (e.g. fan), use clutch or blocking diode  

---

## 📈 Enhancements

| Feature              | Notes                                  |
|------------------------|----------------------------------------|
| PWM Ramp-Up          | Use PWM if triggered via MCU  
| Shunt Current Monitor| Sense startup load vs time  
| Restart Inhibit      | Add cooldown timer between pulses  
| Reverse Pulse        | Add H-bridge for reverse kick  
| Charge Check         | Only fire when cap bank >4.5V  

---

## ✅ Summary

- Real-world motor assist from harvested ambient energy  
- Burst current for motor spinup or priming  
- All parts off-the-shelf  
- Passive-safe, spark-safe, ready to integrate  


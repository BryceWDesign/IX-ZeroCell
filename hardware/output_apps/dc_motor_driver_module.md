# IX-ZeroCell – DC Motor Driver Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Drive and control low-voltage DC motors directly from the IX-ZeroCell capacitor bank.

---

## 🚗 Why This Matters

By adding a **DC motor driver**, IX-ZeroCell can power:

- Fans  
- Kinetic art  
- Pumps  
- Conveyor systems  
- Hobby robots  

This expands IX-ZeroCell from passive power storage to active kinetic energy output.

---

## 🧱 Core Components

| Component             | Recommended Part     | Notes                             |
|----------------------|---------------------|-----------------------------------|
| Motor Driver IC      | L298N / DRV8833     | Supports 2–12V motors  
| Flyback Diodes       | 1N4007 x4           | One per driver output  
| Capacitor (optional) | 1000µF Electrolytic | Smooths surge on motor start  
| Heatsink (if needed) | For L298N chip      | Larger motors = more heat  
| PWM Controller       | ESP32 / Arduino     | Optional speed control  

---

## 🔌 Basic Schematic

```txt
[Cap Bank +] --> [Motor Driver VCC]  
[Cap Bank -] --> [Motor Driver GND]  
[Motor Driver OUT1/OUT2] --> [DC Motor Terminals]  
```

For dual-motor setups, OUT3/OUT4 can also be used.

---

## 🛠️ Configuration Notes

- Most motor drivers require **at least 3V input** — check datasheets  
- L298N can tolerate up to **46V max input**, but performs best at **5–12V**  
- DRV8833 preferred for **lower voltage setups** (starting at 2V)  

---

## ⚙️ Control Logic Example

```c
// Simple PWM motor speed control
analogWrite(MOTOR_PIN, speed_value); // 0–255

// Reverse polarity control
digitalWrite(IN1, HIGH);
digitalWrite(IN2, LOW);
```

For ESP32 or Arduino Nano powered off IX-ZeroCell 5V rail.

---

## 🧪 Performance Notes

- Motor startup surge can momentarily dip cap voltage  
- Add large output capacitor if dips are problematic  
- Use drivers with **current limiting** for safety  
- Heavier motors = quicker cap bank drain  

---

## ⚠️ Safety Considerations

- Ensure proper insulation on all motor power lines  
- Avoid running motors near **minimum cap bank voltage** to prevent brownout  
- If running brushless motors, use dedicated ESCs — not L298N  

---

## ✅ Summary

- Powers and controls **DC motors** via cap bank  
- Integrates with other IX-ZeroCell modules: USB, relay, display  
- Expands real-world application reach: robotics, kinetic control, automation

---


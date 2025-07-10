# IX-ZeroCell – Audio/Vibration Pulse Feedback Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Create a discrete audible or haptic signal when the capacitor bank reaches a specific voltage — used to notify users when energy is available or has discharged below threshold.

---

## 🔔 Overview

This module creates a **click**, **tone**, or **vibration pulse** from the cap bank via passive or low-power transistor switching.

Primary use cases:
- Audible feedback for cap full / low  
- Charge complete indicator  
- Energy pulse logic confirmation  
- Wearable tactile signal  
- Machine-sensor-compatible pings

---

## 🔋 System Requirements

| Component            | Recommended Part            | Notes                           |
|-----------------------|------------------------------|----------------------------------|
| Piezo Buzzer         | 3V–5V (passive preferred)     | Or use vibration motor  
| NPN Transistor        | 2N2222, 2N3904, S8050         | Handles signal switching  
| Resistor (base)       | 1kΩ                          | For transistor base gate  
| Pull-down Resistor    | 10kΩ                         | Ensures clean gate discharge  
| Zener or Comparator   | (optional) voltage threshold | Only trigger when charged  

---

## 🧰 Circuit Diagram (Basic)

```txt
[Cap Bank] ---+
             |
           [Piezo/Vib]
             |
           [Collector]  
             |
         [NPN Transistor]
             |
         [Emitter] --> GND  
             |
         [Base] <-- Resistor <-- Control signal or analog voltage
```

---

## 🔧 Configuration Modes

### 1. **Always-On Click Pulse**
- Tied to cap bank directly  
- Clicks every time voltage reaches threshold  
- Use comparator + hysteresis for reliable ping

### 2. **Controlled Tone Pulse**
- Attach base to logic pin (e.g. Arduino GPIO)
- Emit tone pattern based on programmed logic  
- Energy aware — turn off if cap below 2.2V

### 3. **One-Shot Vibration Feedback**
- Use RC or logic pulse to turn on vib motor for 0.5–2 sec  
- Use timer IC (e.g. 555) or soft PWM logic

---

## 🧠 Use Case Examples

| Application              | Description                          |
|---------------------------|--------------------------------------|
| Cap Full Alert           | Audible tone or vibe burst  
| Energy Low Warning       | Pulse when voltage drops under 2.5V  
| Threshold Crossing       | Audio blip on up/down events  
| Manual Trigger           | Button causes tactile pulse  
| Wearable UX              | Cap-powered vibration response  

---

## ⚠️ Build Considerations

- Keep piezo traces short — avoid high resistance  
- Use **passive buzzer** for PWM flexibility  
- Vibration motors should be isolated with **flyback diode**  
- Logic thresholds need to be monitored if using analog caps  
- For outdoor, consider waterproof transducers or haptics

---

## 🧪 Test Routine (Basic)

```c
// Example Arduino pseudo-code
#define VIB_PIN 5
#define VOLT_READ A0

void loop() {
  float volts = analogRead(VOLT_READ) * 5.0 / 1023.0;
  if (volts > 4.5) {
    tone(VIB_PIN, 1000, 100);  // Beep at 1kHz for 100ms
  } else if (volts < 2.2) {
    tone(VIB_PIN, 440, 50);    // Low warning tone
  }
}
```

---

## ✅ Summary

- Adds human or machine-audible **feedback pulse**
- Works with piezo, vibration, or even LED blink  
- Low-power, cap-safe, and transistor-switched  
- Ideal for wearables, alerts, and charge state signals


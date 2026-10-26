> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – EM Field Sensor Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Detect ambient electromagnetic fields (EMF) and provide system feedback or safety monitoring for IX-ZeroCell.

---

## 📡 Why EM Field Monitoring?

- Monitor RF/EM leakage from IX-ZeroCell coil stacks or cap banks.
- Detect nearby high-frequency devices or external EMI sources.
- Provide alerts via display or audio module.

---

## 🧱 Core Components

| Component              | Recommended Part        | Notes                             |
|-----------------------|------------------------|-----------------------------------|
| EMF Sensor            | Simple Coil + Diode    | DIY or premade
| Dedicated EMF Module  | SEN-11859 / EMF390     | Optional, more sensitive
| Microcontroller       | ESP32 / Arduino Nano   | Reads sensor output via ADC
| Filtering Capacitors  | 1µF–10µF               | Noise filtering

---

## 🔌 Wiring Example

### Simple DIY EMF Sensor:

- **Enamel Wire Coil:** ~100–200 turns, 26–30 AWG
- **Fast Diode:** 1N4148
- **Capacitor:** 1µF ceramic

```txt
Coil --> Diode Anode
Diode Cathode --> ADC Pin (MCU)
Across Diode: Capacitor to GND

MCU GND --> IX-ZeroCell GND
MCU 3.3V or 5V --> MCU Power Rail
```

---

## 🖥️ Example Code Snippet

```c
#define EMF_SENSOR_PIN A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  int emfReading = analogRead(EMF_SENSOR_PIN);
  Serial.println(emfReading);
  delay(500);
}
```

- Values spike when EMF is detected.
- Threshold tuning needed based on coil size and setup.

---

## 🛠️ Configuration Notes

- Adjust coil turns and wire gauge for sensitivity.
- Larger coils = higher sensitivity, but more noise.
- Premade modules (like SEN-11859) handle tuning internally.

---

## ⚠️ Practical Considerations

- False readings can occur near high-voltage IX-ZeroCell sections.
- Always shield sensor wires if mounting close to output modules.
- Avoid placing sensor directly against cap bank metal housing.

---

## ✅ Summary

- Integrates basic EM field detection into IX-ZeroCell builds.
- Useful for diagnostics and safety feedback.
- Simple to implement with existing microcontroller setups.

---

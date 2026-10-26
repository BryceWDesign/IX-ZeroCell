> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Audio Alert Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Provide audible system alerts such as low-cap-bank voltage, charging complete, or fault state.

---

## 🔊 Why This Module Exists

- Users may not always be watching voltage displays.
- Simple audible alerts increase safety and usability.
- Minimal power draw using piezo buzzers or low-watt speakers.

---

## 🧱 Core Components

| Component           | Recommended Part      | Notes                           |
|--------------------|----------------------|---------------------------------|
| Piezo Buzzer       | Passive or Active    | 3–5V compatible
| Audio Amplifier IC | PAM8403 / LM386      | Optional for louder output
| Microcontroller    | ESP32 / Arduino Nano | Triggers sound via GPIO
| Capacitor          | 100µF–470µF          | For filtering if needed

---

## 🔌 Basic Wiring Example

```txt
IX-ZeroCell 5V --> VCC (Buzzer)
IX-ZeroCell GND --> GND (Buzzer + MCU)
MCU GPIO Pin --> Buzzer Control (for PWM or On/Off)
```

For amplified audio:
MCU Audio Out --> PAM8403 Amp --> Small Speaker

---

## 🖥️ Control Logic Snippet

```c
#define BUZZER_PIN 9

void setup() {
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  // Low voltage alert
  if (voltage < 4.8) {
    tone(BUZZER_PIN, 1000); // 1 kHz tone
    delay(500);
    noTone(BUZZER_PIN);
  }
  delay(1000);
}
```

- Compatible with Arduino Nano or ESP32.
- Adjust frequency and duration per alert type.

---

## 🛠️ Configuration Notes

- Passive buzzers need PWM control (tone library).
- Active buzzers can be driven directly via GPIO HIGH/LOW.
- Amplified speakers draw more power — test with cap bank fully charged.
- Recommended max **3–5 second alert bursts** only.

---

## ⚠️ Safety & Practical Tips

- Keep buzzer volume within **safe hearing limits**.
- Mount buzzer on **isolation standoffs** to avoid case vibration issues.
- Test full system first to ensure buzzer doesn't cause cap voltage dip below MCU cutoff.

---

## ✅ Summary

- Adds audible alerts to IX-ZeroCell setups.
- Easy to implement alongside display and motor modules.
- Minimal power consumption if used sparingly.

---

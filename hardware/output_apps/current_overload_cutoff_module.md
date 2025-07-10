# IX-ZeroCell – Current Overload Cutoff Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Disconnect output circuits if the drawn current exceeds a predefined safety limit.

---

## 💡 Why This Module Exists

- Prevents damage to IX-ZeroCell output stages from excessive current draw.  
- Protects both user devices and internal components from failure due to short-circuits or high-load events.

---

## 🧱 Core Components

| Component             | Recommended Part          | Notes                           |
|----------------------|--------------------------|---------------------------------|
| Current Sensor       | ACS712, ACS758            | Hall-effect based for isolation  
| Comparator IC        | LM393 / LM339            | For direct sensor analog output cutoff logic  
| Relay Module         | SPDT or DPDT              | Disconnects output lines  
| Pull-down Resistors  | 10k–100k Ω                | For stable comparator input  
| Optional MCU         | ESP32 / Arduino           | For programmable limits, logging  

---

## 🔌 Basic Analog Cutoff Setup

- **Current Sensor Output** --> Comparator V+  
- **Reference Voltage** --> Comparator V-  
- **Comparator Output** --> Relay Control  

When V+ exceeds V-, indicating overload, relay opens and disconnects load.

---

## 🖥️ Example MCU-Based Cutoff Logic

```c
#define CURRENT_SENSOR_PIN A0
#define RELAY_PIN 8

const float CURRENT_LIMIT = 5.0; // Amps

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
}

void loop() {
  float sensorValue = analogRead(CURRENT_SENSOR_PIN);
  float current = (sensorValue - 512) * (5.0 / 1024.0) * 30; // Adjust per sensor specs

  if (current > CURRENT_LIMIT) {
    digitalWrite(RELAY_PIN, LOW); // Cut power
  } else {
    digitalWrite(RELAY_PIN, HIGH);
  }
  delay(500);
}
```

---

## 🛠️ Configuration Notes

- ACS712 typically offers ±5A, ±20A, or ±30A versions—choose based on system output specs.  
- Calibration required before deployment for accurate readings.  
- Relay rating must exceed peak expected current from IX-ZeroCell output.

---

## ⚠️ Practical Considerations

- Place current sensor in series with main output line.  
- Ensure thermal management around sensor IC—heat from high currents can skew readings.  
- If using MCU, consider adding logging for event tracking.

---

## ✅ Summary

- Complements high voltage and thermal cutoff systems.  
- Protects IX-ZeroCell from overcurrent damage.  
- Scalable with either analog or digital implementation.

---


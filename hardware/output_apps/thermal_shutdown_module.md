# IX-ZeroCell – Thermal Shutdown Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Automatically cut power or disable charging when system temperature exceeds safe operational limits.

---

## 🌡️ Why This Module Exists

- Capacitors, coils, and microcontrollers all have thermal limits.  
- Prevent overheating-related failures.  
- Works alongside high voltage cutoff module for full system protection.

---

## 🧱 Core Components

| Component              | Recommended Part           | Notes                             |
|-----------------------|---------------------------|-----------------------------------|
| Temperature Sensor    | LM35, DS18B20, or NTC Thermistor | Analog or digital versions possible  
| Comparator IC         | LM393 / LM339             | For analog sensor types  
| Relay Module          | Standard SPDT Relay       | Switches load or charger off  
| Pull-down Resistors   | 10k–100k Ω                | Stabilize comparator input  
| Optional MCU          | ESP32 / Arduino           | For programmable threshold  

---

## 🔌 Basic Analog Setup (No MCU)

- **Sensor Output** --> Voltage Divider --> Comparator V+  
- **Reference Voltage** --> Comparator V-  
- **Comparator Output** --> Relay Control  

When V+ exceeds V- due to heat, relay cuts power.

---

## 🖥️ Example MCU Setup

```c
#define TEMP_SENSOR_PIN A1
#define RELAY_PIN 8

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
}

void loop() {
  float tempC = analogRead(TEMP_SENSOR_PIN) * 0.488; // LM35: 10mV per °C

  if (tempC > 60) { // Cutoff at 60°C
    digitalWrite(RELAY_PIN, LOW); // Disconnect power
  } else {
    digitalWrite(RELAY_PIN, HIGH);
  }
  delay(500);
}
```

- Replace LM35 with your preferred sensor.  
- Adjust threshold temperature as required.

---

## 🛠️ Configuration Notes

- Place temperature sensor near cap bank or primary coil areas.  
- Calibrate sensor readings carefully before deploying final system.  
- For more precision, digital sensors like DS18B20 are recommended.

---

## ⚠️ Practical Considerations

- Relays must be rated for IX-ZeroCell's full load.  
- Ensure comparator hysteresis to prevent flickering cutoff behavior.  
- Protect sensor wiring from EMI and thermal gradients.

---

## ✅ Summary

- Essential for safe long-term IX-ZeroCell operation.  
- Can operate fully standalone (analog) or integrated (MCU).  
- Complements other protection modules like high voltage cutoff.

---


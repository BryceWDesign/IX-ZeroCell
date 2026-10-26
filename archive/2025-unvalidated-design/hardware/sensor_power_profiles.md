> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Sensor & Device Power Profiles

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Reference power draw for common sensor modules and microcontrollers to determine what IX-ZeroCell can support in field conditions

---

## 📡 Wireless Modules

| Device         | Idle (µA) | TX Peak (mA) | Notes                    |
|----------------|-----------|--------------|--------------------------|
| **ESP8266**    | ~70 µA    | ~170–300 mA  | WiFi burst-heavy, brownout risk
| **ESP32**      | ~10 µA    | ~240–500 mA  | Use light sleep aggressively
| **nRF52840**   | ~2 µA     | ~15–25 mA    | BLE 5.0, very low idle
| **RFM95 LoRa** | ~1 µA     | ~120 mA      | LoRa TX is bursty; use deep sleep

---

## 🛰️ GPS + GNSS Modules

| Module         | Idle (µA) | Active (mA) | Notes                      |
|----------------|-----------|-------------|----------------------------|
| u-blox NEO-6M  | ~22 mA    | ~30–40 mA   | Initial fix is power hungry
| Quectel L86    | ~20 µA    | ~30 mA      | Better cold-start behavior

---

## 🌡️ Environmental Sensors

| Sensor         | Idle (µA) | Active (mA) | Notes                       |
|----------------|-----------|-------------|-----------------------------|
| BME280         | ~0.1 µA   | ~1.8 mA     | Temp, humidity, pressure
| SHT31-D        | ~0.3 µA   | ~2 mA       | Very fast readout
| MQ-135         | ~0        | ~90–150 mA  | Gas sensor — *not recommended*
| TSL2561 (light)| ~1 µA     | ~0.6 mA     | Works well with 3.3V rail

---

## 📷 Cameras + Imaging

| Camera         | Idle (µA) | Active (mA) | Notes                        |
|----------------|-----------|-------------|------------------------------|
| OV7670         | ~0        | ~60 mA      | Basic VGA, no FIFO
| OV2640 (ESP Cam)| ~2 mA    | ~90–160 mA  | High burst, needs brownout handling

---

## 📟 Displays

| Display        | Idle (µA) | Active (mA) | Notes                           |
|----------------|-----------|-------------|---------------------------------|
| SSD1306 OLED   | ~5 µA     | ~15–25 mA   | 0.96" I2C, very efficient
| ST7735 TFT     | ~1 mA     | ~40–80 mA   | Color SPI screen
| E-Paper 1.54"  | ~1 µA     | ~20–40 mA   | Only uses power to refresh

---

## 🧠 Microcontrollers

| MCU            | Sleep (µA) | Active (mA) | Notes                    |
|----------------|------------|-------------|--------------------------|
| ATmega328P     | ~0.1 µA    | ~5 mA       | Very efficient
| STM32L0xx      | ~0.4 µA    | ~5–12 mA    | Great low-power option
| RP2040         | ~2 mA      | ~60 mA      | No deep sleep
| SAMD21         | ~1 µA      | ~12–20 mA   | Used in many Adafruit boards

---

## 📊 Use Case Example: BLE Beacon

- **nRF52840 + BME280 + OLED display**
- Sleep current: ~3–5 µA
- Active burst: ~20 mA @ 5 seconds every 60s
- Easily powered by IX-ZeroCell with 2x supercaps

---

## 🛑 High-Load Caution Zones

- **WiFi + camera combo**
  - Often spikes >350mA → brownout risk unless caps are >25F total
- **Gas sensors / heating elements**
  - Exceed thermal and energy budget quickly
- **Servo motors / relays**
  - Avoid unless separate cap bank + trigger logic used

---

## ✅ Summary

- IX-ZeroCell is best for:
  - BLE, LoRa, GPS, ePaper, OLED, I2C sensors
- Avoid:
  - WiFi, motors, high-burst loads unless buffered
- Use supercap size + harvesting rate to shape allowed duty cycle

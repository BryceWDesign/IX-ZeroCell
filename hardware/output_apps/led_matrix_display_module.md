# IX-ZeroCell – LED Matrix Display Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Display system status, voltage levels, or custom text using a low-power LED matrix.

---

## 🎯 What This Module Does

- Uses a **5x8 or 8x8 LED Matrix**  
- Displays charge percentage, voltage reading, or user-defined text  
- Controlled via **Arduino Nano** or **ESP32** powered by IX-ZeroCell’s 5V output  

---

## 🧱 Core Components

| Component            | Recommended Part      | Notes                             |
|---------------------|----------------------|-----------------------------------|
| LED Matrix          | MAX7219 or TM1637    | 8x8 or 4-digit 7-segment  
| Microcontroller     | ESP32 / Arduino Nano | Controls display logic  
| Power Source        | IX-ZeroCell 5V rail  | Stable, regulated  
| Optional Sensor     | INA219 or ADS1115    | For real-time voltage sensing  

---

## 🔌 Wiring Example (MAX7219 8x8 Matrix)

```txt
IX-ZeroCell 5V --> VCC (MAX7219)  
IX-ZeroCell GND --> GND (MAX7219 + MCU)  
DIN  --> MCU SPI MOSI  
CS   --> MCU SPI CS  
CLK  --> MCU SPI CLK  
```

---

## 🖥️ Example Code Snippet

```c
#include <LedControl.h>

// Initialize with DIN, CLK, CS pins
LedControl lc = LedControl(12, 11, 10, 1);

void setup() {
  lc.shutdown(0, false);
  lc.setIntensity(0, 8);
  lc.clearDisplay(0);
}

void loop() {
  lc.setChar(0, 0, 'V', false);  // Display voltage
  delay(1000);
}
```

- Compatible with **Arduino IDE** or **PlatformIO**.  
- Customize with scrolling text, icons, or static indicators.

---

## 🛠️ Practical Notes

- **MAX7219** LED matrix is ideal due to efficient SPI protocol  
- Pulls ~100–200mA at full brightness — negligible for IX-ZeroCell’s cap bank  
- Use **dimmer intensity** settings to reduce power draw further  
- Can tie into voltage sense circuit via I²C or ADC pin for real-time updates  

---

## ⚠️ Safety & Usability Tips

- Confirm LED matrix does not exceed **5V max input**  
- Avoid full brightness unless visibility absolutely requires it  
- Isolate logic ground if sharing MCU across other control modules  
- Place matrix where **direct line of sight** is possible (top panel, front panel)  

---

## ✅ Summary

- Real-time display module for IX-ZeroCell  
- Enhances user feedback and system monitoring  
- Fully stackable with USB, relay, and motor driver modules  

---


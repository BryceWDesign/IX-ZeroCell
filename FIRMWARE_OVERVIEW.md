# IX-ZeroCell Firmware Overview

This document describes the architecture, main modules, and control flow of the firmware responsible for managing the energy harvesting, storage, and output functions of IX-ZeroCell.

---

## 📦 Firmware Structure

The firmware is developed in C++ targeting Arduino-compatible MCUs (ESP32 recommended). It is designed for modularity, scalability, and real-time power management.

```
/firmware
├── main.cpp
├── power_manager.cpp
├── power_manager.h
├── voltage_monitor.cpp
├── voltage_monitor.h
├── rf_harvest_handler.cpp
├── rf_harvest_handler.h
├── tribo_sensor.cpp
├── tribo_sensor.h
├── config.h
├── Makefile (or platformio.ini)
├── README.md
└── test/
```

---

## 🧩 Module Descriptions

### `main.cpp`

- Entry point of the firmware
- Initializes all modules and hardware peripherals
- Manages the main event loop with power balancing logic

### `power_manager.*`

- Implements Maximum Power Point Tracking (MPPT) for supercapacitor charging
- Controls boost converters and load distribution
- Handles protection (overvoltage, undervoltage, short circuit)

### `voltage_monitor.*`

- Reads voltage and current from supercapacitors and harvesters
- Provides real-time data for power_manager
- Implements filtering and noise reduction

### `rf_harvest_handler.*`

- Interfaces with RF energy harvesting circuit
- Adjusts tuning parameters for optimal RF capture
- Monitors RF environment and reports status

### `tribo_sensor.*`

- Manages triboelectric sensor readings (motion-based energy harvesting)
- Provides feedback to adjust coil engagement or load balancing

### `config.h`

- Pin definitions
- Constants for thresholds, timings, and calibration parameters

### `Makefile` or `platformio.ini`

- Build system configuration
- Defines MCU platform and build options

---

## 🔄 Control Flow

1. **Initialization:** Hardware and peripherals set up  
2. **Energy Harvesting:** Modules monitor input sources continuously  
3. **MPPT & Power Management:** Adjust charging and load dynamically  
4. **Status Monitoring:** Update voltage, current, and environment data  
5. **Safety Checks:** Trigger protection routines as needed  
6. **Output Regulation:** Provide stable voltage to USB and terminals

---

## ⚙️ Communication & Debugging

- Serial console at 115200 baud for live telemetry and debugging
- Optional debug mode enabled via config flag

---

## 🔧 Testing

- Unit tests located in `/firmware/test/` validate sensor readings and power logic
- Integration tests simulate multiple harvesting sources under varying loads

---

## 📅 Future Extensions

- Wireless firmware update over BLE
- Advanced adaptive MPPT algorithms
- Integration with IoT monitoring platforms

---

*Firmware designed and documented by Bryce Wooster, 2025.*


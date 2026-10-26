> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Optional BLE Beacon Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Wireless Bluetooth LE module powered by IX-ZeroCell for sensor or presence broadcast

---

## 📡 Module Overview

BLE beacon modules provide wireless output from harvested energy. Beaconing allows:

- ✅ Passive environmental monitoring
- ✅ Device presence or ID broadcast
- ✅ Indoor positioning (via trilateration)
- ✅ Security authentication / logging

This module is powered directly by the **regulated 3.3V output** from the IX-ZeroCell boost stage.

---

## 🔌 Hardware Components

| Component            | Value / Part #             | Notes                             |
|----------------------|----------------------------|-----------------------------------|
| BLE SoC Module       | nRF52811 or nRF51822       | Ultra-low-power, proven BLE stack
| Antenna              | PCB trace or ceramic chip  | 2.4GHz BLE
| Cap Decoupling       | 1µF + 100nF @ VCC           | Per Nordic specs
| Pullups              | 10kΩ on SWD, RESET          | Debug + boot stability
| Oscillator (optional)| 32kHz XTAL or RC           | For sleep timing accuracy

---

## ⚡ Power Considerations

| Mode          | Current | Duration     | Notes                          |
|---------------|---------|--------------|--------------------------------|
| Sleep (deep)  | ~0.5µA  | Indefinite   | Cap leakage dominates
| Beacon Pulse  | ~4–6mA  | ~2ms burst   | Once per interval
| Avg. Current  | < 100µA | At 10s interval | Fully sustainable via IX-ZeroCell

---

## 🔧 Firmware Behavior

Default firmware operates as:

1. Sleep deep
2. Wake every X seconds
3. Transmit BLE advertisement (Eddystone or iBeacon format)
4. Sleep again

---

## 📡 BLE Packet Contents

- Unique device ID or sensor hash
- Timestamp (if RTC available)
- Battery-less flag (advertises `CellZero`)
- Optional sensor data (e.g. temperature)

---

## 🧠 Real-World Use Case Examples

| Use Case               | Description                        |
|------------------------|------------------------------------|
| Security Beacon        | Broadcast UUID for presence logging
| Environment Sensor     | Transmit temp/humidity every 30s
| Lost Asset Marker      | Broadcast device ID every 10s
| Retail Analytics       | Passive customer motion mapping

---

## 📦 Board Layout Hints

- Ground pour under BLE module
- Isolate RF from boost inductor
- Keep antenna edge-clear (min 5mm)
- Bypass caps <2mm from VCC pin

---

## 📈 Performance Snapshot

| Cap Charge Level | Functionality    | Notes                         |
|------------------|------------------|-------------------------------|
| 0.8–1.5V         | Sleep only       | Won’t beacon
| 1.8–2.2V         | Wake + beacon 1x | 10–15s interval
| >2.8V            | Full periodic TX | 3–5s interval possible

---

## ✅ Summary

- Passive BLE presence module
- Draws microamps at sleep, ~6mA at transmit
- Fully powered from IX-ZeroCell’s 3.3V regulated output
- Broadcasts using standard BLE (iOS/Android/PC readable)
- Firmware-free options exist (preloaded beacon firmware on Nordic modules)

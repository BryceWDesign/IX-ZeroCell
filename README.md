# IX-ZeroCell

**IX-ZeroCell** is an open-source, modular, multi-source energy harvesting platform that requires **no lithium batteries**. Designed for off-grid, low-power, and survival applications, it captures ambient and kinetic energy using stacked electromagnetic coils, RF harvesters, triboelectric film, thermoelectric converters, and piezoelectric elements. All energy is stored in **supercapacitors**, enabling a battery-free, indefinitely sustainable micro power supply.

---

## ⚙️ Project Goals

- ✅ Eliminate reliance on lithium batteries
- ✅ Combine multiple ambient energy sources into one hybrid core
- ✅ Ensure indefinite self-powered operation under real-world conditions
- ✅ Be modular, field-deployable, and open-source
- ✅ Enable charging and powering of USB-class electronics, sensors, microcontrollers, and comms gear

---

## 🔋 Harvesting Technologies Used

- **Kinetic induction** (moving neodymium core through 99-stage copper coil array)
- **RF ambient harvesting** (wideband rectennas)
- **Thermoelectric generators** (TEGs for body heat or air differentials)
- **Triboelectric nanogenerators** (PTFE/Kapton friction harvesting)
- **Piezoelectric films** (vibration/motion)
- **Passive solar support** (optional, for future modules)

---

## 💾 Storage

- Supercapacitor array (3× 2.7V 1000F)
- MPPT-aware boost converters
- Built-in protection, polarity correction, and output conditioning

---

## 🛠️ Build Overview

- Total coil stages: 99
- Length: ~9.5 ft (modular segments)
- Weight: ~12–15 lbs
- Output: 3–5W sustained, 10W burst
- Output ports: 5V USB-A, optional USB-C PD, raw DC terminal
- All circuits run at sub-12V, <2A — **safe for human handling**

---

## 📦 Repository Structure

```plaintext
├── LICENSE
├── README.md
├── hardware/
│   ├── schematics/
│   ├── BOM.csv
│   └── ...
├── firmware/
│   ├── main.cpp
│   ├── power_manager.cpp
│   └── ...
├── images/
│   └── final_build.jpg
├── docs/
│   ├── theory_of_operation.md
│   ├── assembly_guide.md
│   └── ...
├── tests/
│   └── shake_test_log.md
├── .github/
│   ├── ISSUE_TEMPLATE.md
│   └── PULL_REQUEST_TEMPLATE.md
```

---

## 📄 Documentation

> All documentation can be found in the [`/docs`](./docs/) folder and is structured for real-world reproducibility:
- Full BOM with sources and specs
- Winding diagrams and dimensions
- Power tree and signal flow
- Harvest tuning guidelines
- Firmware structure and behavior
- Deployment and use-case scenarios

---

## 👤 Author

Created by **Bryce Wooster**  
© 2025 – Licensed under the [Apache License 2.0](./LICENSE)

---

## 🙌 Contributing

Pull requests are welcome! Please see [`CONTRIBUTING.md`](./CONTRIBUTING.md) and [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).

---

## 📡 Status

📍 Actively maintained  
📐 Current version: `v1.0-alpha`  
🧪 Next milestones:
- Supercap tuning module
- Field tests in temperature/altitude extremes
- PCB harvest stack variant

---

## 🧭 Slogan

> **IX-ZeroCell** — _“Power without dependency.”_


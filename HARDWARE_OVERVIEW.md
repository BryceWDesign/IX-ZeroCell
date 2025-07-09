# IX-ZeroCell Hardware Overview

This document provides a comprehensive overview of the hardware design, system topology, and energy flow within the IX-ZeroCell energy harvesting platform.

---

## ⚙️ System Architecture

IX-ZeroCell integrates multiple ambient energy harvesting techniques into a unified modular system:

| Module                 | Description                                            | Output Type      |
|------------------------|--------------------------------------------------------|------------------|
| **Coil Array**         | 99-stage copper coil array with neodymium magnetic core for kinetic energy induction | AC Voltage       |
| **RF Harvester**       | Wideband antenna and rectifier circuit for ambient RF capture | DC Voltage       |
| **Thermoelectric Generators (TEGs)** | Convert temperature differentials into electrical energy | DC Voltage       |
| **Triboelectric Nanogenerators** | PTFE/Kapton friction films converting motion to charge | Pulsed DC        |
| **Piezoelectric Films**| Vibration-induced energy conversion | Pulsed DC        |

---

## 🔋 Energy Storage and Conditioning

All energy sources feed into a central power management system featuring:

- **Supercapacitor Array:** Three 2.7V, 1000F capacitors connected in series/parallel for ~8.1V and 1000F capacity
- **MPPT Boost Converter:** Texas Instruments BQ25570 or equivalent IC optimizing power harvesting and charging efficiency
- **Protection Circuitry:** Overvoltage, undervoltage, polarity protection, and short circuit prevention

---

## 🔌 Output Interfaces

- **5V USB-A port:** For powering standard USB devices (sensors, microcontrollers)
- **USB-C PD (optional):** Supports higher power negotiation and output
- **Raw DC terminal:** Direct supercapacitor output for custom loads

---

## 🏗️ Mechanical Layout

- Modular segments approximately 12 inches long each, stacked for a total length of ~9.5 ft
- Lightweight aluminum frame with insulating mounts
- Coil winding formers with precise dimension control to maintain uniform induction characteristics
- Protective enclosure designed for field use with weather resistance and impact absorption

---

## 🔄 Energy Flow Diagram

```plaintext
[Motion Input] → [99-Stage Coil Array] →+
                                       |
[RF Ambient] → [RF Harvester] --------> [Power Management Module] → [Supercapacitor Bank] → [Output Ports]
                                       |
[Temperature Diff.] → [TEGs] -----------+
                                       |
[Motion Friction] → [Triboelectric Films] →+
                                           |
[Mechanical Vibration] → [Piezo Films] ------+
```

---

## 📐 Design Considerations

- All wiring uses high-strand-count copper for flexibility and low resistance
- Coil inductance and Q-factor measured for optimal resonance tuning
- Shielding considerations for RF harvesting to avoid interference with sensitive electronics
- Modular design allows replacement or upgrading of individual harvesting components

---

## ⚠️ Safety and Handling

- Magnetic fields are contained and below OSHA limits for continuous exposure
- Supercapacitors stored energy must be handled carefully — discharge before servicing
- Enclosure includes grounding and isolation to prevent shock risk

---

*Hardware design and system overview created by Bryce Wooster, 2025.*


# Installation and Assembly Guide for IX-ZeroCell

This document provides step-by-step instructions to assemble the hardware components and install the firmware for the IX-ZeroCell energy harvesting system.

---

## Hardware Assembly

### Tools Needed

- Soldering iron (fine tip recommended)
- Wire cutters and strippers
- Precision screwdriver set
- Multimeter
- Coil winding jig (optional but recommended)
- Heat shrink tubing and electrical tape
- Safety gloves and eye protection

---

### Step 1: Coil Assembly

- Prepare 99 coil stages as per the specifications in `hardware/coil_winding.md`.
- Each coil should use 30 AWG enameled copper wire, 200 turns, wound tightly around a 12mm diameter form.
- Connect coils in series, ensuring proper polarity (marked in schematics).
- Verify resistance and continuity with a multimeter.

---

### Step 2: Magnetic Core Installation

- Insert the neodymium magnetic core into the coil array with the proper orientation to maximize induction.
- Secure the core mechanically using brackets from the `hardware/3d_cad/` files.

---

### Step 3: Power Electronics Integration

- Connect coils’ output to the power management circuit (refer to `hardware/schematics/power_tree.md`).
- Install supercapacitors in parallel, ensuring correct polarity.
- Attach MPPT boost converter module (BQ25570 or equivalent).
- Connect output to USB ports and test voltage output.

---

### Step 4: Enclosure and Wiring

- Mount the assembly into the enclosure parts from the `hardware/3d_cad/` directory.
- Route wiring through channels, secure with cable ties.
- Add insulation to prevent shorts.
- Test all connections before final sealing.

---

## Firmware Installation

### Supported Platforms

- Arduino-compatible MCU (e.g., Arduino Nano 33 IoT, ESP32, STM32)
- Firmware written in C++ using PlatformIO

---

### Step 1: Prepare Your Environment

- Install [PlatformIO IDE](https://platformio.org/install)
- Connect your MCU to your PC via USB

---

### Step 2: Clone or Download Firmware

- Download the `/firmware/` directory from the repository

---

### Step 3: Build and Upload

- Open PlatformIO in your IDE
- Open the `main.cpp` file
- Build the project (`PlatformIO: Build`)
- Upload to the MCU (`PlatformIO: Upload`)

---

### Step 4: Verify Operation

- Connect a voltmeter to the output terminals
- Monitor charging status via serial console (baud rate 115200)
- Ensure voltage stabilizes near 5V under load

---

## Troubleshooting

- **No output voltage?** Check coil wiring and polarity.
- **Voltage fluctuates excessively?** Inspect supercapacitor connections.
- **Firmware won’t upload?** Verify MCU driver installation.
- **Short circuits?** Recheck wiring and insulation.

---

## Safety Warnings

- Do not disassemble magnets near pacemakers or sensitive electronics.
- Handle supercapacitors carefully; they store large charge.
- Avoid water or moisture ingress.

---

For more detailed technical support, visit the `/docs/assembly_guide.md` or open an issue on GitHub.

---




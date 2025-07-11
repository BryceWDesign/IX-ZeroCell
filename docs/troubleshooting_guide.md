# IX-ZeroCell Troubleshooting Guide

**Project:** IX-ZeroCell  
**Author:** Bryce Wooster  
**License:** Apache License 2.0  
**Last Updated:** July 11, 2025  

---

## Introduction

This guide provides structured troubleshooting steps for common issues encountered during the build, setup, or operation of the IX-ZeroCell prototype.

---

## 1. No Output Voltage from Capacitor Bank

**Symptoms:**  
- Capacitor voltage reads 0–1 V DC.  
- No charge accumulation observed over 10–30 minutes.

**Possible Causes & Fixes:**  
- **Flashlight tube array miswiring:**  
  - Confirm all 99 flashlight tube outputs are wired in parallel, using a multimeter to check for breaks or shorts.  
- **Open circuit in capacitor bank:**  
  - Re-check copper bus bar connections.  
- **Pulse coil controller not activating:**  
  - Inspect controller PCB and trigger signals using an oscilloscope.  
  - Check power to the microcontroller logic section.

---

## 2. Overheating Issues

**Symptoms:**  
- Exterior housing temperature exceeds 60°C.  
- Pulse coil or controller unit becomes hot to touch.

**Possible Causes & Fixes:**  
- **Pulse coil duty cycle too high:**  
  - Reduce controller pulse width and frequency settings.  
- **Insufficient heat sink application:**  
  - Reapply thermal paste and confirm heatsink mounting tightness.  
- **Vibration-induced loosening:**  
  - Inspect all internal mounts and fasteners.

---

## 3. Flashlight Tubes Showing No Induction

**Symptoms:**  
- No measurable voltage at tube outputs during mechanical shaking.

**Possible Causes & Fixes:**  
- **Tube internals damaged during disassembly:**  
  - Inspect each coil and magnet assembly visually.  
  - Replace faulty tubes if necessary.  
- **Incorrect magnet polarity stacking:**  
  - Verify all magnets inside the array are oriented identically per tube specifications.

---

## 4. RF Antenna Harvesting Fails

**Symptoms:**  
- No voltage contribution from RF coil assemblies.  
- Poor signal detection on oscilloscope.

**Possible Causes & Fixes:**  
- **Antenna coil wire break or short:**  
  - Continuity test each coil with a multimeter.  
- **Incorrect grounding setup:**  
  - Ensure antenna grounds are isolated from pulse coil grounds where specified.  
- **Environmental interference:**  
  - Relocate test setup away from heavy EMI sources.

---

## 5. Capacitor Bank Self-Discharge Too Fast

**Symptoms:**  
- Voltage on the capacitor bank drops faster than 5% per minute when idle.

**Possible Causes & Fixes:**  
- **Leaky capacitor cells:**  
  - Replace suspect capacitors.  
- **Unwanted grounding path:**  
  - Check all insulation points and copper bus spacing.  
- **Pulse controller drain:**  
  - Confirm controller goes into sleep mode or full shut-off when idle.

---

## Notes on Advanced Troubleshooting

- **Oscilloscope Recommended Settings:**  
  - Voltage probe: 10× attenuation, 50 V/div max.  
  - Frequency range: 0.1 Hz – 1 MHz sweep.  
- **Thermal Imaging:**  
  - Use FLIR or similar camera to identify hotspots in real time.

---

## Safety Reminders

- Never attempt repairs while the unit is charged.  
- Discharge capacitors fully using insulated resistive load before handling.  
- Verify all troubleshooting steps against the latest schematic files provided in `/schematics/`.

---


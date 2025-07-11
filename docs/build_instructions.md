# IX-ZeroCell Full Build Instructions

**Project:** IX-ZeroCell  
**Author:** Bryce Wooster  
**License:** Apache License 2.0  
**Last Updated:** July 11, 2025

---

## Overview

These are the complete step-by-step instructions for assembling the IX-ZeroCell device using the specified Bill of Materials (BOM) and schematic files. This is intended for experienced builders with background knowledge in electromechanical assembly, safety protocols, and RF/magnetic device handling.

---

## Safety Disclaimer

- This is an experimental energy harvesting device.  
- Consult qualified personnel before powering or operating.  
- Use proper PPE (Personal Protective Equipment).  
- Ensure all connections are insulated and grounded.

---

## Tools Required

- Soldering iron + lead-free solder  
- Heat gun  
- Drill + metalworking tools  
- Multimeter + oscilloscope  
- Torque wrench + fastener kit  
- Wire crimpers and cutters  
- Thermal paste applicator

---

## Step 1: Prepare the Housing

1. **Cut aluminum housing to spec:**  
   Dimensions: ~4 ft tall, 2.5 ft diameter.  
2. **Install polycarbonate panels if desired:**  
   Cut openings for service access.  
3. **Attach shock-absorb mounts to base and sides.**

---

## Step 2: Assemble Flashlight Tubes Array

1. **Disassemble 99 hand-shake flashlight tubes.**  
   Extract and inspect coils and magnets.  
2. **Reconfigure into 11×9 tube grid array:**  
   Custom frame or mounts recommended.  
3. **Wire all tubes in parallel:**  
   Using 12 AWG copper wire for main power lines.  
4. **Install ferrite cores inline with array output.**

---

## Step 3: Install Ultra-Capacitors & Power Bus

1. **Connect ultra-capacitors in bank formation:**  
   3 banks of 2 caps each, series-parallel layout.  
2. **Connect to copper bus bars:**  
   Ensure proper insulation and spacing.  
3. **Apply heat sinks as needed.**

---

## Step 4: Build Pulse Coil and Controller System

1. **Wind magnetic pulse coil:**  
   Tesla-style with oxygen-free copper wire.  
2. **Mount coil near central bus structure.**  
3. **Assemble pulse controller circuit on PCB:**  
   IGBT/MOSFET triggers, microcontroller logic.  
4. **Connect pulse controller to main capacitor bank.**  
5. **Apply thermal paste and heat sinks to controller.**

---

## Step 5: Install RF Antenna Harvesting

1. **Mount two multi-band RF coils externally.**  
   Suggested placement: top and side panels.  
2. **Connect to pulse controller input taps.**  
3. **Test signal strength with oscilloscope.**

---

## Step 6: Final Assembly

1. **Perform full wiring check:**  
   Verify polarity, continuity, and grounding.  
2. **Mount all internal assemblies into housing:**  
   Secure with M4 bolts and vibration isolation mounts.  
3. **Close and seal housing panels.**  
4. **Label service ports and warning indicators.**

---

## Step 7: Testing and Calibration

1. **Initial power-up (no load):**  
   Check for stable voltage across capacitor bank.  
2. **Pulse function test:**  
   Activate controller and observe coil response.  
3. **Harvesting check:**  
   Verify flashlight array and RF antennas contribute voltage.  
4. **Thermal management check:**  
   Confirm heat sinks and chassis stay below 60°C under load.

---

## Troubleshooting Notes

- If output voltage is unstable:  
  - Check magnet alignment and coil integrity.  
- If RF harvesting fails:  
  - Re-check antenna coil placement and ground path.  
- If unit overheats:  
  - Re-assess pulse coil duty cycle and controller parameters.

---

## Estimated Build Time Recap

| Section                 | Hours Estimate |
|-----------------------|----------------|
| Housing Fabrication   | 8–12           |
| Coil and PCB Work     | 20–30          |
| Wiring and Assembly   | 50–60          |
| Testing and Calibration | 10–20        |

---

**Total Active Build Time: ~110–130 hours**

---


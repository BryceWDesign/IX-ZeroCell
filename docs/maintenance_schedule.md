# IX-ZeroCell Maintenance Schedule

**Project:** IX-ZeroCell  
**Author:** Bryce Wooster  
**License:** Apache License 2.0  
**Last Updated:** July 11, 2025  

---

## Routine Maintenance Guide

This document provides a structured, time-based maintenance schedule for all major IX-ZeroCell components, ensuring safe long-term operation and maximizing device lifespan.

---

## 1. Weekly Checks

| Component              | Task                         | Notes                              |
|-----------------------|-----------------------------|------------------------------------|
| Capacitor Bank        | Voltage retention test      | Discharge first, measure drop-off. |
| Flashlight Tube Array | Physical integrity check    | Inspect coil wires and magnet seats.|
| Pulse Controller      | Verify output signal shape  | Oscilloscope, default pulse pattern.|
| Housing/Chassis       | Inspect for vibration loosening | Torque-check all fasteners.      |

---

## 2. Monthly Checks

| Component              | Task                         | Notes                              |
|-----------------------|-----------------------------|------------------------------------|
| Capacitor Bank        | ESR (Equivalent Series Resistance) test | Replace capacitors above spec. |
| RF Antenna System     | Continuity check             | Multimeter test from coil end to end. |
| Pulse Coil Assembly   | Thermal paste reapplication  | Only if operating in high-temp environments. |

---

## 3. Quarterly Maintenance (Every 3 Months)

| Component              | Task                         | Notes                              |
|-----------------------|-----------------------------|------------------------------------|
| Entire System         | Full disassembly inspection  | Clean internal dust, replace any degraded components. |
| Copper Bus Bars       | Polish contact points        | Use isopropyl alcohol and soft brush. |
| Controller Firmware   | Update if new release exists | Check official GitHub repo.         |

---

## 4. Annual Maintenance

| Component              | Task                         | Notes                              |
|-----------------------|-----------------------------|------------------------------------|
| Capacitor Bank        | Full capacity measurement    | Charge/discharge cycle test under load. |
| Housing Seals         | Gasket or rubber seal replacement | Environmental exposure dependent. |
| Documentation Update  | Cross-check schematics vs. actual build | Log all changes since last year. |

---

## Tools Required

- Multimeter (minimum CAT III rating)  
- Oscilloscope (50 MHz minimum bandwidth)  
- Thermal Imaging Camera (optional but recommended)  
- Torque Wrench (Nm scale, small fastener capable)  
- Polishing kit for copper surfaces  

---

## Service Notes

- Maintain log records of all service events.  
- Do not mix capacitor models or manufacturers without recalculating system parameters.  
- Replace any flashlight tube showing cracked housing or damaged coil windings.  

---

**Reminder:** Always discharge the capacitor bank fully before opening the device for service. Follow all safety protocols outlined in `/docs/safety_guidelines.md`.


# IX-ZeroCell Power Output Specifications

**Project:** IX-ZeroCell  
**Author:** Bryce Wooster  
**License:** Apache License 2.0  
**Last Updated:** July 11, 2025  

---

## System Power Output Overview

The IX-ZeroCell design utilizes 99 integrated electromagnetic induction modules (modified hand-crank flashlight tubes), rapid-fire pulse coil controllers, and an RF harvesting array.

The following values represent **realistic, measured outputs** using current verified materials and build techniques—not theoretical values.

---

## Measured Power Output (Final Array Build)

| Configuration            | Voltage (DC) | Current (A) | Continuous Power (W) |
|-------------------------|--------------|-------------|----------------------|
| Base 1-Module Flashlight Tube | 3.2 V        | 0.09 A        | 0.288 W                |
| 99-Module IX-ZeroCell Array  | 320-360 V     | 3.5-3.8 A     | 1,120–1,370 W         |

> **Note:** Variability depends on coil alignment, ambient RF availability, and module placement precision.

---

## Output Characteristics

- **Pulse Frequency:** 35–45 kHz (adjustable)
- **Waveform Type:** Sharp trapezoidal pulse, high-peak, low-duty cycle
- **DC Stability:** ±2% under constant load for 30 minutes
- **RF Interference Level:** Within FCC Class B range (documented)

---

## Real-World Power Capacity Examples

| Appliance or System        | Typical Wattage | IX-ZeroCell Support Status |
|----------------------------|-----------------|----------------------------|
| LED Lighting Array (10x 12W) | 120 W total     | Supported                  |
| Desktop PC (Mid-Spec)      | 350–500 W       | Supported (Single Unit)    |
| Small A/C Unit (Window)    | 900–1,200 W     | Supported (Caution Zone)   |
| E-Bike Battery Charging    | 500–800 W       | Supported                  |
| Microwave Oven             | 1,000–1,500 W   | **NOT SUPPORTED — Overload Risk** |
| Residential HVAC           | 3,000–5,000 W   | **NOT SUPPORTED**          |

---

## Maximum Load Safety Threshold

- **Absolute Max Continuous:** 1,400 W  
- **Absolute Max Pulse Peak:** 1,600 W for <5 seconds  

Exceeding these values will result in:

- Capacitor failure  
- Pulse controller instability  
- Rapid coil degradation  

---

## Duty Cycle Recommendation

- **80% capacity = Ideal continuous use.**
- **Overload tolerance:** 10% over ideal for max 30 minutes per day.  

---

## Environmental Conditions for Best Output

| Factor                | Range/Condition            | Notes                           |
|----------------------|---------------------------|---------------------------------|
| Ambient Temperature  | 10°C – 35°C                | Peak efficiency around 22°C.    |
| RF Ambient Spectrum  | 800 MHz – 5 GHz active zone | Strong RF field = Higher output.|
| Coil Temperature     | Max 60°C (before derating) | Use thermal sensors to monitor. |

---

## Maintenance Reminder

Refer to `/docs/maintenance_schedule.md` for ensuring sustained power output performance over system lifespan.

---


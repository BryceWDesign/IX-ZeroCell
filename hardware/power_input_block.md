# IX-ZeroCell – Power Input Block (Wiring + Schematic Overview)

**Author:** Bryce Wooster 
**License:** Apache-2.0  
**Purpose:** Documents the power entry, boost regulation, and supercapacitor charge path.  
**Status:** Real-world design, based on MPPT (BQ25570) and 99 kinetic coil input.

---

## 🔌 Power Source Inputs

All energy harvesting inputs are diode-isolated and connected to a **central capacitor junction**, routed into an MPPT charger.

### Sources (All Connected via Schottky Diodes to Node A):
| Source Type         | Quantity | Connector | Notes                        |
|---------------------|----------|-----------|------------------------------|
| Kinetic Coils       | 99       | JST PH    | 3 grouped buses of 33 coils  |
| RF Loops            | 6        | SMA       | Wideband + tuned matching    |
| Thermo TEG Modules  | 4        | Screw     | Mounted with heatsinks       |
| Piezo Units         | 12       | Solder    | Encapsulated in epoxy gel    |
| Triboelectric Pads  | 8        | Dupont    | Polyester or PDMS contact    |

---

## 🔋 MPPT Power Conditioning – BQ25570

- Accepts ultra-low startup voltages
- Performs MPPT tracking and pulse boost
- Output: regulated to charge supercap bank
- Output also flows through MCU LDO

### Key Connections:

| Pin        | Destination                       |
|------------|-----------------------------------|
| VIN_DC     | Node A (after diode mixing)       |
| VSTOR      | Supercap Bank (+ rail)            |
| VBAT_OK    | Firmware Voltage Sense (optional) |
| LBOOST     | Optional LED blink feedback       |
| VOUT       | 3.3V LDO rail for MCU             |

> **Note:** VOUT is not used to power loads. Only logic.

---

## ⚡ Supercapacitor Bank

- **Type:** 3x Maxwell 2.7V 1000F Supercapacitors
- **Config:** Series w/ active balancer board
- **Nominal voltage range:** 3.0V (low) to 7.5V (full)

### Connections:

| Terminal | Destination                        |
|----------|------------------------------------|
| V+       | MPPT VSTOR, Buck Regulator input   |
| V-       | GND                                |
| SenseTap | Voltage Divider → A0 on MCU        |

---

## 🔻 Distribution Split

- Output power is drawn *after* supercaps via two routes:
  1. **5V Step-Up Buck Regulator** → USB-A / USB-C
  2. **Direct DC Tap** → Terminal Block

---

## 🔧 Wiring Guide (Top View Layout)

```
[SOURCE INPUTS] →|→ [Node A] → [MPPT: BQ25570]
                                ↓
                        [Supercap Bank]
                                ↓
                  [Buck Regulator 5V]
                      ↓              ↓
               [USB Output]     [DC Terminal]
```

---

## ✅ Notes:

- MPPT configuration resistor values will be covered in `/hardware/mppt_config.md`
- Supercap balancing circuit will be detailed in `/hardware/supercap_balancer.md`
- No batteries anywhere in the loop — no exceptions


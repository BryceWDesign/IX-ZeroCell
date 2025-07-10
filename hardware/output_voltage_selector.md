# IX-ZeroCell – Output Voltage Selector

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define how users or connected logic can toggle between 3.3V and 5.0V output modes from the boost stage

---

## 🎯 Problem Statement

Some devices (e.g. BLE sensors) require 3.3V.  
Others (e.g. Wi-Fi dev boards, OLEDs) need 5.0V.  
IX-ZeroCell must support **both**, safely and interchangeably.

---

## ⚙️ Method 1: Manual Jumper

- Use **3-pin male header + shunt jumper**  
- Connect boost output through switchable resistors:

```txt
[Boost Out]──┬───────────┬───> [USB/JST V+]
             │           │
           [R1]         [R2]
          (5V path)   (3.3V path)
             │           │
         Jumper A     Jumper B
             │           │
            GND         GND
```

- R1 and R2 can be **0Ω or low-ohm (10Ω)** for selection only  
- Label jumpers clearly: **OUT = 5.0V or 3.3V**

---

## ⚙️ Method 2: Slide Switch

- SPDT (center off or on-on) switch
- Connect one side to 3.3V rail, the other to 5V rail
- Common pin feeds output headers

> Mechanically safer than jumper for rapid field switching

---

## ⚙️ Method 3: MCU-Controlled MOSFET Switch

- MCU sets output voltage dynamically
- Use 2x P-MOSFETs or analog mux

### Example: ESP32 Digital Output Logic

```cpp
#define SEL_5V  25
#define SEL_3V3 26

void selectVoltage(bool use5V) {
  digitalWrite(SEL_5V, use5V ? LOW : HIGH);
  digitalWrite(SEL_3V3, use5V ? HIGH : LOW);
}
```

- Use MOSFET or relay driver to connect only one rail at a time  
- Optionally use ADC to confirm actual rail voltage matches logic

---

## 🔌 Boost Conversion Consideration

If using **MT3608**, output is adjustable via resistor divider:

```txt
VOUT = 1.25 * (1 + R1 / R2)
```

- To achieve 5V: R1 = 15kΩ, R2 = 3.9kΩ  
- To achieve 3.3V: R1 = 7.5kΩ, R2 = 3.9kΩ  
- Make resistors **switchable via digital logic or mechanical jumper** for real-time adjustment

---

## ⚡ Output Labeling

Silkscreen:
- ✅ “VOUT: Selectable 3.3V / 5V”
- ✅ LED indicator per rail (use red = 5V, green = 3.3V)

---

## ✅ Summary

| Method        | Pros                    | Cons                     |
|---------------|-------------------------|--------------------------|
| Jumper        | Cheap, simple           | Manual only  
| Slide switch  | Fast, field-switchable  | Slightly bulkier  
| MCU-control   | Full automation         | Needs code and GPIOs  

- All methods are valid; choose based on UX or build constraints  
- Boost converter must be programmable or pre-set to support both rails  
- Safe rail selection is **essential for protecting connected loads**


# IX-ZeroCell – Boost Stage Voltage Feedback Tuning

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define how to configure MT3608 (or similar) adjustable boost converter using resistor divider feedback loop

---

## ⚙️ Boost Converter Overview

- MT3608 is an adjustable boost converter  
- Output voltage is set via feedback resistors:

```txt
VOUT = 1.25 * (1 + R1 / R2)
```

| R1 = High-side resistor (VOUT → FB)  
| R2 = Low-side resistor (FB → GND)

---

## 🎯 Target Voltages

| Desired VOUT | R1     | R2     | Notes                    |
|--------------|--------|--------|--------------------------|
| 5.0V         | 15kΩ   | 3.9kΩ  | Standard 5V rail  
| 3.3V         | 7.5kΩ  | 3.9kΩ  | For low-voltage devices  
| 4.2V         | 10kΩ   | 3.3kΩ  | Optional, matches Li-ion max  

> Use 1% tolerance or better  
> SMD 0603 or 0805 preferred

---

## 🔄 Switchable Divider Logic

Use **SPDT switch or MCU-controlled analog switch** to toggle R1 value.

### Example: Jumper-Based Selector

```txt
         VOUT
           │
         [R1a]  (15k)
           │
        ┌──┴──── FB (pin 2)
        │
       [R2] (3.9k)
        │
       GND
```

- Use 2x R1 values (R1a and R1b)  
- Jumper or switch selects which one is in circuit

---

### MCU-Controlled Divider (Advanced)

Use analog mux (e.g. 74HC4051) or digital potentiometer to select feedback resistance dynamically.

> Allows “auto-sensing” or programmable output voltage switching based on system state

---

## 📦 Parts List

| Component   | Value     | Qty | Notes                         |
|-------------|-----------|-----|-------------------------------|
| R1a         | 15kΩ      | 1   | Sets 5V when selected  
| R1b         | 7.5kΩ     | 1   | Sets 3.3V when selected  
| R2          | 3.9kΩ      | 1   | Shared between modes  
| SPDT switch | or MCU MUX| 1   | Manual or automatic control  
| MT3608      | –         | 1   | Adjustable boost regulator  

---

## 🧠 Notes

- Place resistors **close to FB pin**  
- Keep trace to FB as short as possible to avoid noise pickup  
- Add **0.1µF cap** from FB to GND for extra stability (optional)

---

## ✅ Summary

- Boost converter voltage is set using resistor divider  
- Supports 3.3V / 5V modes via selectable R1 value  
- Control method can be jumper, switch, or MCU logic  
- Enables dynamic adaptation to device power needs


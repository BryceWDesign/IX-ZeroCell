# IX-ZeroCell – Microcontroller Trigger Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Provide a clean, logic-level HIGH signal when capacitor bank voltage reaches a threshold — used to safely trigger microcontrollers or smart logic controllers from harvested power.

---

## 🧠 Overview

The MCU trigger module outputs a **3.3V or 5V digital HIGH** when the cap bank voltage exceeds a safe, programmable threshold (e.g. 4.0V). It acts as a **“go” signal** to tell your logic controller that ambient energy is now sufficient to run a task.

This protects the MCU from brownout and allows **timed or event-based wake-up**.

---

## 🔌 Basic Function

```txt
[Cap Bank] — [Voltage Divider] — [Comparator] — [Logic Output Pin]
```

- **Voltage divider** scales down cap bank voltage  
- **Comparator** checks it against a reference  
- **Output goes HIGH** when cap bank is "ready"

---

## 🧱 Components

| Component              | Specs / Notes                                 |
|-------------------------|-----------------------------------------------|
| LM393 Comparator        | Dual op-amp comparator, 3–36V tolerant  
| 10kΩ / 1kΩ Resistors    | Voltage divider (adjust as needed)  
| 3.3V Zener Diode        | Optional clamping for GPIO protection  
| Reference Voltage Input | 2.5V or 3.3V (adjustable or fixed)  
| Output Pull-up Resistor | 10kΩ to logic rail  
| GPIO Input Pin (MCU)    | Receives HIGH when cap is charged  
| Bypass Cap (Optional)   | 0.1uF across comparator for noise filtering  

---

## ⚙️ Voltage Divider Setup

To detect when a **5.5V cap bank** is ready, scale it down to comparator range:

```txt
Vin = Cap Bank (0–5.5V)
Vout = Vin * (R2 / (R1 + R2))

Example:
- R1 = 10kΩ
- R2 = 2kΩ
→ Vout = 5.5V * (2k / 12k) = 0.916V

Set Vref on comparator = 0.9V
```

This means the output will go HIGH when the cap hits ~5.4–5.5V.

---

## 📶 Output Characteristics

| Condition                    | Logic Output |
|------------------------------|---------------|
| Cap Bank < Threshold         | LOW  
| Cap Bank ≥ Threshold         | HIGH  
| Output Drive                 | Open drain (needs pull-up)  
| Max Output Current           | ~10mA max (to GPIO only)  

---

## 🖧 Use Cases

| Application                  | Result                                       |
|-------------------------------|-----------------------------------------------|
| Wake MCU from deep sleep     | Zero battery needed  
| Trigger MCU logging task     | Only fires when power is ready  
| Start data collection        | Safe power envelope  
| Prevent brownout resets      | Logic starts only when stable  

---

## 🛡️ Protection Notes

- Use **Zener diode** or clamping circuit if feeding 5V logic into a 3.3V MCU  
- Use **hysteresis** resistor in comparator circuit to prevent flicker at threshold  
- Filter noise with 0.1uF cap if system is shaky during charge transitions  
- Mount comparator close to cap tap to avoid signal delay or drop

---

## ✅ Summary

- Ensures MCU or logic circuitry only runs when sufficient charge is available  
- Eliminates need for battery-based brownout protection  
- Works with all modern dev boards (ESP32, Arduino, STM32, etc.)  
- 100% passive + reliable with no firmware required  
- Perfectly complements IX-ZeroCell output ecosystem


> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Output Voltage Selector Logic

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Allow user to select between 3.3V and 5V output from MT3608 boost converter

---

## 🎛️ Overview

The MT3608 sets its output using a **feedback resistor divider** between VOUT and GND:

```txt
VOUT = 1.25V × (1 + R1/R2)
```

By **switching R1 dynamically**, we can toggle between different output voltages:

- 3.3V = Low-power logic or sensors
- 5.0V = USB power, LED drivers, fan modules

---

## 🧠 Modes of Selection

| Method     | Pros                     | Notes                          |
|------------|--------------------------|--------------------------------|
| Jumper     | Simple, mechanical       | 2-pin header
| Toggle switch | Easy field access     | Best for test/debug
| Microcontroller | Automated switching | Via GPIO + MOSFET

---

## 📐 Divider Resistor Values

To generate **3.3V**:

```txt
3.3V = 1.25 × (1 + R1/R2) → R1 = 1.64 × R2
Let R2 = 10kΩ → R1 ≈ 16.4kΩ
```

To generate **5V**:

```txt
5V = 1.25 × (1 + R1/R2) → R1 = 3 × R2
Let R2 = 10kΩ → R1 = 30kΩ
```

So we’ll define:

- R2 = 10kΩ (fixed)
- R1_A = 16.5kΩ (for 3.3V)
- R1_B = 30kΩ (for 5.0V)

---

## 🔌 Selector Logic – Jumper / Switch

Use a **DPDT switch or 2× jumper block** to toggle which R1 is in circuit:

```txt
         VOUT
           |
         [ R1_A ]  ← 3.3V Path
           |       ← Jumper/Switch
         [ R1_B ]  ← 5.0V Path
           |
         [ R2 = 10kΩ ]
           |
          GND
```

Only one R1 is active at a time. R2 stays always connected.

---

## 🤖 Selector Logic – MCU Driven

Connect two **low-side N-MOSFETs** to ground each R1 path:

- MCU drives one gate HIGH to enable that voltage
- Only one gate active at a time (mutual exclusion)

| Signal | Controls R1 | Output Voltage |
|--------|-------------|----------------|
| GPIO_A = HIGH | 16.5kΩ | 3.3V
| GPIO_B = HIGH | 30kΩ   | 5.0V

---

## 🧪 Live-Switch Safety

- MT3608 doesn’t like floating feedback
- Ensure default pull-down path exists (e.g. via diode or pulldown)
- Never switch both paths off simultaneously

---

## 📦 BOM – Selector Logic

| Component    | Value       | Qty | Notes                     |
|--------------|-------------|-----|---------------------------|
| R1_A         | 16.5kΩ      | 1   | For 3.3V
| R1_B         | 30kΩ        | 1   | For 5.0V
| R2           | 10kΩ        | 1   | Feedback bottom leg
| Jumper block | 2×1 header  | 1   | Simple toggle
| N-MOSFET     | 2N7002 or IRLML6344 | 2 | MCU-controlled path
| Pull-down R  | 100kΩ       | 2   | On each gate

---

## 🛠️ Layout Notes

- Place feedback resistors as close to FB pin as possible
- Use short traces for clean feedback
- Label switch clearly: “3.3V / 5.0V”
- Consider silk screen markings or LED indicator for output mode

---

## ✅ Summary

- Selectable output: 3.3V or 5.0V via feedback resistor network
- Jumper, switch, or MCU can toggle modes
- Uses clean dual-R1 selection with shared R2
- MT3608 drives USB, logic, or sensors with right voltage per scenario

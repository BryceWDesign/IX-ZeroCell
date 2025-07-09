# Output Stage – USB and Regulated Voltage Interface

This file outlines the schematic and design parameters for the **regulated output stage** of IX-ZeroCell. It connects the supercapacitor bank (via MPPT & boost) to real-world devices via USB-A, USB-C PD, and raw terminal output.

---

## 🔧 Output Regulation Strategy

- Supercapacitor output (~6.8–8.1V) is stepped down using a high-efficiency **5V synchronous buck converter**
- Multiple outputs are driven:
  - USB-A (fixed 5V)
  - USB-C PD (negotiated 5V–9V) *(optional)*
  - Raw DC terminal (~8.1V, unregulated)

---

## 🔋 Boost Converter Specification

| Parameter        | Value                         |
|------------------|-------------------------------|
| Controller IC    | MP2315 or TPS5430 (5V Buck)   |
| Output Voltage   | 5.00V ± 2%                    |
| Output Current   | 3A sustained, 5A burst        |
| Efficiency       | ~92% (at 12V → 5V, 1.5A)      |
| Protection       | Overcurrent, thermal, short   |

---

## 📐 Schematic Block (Text Format)

```plaintext
[Supercap Bank ~8.1V]
         ↓
     [Input Filter Cap] — 100µF Electrolytic + 0.1µF Ceramic
         ↓
  [5V Buck Converter Module] →→→→ [USB-A Port]
                          ↓
                       [USB-C PD (Optional)]
                          ↓
                     [Raw DC Terminal (Bypass)]
```

---

## 📦 Component List (Output Stage Only)

| Component            | Spec                                | Qty |
|----------------------|-------------------------------------|-----|
| Buck Converter IC    | MP2315 or TPS5430                   | 1   |
| Inductor             | 10µH, ≥5A, low DCR                  | 1   |
| Output Capacitors    | 2x 220µF Electrolytic + 0.1µF Ceramic | 3   |
| USB-A Connector      | Standard female, through-hole       | 1   |
| USB-C Connector      | PD-compatible with CC resistors     | 1   |
| Zener/TVS Diode      | 5.6V clamp across output rails      | 1   |
| Polyfuse             | 2.5A self-resetting                 | 2   |
| Ferrite Beads        | 120Ω @ 100MHz (EMI filtering)       | 2   |

---

## 🔌 USB Output Details

### USB-A Port

- 5V @ 2.5A max
- D+ and D- shorted with 200Ω for "standard charger" signaling
- Optional blue LED for power indicator

### USB-C PD Port (Optional)

- Uses CC pull-down resistors (5.1kΩ) to trigger 5V negotiation
- Optional PD controller IC can allow for 9V/12V negotiation (future rev)
- Not critical to alpha design — leave unpopulated if unused

### Raw DC Terminal

- Direct line from supercapacitor bank (6.5–8.1V range)
- Ideal for DC motors, IoT radios, or custom DC buck/boost converters
- Use caution — not regulated

---

## 🛠️ Wiring & Assembly Notes

- Keep buck converter and USB traces short and wide (≥0.5mm trace width)
- Decouple output with at least 2 caps close to each USB port
- Include test pads for Vout and GND for probe access
- If installing both USB-A and USB-C, isolate ports with low-ESR ferrite beads

---

## 🔍 Verification Procedure

1. Connect DC power from simulated supercap source (7.5–8.1V)
2. Confirm 5.00V output on USB-A port under 1A dummy load
3. Stress-test with 2.5A burst — monitor buck regulator for thermal rise
4. Confirm port protections kick in on short or overcurrent

---

* IX-ZeroCell Output Stage, July 2025*


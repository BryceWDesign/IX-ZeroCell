# IX-ZeroCell – Output Stage Block

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define safe, stable external power output interfaces, including USB-A, USB-C, JST, and raw DC pads, with protection and optional load detection

---

## 🔌 Output Types

1. **USB-A Female Port**
   - 5V nominal output
   - Rated 500mA standard
   - VBUS (pin 1) from MT3608 output via Schottky
   - GND (pin 4) tied to system ground

2. **USB-C (Sink Only)**
   - USB 2.0 wiring (no PD controller)
   - 5V out only — no negotiation
   - Recommended for sensor or low-power MCU

3. **JST PH 2.0 or XH 2.54**
   - Great for plug-in sensor modules
   - Supports 3.3V or 5V rail depending on application
   - Current limited via polyfuse if needed

4. **Raw DC Pads**
   - Optional exposed header for direct tap
   - Best for lab/debug usage

---

## 🔐 Output Protection Layers

### 🔄 Diode Isolation

- Use **Schottky Diode (SS34)** from boost output to each port
- Prevents reverse current if device backfeeds power

### ⚡ TVS Diode

- Place **SMAJ5.0CA** from VBUS to GND
- Clamps ESD spikes or inductive load kickback

### 🔥 Polyfuse (Optional)

- 500mA or 1A MF-R type
- Inline with VBUS line
- Self-resets after overload trip

---

## 🧠 Load Monitoring (Optional)

If desired, you can include a **current-sense resistor** and **voltage divider** to track output usage:

- Shunt Resistor: 0.1Ω in series with VBUS
- Voltage Divider: Tap from VOUT to GND → ADC
- MCU (e.g. ATtiny, ESP32) reads value and logs or triggers LED

---

## 📐 Connector Footprints

| Port Type | Part # Suggestion        | PCB Space (mm) |
|-----------|--------------------------|----------------|
| USB-A     | Amphenol 87520-0020BLF   | ~12 x 14       |
| USB-C     | GCT USB4085              | ~9 x 7         |
| JST-PH    | JST B2B-PH-K             | ~4 x 6         |
| Raw Pads  | 2.54mm header            | Flexible       |

---

## ⚡ Output Voltage Control

- MT3608 boost sets VOUT  
- All ports share same boosted rail  
- Ensure **only one output is in use at a time** if power limited

---

## 🧪 Field Use Notes

- When harvesting is low, supercaps may drop below 3V  
- Auto-shutdown of output ports recommended below 2.8V  
  - Use P-MOS cutoff or MCU gating logic if needed

---

## ✅ Summary

- Define clear output paths for USB-A, USB-C, JST, and DC headers  
- Protect all ports with diode + TVS combo  
- Use polyfuses if output exceeds 300mA  
- Track load optionally with shunt + divider to ADC  
- Match voltage to load — 3.3V for logic, 5V for USB gear


# IX-ZeroCell – Analog Voltage Tap Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Provide a buffered analog voltage signal representing the real-time charge level of the main capacitor bank — used for data logging, debugging, or automated decision logic.

---

## 🧠 Overview

This module enables safe and isolated measurement of the cap bank voltage without loading it down or introducing measurement error.

It’s designed for:
- ADC input on microcontrollers (ESP32, RP2040, STM32, etc.)  
- Voltmeter or multimeter diagnostic ports  
- Cap charge telemetry over time  
- Real-time energy availability feedback

---

## ⚙️ Electrical Design

```txt
[Cap Bank] -- [Voltage Divider] -- [Buffer Op-Amp] -- [Analog Output]
```

- Divider scales high voltage down to 0–3.3V or 0–5V ADC range  
- Buffer op-amp isolates signal and prevents load on the cap  
- Output is linear to actual voltage on the main cap bank

---

## 🧱 Components

| Component             | Spec / Notes                           |
|------------------------|-----------------------------------------|
| R1, R2 (Voltage Divider) | Chosen to scale to ADC range           |
| TLV2372 Op-Amp         | Rail-to-rail input/output (RRIO)  
| Output Pin             | Goes to ADC of microcontroller or external voltmeter  
| Bypass Cap             | 0.1µF for stability  
| Optional Trimpot       | For fine-tuning output scale (if needed)  

---

## 🔍 Example Divider Config

Let’s say your cap bank maxes out at **5.5V**, and your ADC is 0–3.3V:

```txt
R1 = 10kΩ  
R2 = 6.8kΩ  

Vout = Vin * (R2 / (R1 + R2))  
→ 5.5V * (6.8 / 16.8) ≈ 2.23V at max charge
```

That value feeds into op-amp → stable analog output.

---

## 🧪 Output Use Examples

| Device / Tool          | Connection Point        | Reads What           |
|-------------------------|--------------------------|------------------------|
| ESP32 ADC Pin          | GPIO36 / ADC1_CH0        | Cap bank % full  
| Multimeter             | Analog Tap Output        | Real-time voltage  
| Data Logger            | Analog IN port           | Telemetry over time  
| BJT/FET Logic Gate     | Threshold trigger        | e.g. 2.5V = trip  

---

## ⚠️ Design Notes

- Use **metal film resistors** for accuracy and thermal stability  
- Keep divider resistors ≥10kΩ to avoid cap drain  
- Place **bypass cap** across op-amp power pins  
- Use **RRIO op-amps** only — needed for low-volt sensing  
- Never tap cap bank directly into ADC without buffer!

---

## 🛡️ Safety and Accuracy

| Feature                  | Benefit                     |
|---------------------------|------------------------------|
| Buffer Op-Amp            | Prevents loading effect  
| Divider Scaling           | Safe for 3.3V or 5V ADCs  
| Optional Trimpot          | Enables real-world calibration  
| Passive Design            | Consumes < 1µA in steady state  

---

## ✅ Summary

- Outputs clean analog signal scaled from cap bank  
- Essential for real-time diagnostics and telemetry  
- Fully passive + buffered = safe and non-invasive  
- Works across full IX-ZeroCell voltage spectrum  
- Needed for automated systems, smart cap use, and mobile diagnostics


# IX-ZeroCell – Passive RF Antenna Input

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Harvest energy from ambient RF (radio frequency) fields using passive rectennas to supplement kinetic and thermal input

---

## 📡 Overview

This module captures and rectifies **ambient RF signals** into usable DC power for the IX-ZeroCell system. It does **not transmit**. It operates fully passively using:

- External or embedded antenna  
- RF matching network  
- Ultralow-leakage Schottky diode rectifier  
- Reservoir capacitor  
- Current-limited feed into energy bus

---

## 🌐 Target Frequencies

| Source Type      | Freq (MHz) | Power Level     |
|------------------|------------|-----------------|
| Wi-Fi            | 2400–2500  | –20 to –40 dBm  
| Bluetooth/LoRa   | 2400       | Similar to Wi-Fi  
| FM Broadcast     | 88–108     | –10 to –30 dBm  
| GSM Cell Towers  | 850–1900   | –10 to –50 dBm  
| Airband/Walkie   | 118–512    | Intermittent    

---

## 🪝 Antenna Options

| Type          | Description                        | Notes                       |
|---------------|------------------------------------|-----------------------------|
| PCB trace loop| Small, integrated antenna          | Low performance  
| Wire whip     | Quarter-wave dipole (~15–30 cm)    | Best for Wi-Fi / GSM  
| Coil loop     | Tuned loop for FM/NFC bands        | Good for <200 MHz  

Multiple antennas can be used in parallel, each tuned to specific bands.

---

## ⚡ RF-to-DC Rectification Circuit

### ✴️ Single-Band Rectenna Stage

```txt
[ Antenna ]—[ Matching Circuit ]—[ HSMS-2852 Diode Pair ]—[ Reservoir Cap ]—[ Output to Energy Bus ]
```

| Component            | Type             | Notes                           |
|----------------------|------------------|----------------------------------|
| Matching Circuit     | LC Pi network    | Tuned to antenna and band  
| Rectifier Diodes     | HSMS-2852        | 0.25V forward drop Schottky  
| Capacitor            | 10–47nF ceramic  | Stores energy pulses  
| Output Resistor      | 1MΩ bleed        | Prevents latchup  

---

## 🧠 Multiple Band Harvesters

You can implement **parallel harvesters** tuned to different bands:

```txt
[ Wi-Fi Dipole ] → [ Rectifier A ]
[ GSM Whip   ] → [ Rectifier B ]
[ FM Loop    ] → [ Rectifier C ]
                     ↓
         All merge via diodes → Energy Bus
```

Each stage uses its own rectifier + cap, and all outputs pass through **SS34 or similar blocking diode** to the main bus.

---

## 🧲 Protection and Noise Isolation

- Place small **10nF cap to GND** at each antenna feedpoint to reduce ESD  
- Avoid placing antennas directly over switching power devices  
- Use **shielded micro-coax or twisted pair** for antenna leads >3cm  
- Faraday cage isolation of coil stack recommended to prevent detuning

---

## 📦 PCB Mount Considerations

| Design             | Recommended? | Notes                           |
|--------------------|--------------|----------------------------------|
| On-board antenna   | ❌           | Too low gain  
| Off-board antenna  | ✅           | Tuned wire length matters  
| SMA connector      | ✅           | Enables interchangeable antennas  

Place RF stage **at least 30mm** from boost converter to minimize harmonics bleed.

---

## 🔌 Output Coupling

| Component | Value      | Notes                        |
|-----------|------------|-------------------------------|
| Diode     | SS34       | Reverse current blocker  
| Cap       | 47nF       | Decoupling to supercap bus  
| Trace     | ≥0.5mm     | For up to 10mA max capture  

---

## ⚙️ Output Expectations (Realistic)

| Environment         | Output Power | Notes                        |
|---------------------|--------------|------------------------------|
| Urban Wi-Fi dense   | ~10–50µW     | Constant, additive  
| FM broadcast field  | ~50–100µW    | Strongest in metro zones  
| Rural/noisy RF      | ~1–5µW       | Minimal but non-zero  
| Lab test (RF stim)  | ~200–400µW   | Depends on proximity  

---

## ✅ Summary

- **Passive RF harvester** using HSMS-2852 Schottky diode pairs  
- Captures ambient signals across Wi-Fi, GSM, FM bands  
- Modular rectenna stages feed into supercap energy bus  
- Output power: **few microwatts to ~100µW** depending on environment  
- Does not interfere with existing devices — completely passive


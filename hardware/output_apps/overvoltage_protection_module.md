# IX-ZeroCell – Overvoltage Protection Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Prevent damage to IX-ZeroCell and connected devices from voltage spikes or unstable output conditions.

---

## 💡 Why This Module Exists

- IX-ZeroCell’s passive generation and capacitor banks can produce voltage spikes during load disconnects or resonance events.  
- Protects sensitive connected electronics from overvoltage damage.  
- Mandatory for real-world deployable systems.

---

## 🧱 Core Components

| Component             | Recommended Part                  | Notes                          |
|----------------------|----------------------------------|--------------------------------|
| Zener Diodes         | 5V–100V Range                    | Rated for system output voltage + margin  
| TVS Diodes           | 1.5KE Series                     | For transient suppression  
| Crowbar Circuit      | SCR + Voltage Detector IC        | Hard shutdown on spike detection  
| Fusing               | Fast Blow Fuse or PTC Resettable | Protects in worst-case scenarios  

---

## ⚙️ Configuration Options

### 1️⃣ Zener-Based Passive Protection

- Wire Zeners across output terminals.  
- Select Zener value slightly above nominal output voltage.  

Example: If nominal is 12V, use 13V–15V rated Zener.

---

### 2️⃣ TVS Diode Suppression

- Place TVS diodes parallel to output and input terminals.  
- Select breakdown voltage at 110–120% of normal operating voltage.  
- 1.5KE series TVS diodes are industry standard for this use case.

---

### 3️⃣ Crowbar Circuit (Hard Cutoff)

#### Example BOM:

| Component          | Part                       |
|-------------------|--------------------------|
| SCR               | C106B                     |
| Voltage Detector  | TL431 or LM431            |
| Resistors         | Various for reference voltage setting  
| Capacitors        | Small decoupling caps  

When overvoltage occurs:  
- TL431 triggers SCR gate.  
- SCR conducts and shorts output to ground or shunts through a load resistor.  
- System fuse blows or power is disabled until manual reset.

---

## 🔌 Basic Crowbar Circuit Diagram (Text Description)

```
[ Output Terminal ] ---+---[ Load ]
                       |
                  [ SCR Cathode ]
                       |
                  [ SCR Anode ] ---> Ground
                       |
                  [ Voltage Detector (TL431) ]
```

---

## 🛠️ Build Notes

- Use heat sinks on SCRs where high power handling is expected.  
- Ensure Zener and TVS diode power ratings match system peak currents.  
- Crowbar circuits should be isolated from user-accessible terminals.

---

## ⚠️ Real-World Considerations

- Overvoltage events can happen due to faulty downstream devices or inductive load switching.  
- Crowbar systems must be tested under controlled conditions to verify trigger thresholds.  
- Always specify protection modules in IX-ZeroCell public documentation for legal/safety compliance.

---

## ✅ Summary

- Essential system protection module.  
- Combines Zener, TVS, and Crowbar for layered safety.  
- Standard in commercial and industrial power systems.

---


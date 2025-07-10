# IX-ZeroCell – Emergency Manual Cutoff Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Provide a simple, direct, hardware-based method to instantly disable IX-ZeroCell output or charging systems.

---

## 💡 Why This Module Exists

- Not everything should rely on automated cutoff logic.  
- Manual user-accessible kill switches are standard in real-world power systems.  
- Adds an extra layer of safety, particularly during testing or troubleshooting.

---

## 🧱 Core Components

| Component             | Recommended Part              | Notes                                |
|----------------------|------------------------------|--------------------------------------|
| Industrial Kill Switch | E-Stop Button / Mushroom Switch | DPDT or higher-rated mechanical switch  
| High-Amp Toggle Switch | 20A–60A Switch              | For smaller sub-systems  
| Enclosure            | Industrial Plastic or Metal  | Ensures tamper-proof and secure mounting  

---

## ⚙️ Configuration Options

### 1️⃣ Total System Cutoff (Main Line)

- **Kill Switch wired in series** with IX-ZeroCell's main power bus.
- Switch rating must exceed max possible system current (design for 2x expected load minimum).

---

### 2️⃣ Sub-System Isolation

- Separate manual cutoffs per:
  - Charging input  
  - Primary output  
  - Coil array control circuit  
- Helps isolate only specific sections while leaving others active if needed.

---

## 🔌 Basic Wiring Diagram (Textual)

```
[ IX-ZeroCell Power Bus ] --- [ Kill Switch ] --- [ Output Terminals ]
```

For sub-system isolation:

```
[ Charger Input ] --- [ Kill Switch 1 ]
[ Primary Output ] --- [ Kill Switch 2 ]
[ Control System ] --- [ Kill Switch 3 ]
```

---

## 🛡️ Build Notes

- Always mount switches in an easily accessible location.  
- Use proper wire gauge and terminal lugs rated for your system voltage and amperage.  
- Test switch action manually before powering up the main system.

---

## ⚠️ Real-World Considerations

- Mushroom switches preferred for emergency use—high visibility, large surface area.  
- IP65-rated enclosures recommended for outdoor builds or high-dust environments.  
- Label all switches clearly to avoid confusion during operation.

---

## ✅ Summary

- Simple but essential safety feature.  
- No software dependency—purely hardware.  
- Should always be present on real-world IX-ZeroCell builds.

---


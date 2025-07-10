# IX-ZeroCell – Fusing and Electrical Protection Strategies

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define physical and electrical safeguards to prevent damage from overcurrent, reverse polarity, surge backfeed, and ESD

---

## ⚡ Primary Threats Addressed

1. Overcurrent draw from boost converters (short circuit, overload)
2. Reverse voltage from external USB/DC loads
3. High-voltage kickbacks from piezo/tribo harvesting
4. ESD or inrush damaging supercaps or MPPT IC

---

## 🔥 Fuses & Resettable Protection

### 🔄 Polyfuse (PPTC)

- **Part:** MF-R050 or MF-R100 (Littelfuse)
- **Trip Current:** 0.5A or 1.0A respectively
- **Hold Current:** ~60–100% of trip rating

### Placement:

```txt
[Supercap Bank] → Polyfuse → Boost Converter Input
```

> Prevents fire risk or boost IC failure under sustained overload

---

### 🔌 USB Backfeed Protection

Most USB-C/A devices can **push power back** into your board if unprotected.

#### Solution: **Ideal Diode Controller or Schottky**

- **Part:** B240A Schottky Diode or  
  **Ideal Diode IC** (e.g. LTC4359 for advanced cases)

### Placement:

```txt
[Boost Output] → Diode → USB Port (A/C)
```

---

### ↩️ Reverse Polarity Clamp

If the user misconnects an external power source (USB-A host, 5V pin), reverse polarity can destroy everything.

#### Protection Methods:

1. **TVS Diode**
   - Part: **SMAJ5.0CA** (for 5V lines)
   - Bidirectional clamping across V+ and GND

2. **MOSFET Reverse Blocker**
   - P-Channel MOSFET in low-side orientation
   - Gate tied to GND, source to input — blocks reverse flow

---

## 🔋 Supercap Overvoltage Clamp

If supercaps exceed 2.7V per cell, they degrade rapidly.

#### Solutions:

- **TL431 Shunt Regulator** across each cell (optional)
- **Zener Diode (~3.3V, 1W)** across each cell (backup)
- Proper balancing system (already defined earlier)

---

## 🧩 Combined Protection Block Diagram

```txt
         +---------------------------+
         |       Supercap Bank      |
         +---------------------------+
                      |
                 [Polyfuse]
                      |
                 [Boost Regulator]
                      |
           +----------+-----------+
           |                      |
     [Schottky]             [TVS Diode]
           |                      |
     [USB-A Port]           [USB-C Port]
           |                      |
     External Load (Phone, Sensor, etc.)
```

---

## 🛠️ Sourcing Snapshot

| Component         | Suggested Part      | Role                    |
|--------------------|----------------------|--------------------------|
| Polyfuse           | MF-R050              | Self-resetting overcurrent  
| Schottky Diode     | B240A or SS34        | Reverse current block  
| TVS Clamp          | SMAJ5.0CA            | ESD / overvoltage line clamp  
| MOSFET (optional)  | IRF9540N             | Reverse polarity protection

---

## ✅ Summary

- Use **polyfuses** on every major rail before regulated output  
- Use **Schottky diodes or ideal diode ICs** on USB and DC outputs  
- Add **TVS clamps** at external connectors  
- Prevent **reverse polarity, shorts, and overloads** with minimal part count


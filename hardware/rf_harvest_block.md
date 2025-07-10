# IX-ZeroCell – RF Harvesting Block

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Document antenna designs, matching networks, and rectifier setup for RF energy harvesting into the MPPT core

---

## 📡 RF Energy Sources

Harvestable RF exists everywhere:

- WiFi / Bluetooth (~2.4 GHz)
- FM / TV Broadcast (50 MHz – 900 MHz)
- LTE / GSM towers (700 MHz – 2.5 GHz)
- Ambient EM from nearby electronics

---

## 📶 Antenna Array (Passive)

| Antenna Type | Qty | Target Band | Notes |
|--------------|-----|-------------|-------|
| Loop Antenna | 2   | 100 MHz – 300 MHz | Wideband low-frequency intake |
| Whip Antenna | 2   | 300 MHz – 1 GHz   | FM/TV/GSM range |
| PCB Meander  | 2   | 2.4 GHz           | WiFi/Bluetooth direct capture |

All antennas route into:

- **Schottky diode bridge**
- **Filter capacitor**
- Then feed **Node A** (MPPT input rail)

---

## 🔩 Matching Network

To improve RF-to-DC efficiency, matching is key.

### For 2.4 GHz PCB Antenna:
```txt
Antenna → 10pF cap → 6.8nH inductor → RF port
```

### For Whip Antennas:
```txt
Antenna → 33pF cap → 100nH inductor → RF port
```

> Use SMA or U.FL for testing, then move to soldered joints for production.

---

## ⚡ RF-DC Conversion

Use **ultra-low forward-voltage Schottky diodes** in a voltage-doubler or bridge config.

### Suggested Diode:
- **Part:** HSMS-2850 (Avago)
- **Vf:** ~0.15V at low current
- **Config:** Greinacher or Villard Doubler

### Output:
```txt
RF → Rectifier → 100nF ceramic cap → MPPT Node A
```

> Parallel multiple rectifier sets from each band — diodes prevent backfeed

---

## 🔋 Filtering

Each RF path should include:
- **100nF ceramic capacitor** at rectifier output
- Optional **220Ω resistor** to prevent current spikes

Add **clamp diodes** or **TVS** if located near high-field emitters.

---

## 📐 Layout Tips

- Use **short traces** for RF paths  
- Isolate each frequency band on separate PCB segment  
- Route all outputs to common **diode-mixed Node A**

### Ground Plane Strategy:

- Star grounding around Node A  
- Isolate high-frequency loops with stitched vias  
- Shielded box optional for FM/TV bands

---

## 🛒 Sourcing Notes

| Part            | Vendor             | Notes                    |
|------------------|---------------------|----------------------------|
| HSMS-2850 Diodes | Mouser, Digikey     | Low Vf, fast switching     |
| SMA Whip Antennas| SparkFun, Adafruit  | 315MHz / 868MHz preferred  |
| PCB 2.4 GHz Trace| Custom etched       | Simulate with KiCAD        |

---

## ✅ Summary

- Each RF band gets its own matched antenna + rectifier path  
- All rectified power is diode-mixed into MPPT VIN_DC  
- No battery buffering needed — MPPT handles pulsed input cleanly  
- Optional ferrite beads can be added if interference is detected


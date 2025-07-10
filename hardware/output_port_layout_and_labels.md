# IX-ZeroCell – Output Port Layout & Labeling

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Define all output ports, their placement, labels, fuse integration, and board edge alignment

---

## 📦 Output Port Summary

| Port Type | Use Case              | Connector         | Current Limit | Notes                 |
|-----------|------------------------|-------------------|---------------|------------------------|
| USB-A     | General 5V output      | Female Type A     | 500mA         | Standard orientation  
| USB-C     | Sink-mode only (power out) | Female Type C | 500mA         | No PD controller  
| JST-XH    | Fixed 3.3V rail        | 2-pin JST XH      | 300–500mA     | Logic sensors, MCUs  
| 2-pin HDR | Direct VOUT access     | 2.54mm male header| Full rail     | For prototyping

---

## 📐 Port Placement Guidelines

| Port      | Edge Distance | Orientation | Notes                      |
|-----------|----------------|-------------|-----------------------------|
| USB-A     | 1.0mm         | Right edge  | Port facing out  
| USB-C     | 1.0mm         | Bottom edge | Aligned for easy cable plug  
| JST-XH    | 3.0mm         | Top edge    | Insert from top  
| 2-pin HDR | 2.54mm grid   | User choice | Custom breakout options

---

## 🛡️ Protection Per Port

- **USB-A / USB-C:**  
  - TVS: SMBJ5.0CA across VBUS-GND  
  - PTC fuse: 500mA  
  - Reverse polarity: MOSFET

- **JST (3.3V rail):**  
  - TVS: SMBJ5.0CA  
  - PTC: 300mA  
  - Clearly labeled for sensor use only

- **2-pin header:**  
  - Exposed full VOUT (3.3V or 5V)  
  - User responsible for downstream load protection

---

## 🏷️ Silk Screen Labels

| Label        | Placement         | Font Size | Example             |
|--------------|-------------------|-----------|---------------------|
| `USB-A OUT`  | Top of connector  | 1.0mm     | Label above port  
| `USB-C OUT`  | Bottom of port    | 1.0mm     | Label below pads  
| `3V3 JST`    | Next to JST block | 0.8mm     | Optional arrow  
| `VOUT`       | Near 2-pin HDR    | 0.8mm     | Add polarity `+ -`

Use **bold sans-serif font** (e.g. Arial Narrow) for readability.

---

## 🧲 Mounting Notes

- Keep at least **0.75mm clearance** between ports  
- USB traces should be **differential pair tuned** if routing data (optional)  
- Add mounting holes if placing near board edge (3.2mm typical)

---

## 📦 BOM Notes

| Item           | Model             | Qty | Notes               |
|----------------|-------------------|-----|----------------------|
| USB-A          | TH female socket  | 1   | Right-angle preferred  
| USB-C          | SMD 16-pin        | 1   | Sink-only  
| JST-XH 2-pin   | Right angle       | 1   | 2.54 or 2.0mm pitch  
| Male header    | 2-pin, 2.54mm     | 1   | General use  
| Polyfuse       | 500mA / 300mA     | 3   | One per port  
| TVS Diodes     | SMBJ5.0CA         | 3   | One per VBUS rail

---

## ✅ Summary

- USB-A, USB-C, JST, and header ports laid out with safe spacing  
- Clear silk screen labeling with port functions and voltage ratings  
- Fuse + TVS per port = full protection stack  
- Aligned to board edges for enclosure design or plug-and-play use


> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – Surge Protection Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Protect IX-ZeroCell and connected devices from large-scale electrical surges such as lightning strikes, grid faults, or sudden load dumps.

---

## 💡 Why Surge Protection Matters

- IX-ZeroCell operates with magnetic pulse arrays and coil systems that can create unexpected surge events internally.
- External surges (e.g., nearby electrical storms or power grid faults) can feed through output terminals.
- Real-world deployments demand industrial-grade surge management.

---

## 🧱 Core Components

| Component            | Recommended Part               | Notes                           |
|---------------------|--------------------------------|---------------------------------|
| MOV (Metal Oxide Varistor) | 275V–500V MOV                  | Industrial surge suppression
| Gas Discharge Tube (GDT)   | 90V–350V GDTs                  | Primary lightning arrestor
| EMI/RFI Filter Module     | DIN Rail or PCB Mount Filters  | Reduces noise and high-frequency surges
| Series Inductor            | Custom Wound Toroid            | Helps absorb fast transients

---

## ⚙️ Configuration Options

### 1️⃣ MOV + GDT Cascade Setup

**Flow:**

```
[ Output Terminal ] — [ MOV ] — [ GDT ] — [ EMI Filter ] — [ Load ]
```

- MOV handles medium surges first.
- GDT triggers on high-voltage peaks above MOV limits.
- EMI/RFI filter cleans up the tail-end frequencies.

---

### 2️⃣ Industrial Panel-Mount Filter Blocks

- Pre-fabricated DIN-rail surge protection blocks rated for 100–500A systems can replace discrete MOV + GDT for cleaner builds.
- Costlier but more robust.

---

## 🛠️ Build Notes

- Always rate MOV and GDTs slightly above IX-ZeroCell’s maximum design output voltage but below dangerous levels for attached equipment.
- Gas Discharge Tubes have limited lifespan—test and replace periodically.
- Use proper ground bonding to chassis or earth ground for GDT discharge path.

---

## ⚠️ Real-World Considerations

- Do not install surge protection modules near high-EMF coil systems—keep them isolated physically to reduce false triggering.
- Over-spec rather than under-spec: Use 20–30% margin on voltage and current ratings.
- Document all surge components in final deployment paperwork for regulatory compliance.

---

## ✅ Summary

- MOV + GDT + EMI filter cascade = best-practice surge protection for IX-ZeroCell.
- Mandatory for grid-tied or outdoor deployments.
- Fits within standard output_app architecture module.

---

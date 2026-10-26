> **WITHDRAWN HISTORICAL DESIGN.** These notes contain unsupported output, compliance and build claims. They are retained for audit, not construction. Follow the current root README and active docs.

# IX-ZeroCell – High Voltage Cutoff Module

**Author:** Bryce Wooster
**License:** Apache-2.0
**Purpose:** Automatically disconnect capacitor bank from output circuits when voltage exceeds a safe threshold.

---

## ⚡ Why This Module Exists

- Capacitor banks in IX-ZeroCell can charge above safe output levels.
- Protect connected devices and prevent component damage.
- Ensures operational safety without constant manual monitoring.

---

## 🧱 Core Components

| Component            | Recommended Part      | Notes                            |
|---------------------|----------------------|----------------------------------|
| Voltage Comparator  | LM393 / LM339        | Compares cap bank voltage vs setpoint
| Relay Module        | 5V or 12V Coil Relay  | Disconnects load
| Reference Voltage   | Adjustable Zener or Potentiometer | Sets cutoff threshold
| Pull-down Resistors | 10k–100k Ω            | For stable comparator inputs

---

## 🔌 Basic Wiring Example

```txt
Cap Bank + --> Voltage Divider --> Comparator V+
Reference Voltage --> Comparator V-

Comparator Output --> Relay Driver Circuit --> Load Switch Relay

Cap Bank Ground --> Comparator Ground
```

---

## 🖥️ Example Threshold Setup

- Cap bank nominal voltage: **5.0V–5.5V**
- Cutoff voltage: **5.6V** (adjustable)

Voltage Divider Setup:

- **R1:** 10k Ω
- **R2:** 1k Ω

Calculates V+ input to comparator relative to cap bank voltage.
Adjust R1/R2 values to match system size.

---

## 🛠️ Configuration Notes

- **Relay should default to “On”** when comparator output is LOW.
- Once V+ exceeds V- (setpoint), comparator output switches, cutting relay.
- Add **hysteresis resistor** if needed to prevent rapid toggling near threshold.

---

## ⚠️ Safety Considerations

- Relays must handle IX-ZeroCell’s maximum output current.
- Comparator reference voltage must be stable and reliable.
- Mount cutoff module with adequate separation from high-frequency switching components to avoid interference.

---

## ✅ Summary

- Protects IX-ZeroCell system and connected equipment from overvoltage.
- Hardware-based — no software dependency required.
- Simple to implement using LM393 or similar ICs.

---

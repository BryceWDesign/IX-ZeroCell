# IX-ZeroCell – AC Relay Trigger Module

**Author:** Bryce Wooster  
**License:** Apache-2.0  
**Purpose:** Allows IX-ZeroCell’s capacitor bank to activate/deactivate high-voltage AC relays via a safe, isolated control circuit.

---

## ⚡ What This Does

- Converts low-voltage IX-ZeroCell output (2.2–5.5V) into **relay trigger signals**  
- Enables external switching of **AC 110V / 220V appliances**  
- Keeps capacitor bank physically isolated from high-voltage components  

---

## 🧱 Core Components

| Component          | Recommended Part     | Notes                           |
|--------------------|---------------------|---------------------------------|
| Opto-isolated Relay | SRD-05VDC-SL-C      | 5V coil, 10A @ 250VAC max  
| Transistor Driver  | 2N2222 / BC547       | NPN to control relay coil  
| Flyback Diode      | 1N4007               | Across relay coil terminals  
| Current-Limiting Resistor | 1kΩ – 4.7kΩ    | For transistor base  
| Optional: MCU Control | ESP32 / Arduino    | Logic timing or sensing  

---

## 🔌 Wiring Schematic

```txt
[Cap Bank +] --> [Relay Control Circuit +]
[Cap Bank -] --> [Relay Control Circuit GND]

[Relay NO] --> [AC Live In]
[Relay COM] --> [AC Load]
[Relay NC] --> (Unused)
```

- **NO** (Normally Open) controls whether the AC circuit is completed.  
- Trigger logic: Cap bank voltage → NPN transistor → Relay coil → Switches AC line.

---

## 🔥 Safety Considerations

- **Do not attempt direct capacitor-to-AC switching without isolation!**  
- Use **optically isolated modules** rated for 110–220V switching  
- Confirm relay ratings — most are 10A max at 250VAC  
- If unsure, use prebuilt relay modules (Songle, etc.)

---

## ⚙️ Control Logic Example

```c
// Pseudo-code
float volts = analogRead(A0) * (5.0 / 1023.0);

if (volts > 3.5) {
  digitalWrite(RELAY_PIN, HIGH);  // Activate relay
} else {
  digitalWrite(RELAY_PIN, LOW);   // Deactivate
}
```

Use logic to only engage the relay when sufficient cap charge is available.

---

## 🛡️ Best Practices

- **Debounce relay switching** — avoid rapid on/off cycling  
- Add **voltage detection circuit** for smart trigger thresholds  
- Place relay control **physically separate** from cap bank module  
- Use **double-insulated wires** rated for mains power  
- Ground your enclosure properly

---

## ✅ Summary

- Lets IX-ZeroCell control high-voltage AC appliances  
- Maintains full isolation between low- and high-voltage sections  
- Extends real-world application scope: hybrid energy control, automation, safety cutoffs  

---


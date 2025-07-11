# IX-ZeroCell Full Bill of Materials (BOM)

**Project:** IX-ZeroCell  
**Author:** Bryce Wooster  
**License:** Apache License 2.0  
**Last Updated:** July 11, 2025

---

## Primary Components

| Item Name                       | Quantity | Description                                       | Source Example                    | Notes                                    |
|---------------------------------|----------|---------------------------------------------------|-----------------------------------|------------------------------------------|
| Linear Flashlight Tubes         | 99       | Handshake/kinetic magnetic coil generator tubes   | Dyno flashlight tubes (x99)       | Prefer sealed aluminum housing types     |
| Neodymium Magnets (N52 Grade)   | 198      | 2 per tube, axial orientation                    | K&J Magnetics, Amazon             | 10mm x 5mm minimum                       |
| Custom Magnetic Pulse Coil      | 3        | Tesla-style rapid pulse driver coil               | Custom wound                      | Use oxygen-free copper wire              |
| Solid State Pulse Controller    | 1        | Microcontroller + IGBT/MOSFET trigger circuit    | DIY PCB                           | Flash pulse control, optional shielded   |
| Ultra-Capacitors                | 6        | 2.7V 500F or higher                              | Mouser, Digikey                   | Replace if unavailable with super caps   |
| RF Antenna Coil (Multi-band)    | 2        | Harvest incoming RF ambient energy                | eBay, Aliexpress                  | Suggest using telescoping whip combo     |
| Ferrite Core Rings              | 20       | EMI reduction + pulse shaping                     | Fair-Rite                         | Must be rated for high pulse currents    |
| Copper Bus Bars                 | 4        | Power distribution                                | McMaster-Carr                     | Solid copper or plated preferred         |
| Heat Sink Plates (Aluminum)     | 6        | Thermal management for pulse controller           | Local metal supplier              | Passive cooling                          |

---

## Structural Materials

| Item Name          | Quantity | Description                | Notes                           |
|--------------------|----------|----------------------------|---------------------------------|
| Aluminum Housing   | 1        | Main chassis enclosure     | Sofa/trashcan scale (approx. 4 ft tall, 2.5 ft diameter) |
| Polycarbonate Panels | 4      | Transparent service panels | Optional visual effect          |
| Shock-Absorb Mounts | 8       | Vibration isolation        | Rubber or silicone              |

---

## Fasteners, Wiring, and Consumables

| Item Name             | Quantity | Description                           |
|----------------------|----------|---------------------------------------|
| M4 Bolts/Nuts        | 100      | Stainless steel                       |
| 12 AWG Copper Wire   | 20m      | Power lines                           |
| 22 AWG Signal Wire   | 30m      | Control and sensor signals            |
| Solder               | 1 spool  | Lead-free                             |
| Thermal Paste        | 1 tube   | Heat sink application                 |

---

## Estimated Build Time

- **Prototype Assembly:** 72–96 hours (approx. 4–6 days active work, single person)
- **Wiring & Testing:** 18–24 hours
- **Housing/Chassis Work:** 8–12 hours

**Total Active Build Time: ~110–130 hours**

---

## Cost Estimate (USD)

| Category                  | Estimated Total |
|--------------------------|-----------------|
| Components               | $850–$1,200     |
| Housing/Frame Materials  | $300–$500       |
| Tooling (one-time cost)  | $150–$250       |
| Total (Excluding Labor)  | $1,300–$1,900   |

---

## Notes:

- Always verify local sourcing and material grades.  
- For highest efficiency, use high-tolerance capacitors and magnets.  
- Structural scale for 99 tubes places the unit around "small appliance / mini fridge size."

---

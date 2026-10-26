# Stack connection schedule

`WIRING.csv` enumerates 5790 power/control routes with unique IDs. It is a power-topology schedule, not a complete harness fabrication drawing. G01/G05 interfaces are logical unreleased assemblies; their labels do not pretend to be physical connector pinouts. Auxiliary, thermal and alarm harness fabrication is blocked by G01. See DESIGN.md and ASSEMBLY.md before using any route.

DC1924A terminal mapping: TP1 VIN, TP3 input PGND, TP2 VOUT, TP4 output PGND, TP5 /SHDN. Diode anodes join; cathode faces destination bus. No series-connected capacitor modules or panels.

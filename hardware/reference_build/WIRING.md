# Wiring schedule, ZC-D10

These are logical endpoint names with board silk-screen/test-point identities, not arbitrary IC pin numbers. All connections must be made with power isolated and the capacitor bank below 0.5 V.

| Wire | From | To | AWG | Maximum internal route, mm |
|---|---|---|---:|---:|
| W01 | PV1.PLUS | F1.IN | 16 | 200 |
| W02 | F1.OUT | S1.A_IN | 16 | 150 |
| W03 | S1.A_OUT | U1.VIN | 16 | 150 |
| W04 | PV1.MINUS | S1.B_IN | 16 | 200 |
| W05 | S1.B_OUT | U1.GND | 16 | 150 |
| W06 | U1.VOUT | F2.IN | 16 | 150 |
| W07 | F2.OUT | U2.E1_VIN | 16 | 150 |
| W08 | U1.GND | U2.E2_GND | 16 | 150 |
| W09 | U2.E3_VOUT | U3.VIN | 16 | 150 |
| W10 | U2.E4_GND | U3.GND | 16 | 150 |
| W11 | U3.VOUT | F3.IN | 16 | 150 |
| W12 | F3.OUT | S2.IN | 16 | 150 |
| W13 | S2.OUT | JOUTP.CORE | 16 | 150 |
| W14 | U3.GND | JOUTN.CORE | 16 | 150 |
| W15 | U1.VIN | RUV1.A | 24 | 75 |
| W16 | RUV1.B | U1.EN | 24 | 75 |
| W17 | U1.EN | RUV2.A | 24 | 75 |
| W18 | RUV2.B | U1.GND | 24 | 75 |
| W19 | U2.E9_VCAP | F4.IN | 20 | 150 |
| W20 | F4.OUT | S3.IN | 20 | 150 |
| W21 | S3.OUT | RDIS.A | 20 | 150 |
| W22 | RDIS.B | U2.E10_GND | 20 | 150 |

Use TWO 20 AWG 50 mm pigtails at each module power node. U1 VOUT, U3 VIN and U3 VOUT use one WAGO 221-413 each. U1 VIN, U1 GND and U3 GND use one WAGO 221-415 each to include the divider and return branches. Leave unused lever positions closed and empty.

At the small U1/U3 pads, solder the two separate 20 AWG pigtails to duplicate same-name power pads; join them to the trunk with the indicated lever connector. Do not install one single header pin as a 4 A output path. W15/W18 are signal-divider branches, not power trunks. Fuse-holder leads and switch solder lugs use soldered, insulated and strain-relieved joints.

U2 E1=VIN, E2=GND, E3=VOUT, E4=GND, E9=VCAP, E10=GND are read from the board schematic. Use those actual labels. No wire attaches to intermediate cell taps for the main power path. E9/E10 are used only for metering and the protected service bleed branch.

Set U2 JP1 to INTVCC for standalone pull-ups; leave its I2C header and DC590 connection disconnected for the standalone build. Confirm the delivered board has the documented standalone pull-up parts before relying on this state.

Leave U1/U3 VRP and PG unconnected and insulated. U3 EN stays unconnected, using its factory default enable. U1 EN connects only to its divider. Normal positions are S1 ON, S2 ON, S3 OFF.

JOUTP.LOAD is external device positive; JOUTN.LOAD is external device return. Neither terminal is USB data, mains neutral, earth or a charging-negotiation interface. Do not connect another power supply to the output.

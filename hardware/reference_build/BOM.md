# ZC-D10 complete assembly-level bill of materials

Version 0.2.0, expanded in place. Build: battery-free, solar-fed 5 V DC source with supercapacitor interruption buffering. Nominal design target: 10 W; 20 W is a separate qualification target. No ZeroCell hardware has been measured in this session.

Buy U1/U2/U3 as populated boards. Their internal chips, inductors, passives and stock capacitors are already included, and must not be bought a second time. The only required modification inside U2 is RFB1 replacing R3. This is a complete module assembly BOM, not a released custom-PCB fabrication BOM.

Exact manufacturer part numbers identify the active modules. Specification-selected commodity items specify quantity, electrical rating and material; current vendor stock and prices are not claimed.

| Ref | Qty | Manufacturer / part or purchase specification | Use |
|---|---:|---|---|
| PV1 | 1 | [ACOPOWER; HY050-12M](https://www.acopower.com/products/hy050-12m) | 50 W photovoltaic module; primary site-dependent energy input |
| U1 | 1 | [Pololu; D36V50F12 / item 4095](https://www.pololu.com/product/4095) | Assembled 12 V buck regulator, fitted with the external enable divider below |
| U2 | 1 | [Analog Devices; DC1937B](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/dc1937b.html) | Assembled LTC3350 board; replace R3 with RFB1 to set nominal 6.5 V backup; retain stock four 10 F capacitors and 2 A input limit |
| U3 | 1 | [Pololu; D36V50F5 / item 4091](https://www.pololu.com/product/4091) | Assembled final 5 V buck regulator |
| RUV1 | 1 | [specification-selected; 2.20 kohm, 1%, 1 W, axial metal film](https://www.pololu.com/product/4095) | PV input to U1 EN; external resistor overrides most internal pull-up tolerance |
| RUV2 | 1 | [specification-selected; 191 ohm, 1%, 0.25 W, axial metal film](https://www.pololu.com/product/4095) | U1 EN to ground; hysteretic source-voltage cutoff divider |
| RDIS | 1 | [specification-selected; 100 ohm, 5%, 5 W flameproof wirewound](https://www.analog.com/media/en/technical-documentation/user-guides/dc1937bfa.pdf) | Service-only capacitor discharge resistor, switched, 1 W at 10 V |
| F1 | 1 | [Littelfuse; 0297005.H; 5 A MINI blade fuse, 32 V DC](https://www.littelfuse.com/assetdocs/littelfuse_datasheet_297_mini32v.pdf?assetguid=42c9dd21-a88e-4328-8e67-2f832444faf1) | PV positive input protection |
| F2 | 1 | [Littelfuse; 0297003.H; 3 A MINI blade fuse, 32 V DC](https://www.littelfuse.com/assetdocs/littelfuse_datasheet_297_mini32v.pdf?assetguid=42c9dd21-a88e-4328-8e67-2f832444faf1) | 12 V link protection, downstream of U1 |
| F3 | 1 | [Littelfuse; 0297005.H; 5 A MINI blade fuse, 32 V DC](https://www.littelfuse.com/assetdocs/littelfuse_datasheet_297_mini32v.pdf?assetguid=42c9dd21-a88e-4328-8e67-2f832444faf1) | 5 V output cable protection |
| F4 | 1 | [Littelfuse; 0297002.H; 2 A MINI blade fuse, 32 V DC](https://www.littelfuse.com/assetdocs/littelfuse_datasheet_297_mini32v.pdf?assetguid=42c9dd21-a88e-4328-8e67-2f832444faf1) | Service discharge branch protection |
| FH1-FH4 | 4 | specification-selected; Insulated MINI-blade inline holder, at least 32 V DC / 10 A, 16 AWG leads | One holder for each fuse; fuse body and holder must be the same MINI format |
| S1 | 1 | specification-selected; DPST maintained switch, explicit DC rating at least 30 V / 5 A | Disconnect both PV conductors, never substitute AC-only rating |
| S2 | 1 | specification-selected; SPST maintained switch, explicit DC rating at least 30 V / 10 A | Output enable, manual hard disconnect |
| S3 | 1 | specification-selected; SPST maintained covered switch, explicit DC rating at least 30 V / 5 A | Service discharge only; must be OFF for normal operation |
| JPAIR | 1 | [ACOPOWER-compatible; Matched pair PV connector to bare-wire adapter leads, 12 AWG, 1 m](https://www.acopower.com/products/hy050-12m) | Buy the exact mating connector type supplied on the selected panel; do not mix incompatible nominal MC4 types |
| JC1-JC3 | 3 | [WAGO; 221-413](https://www.wago.com/global/installation-terminal-blocks-and-connectors/splicing-connector-with-levers/p/221-413) | Three-way paired-pad joins: U1 VOUT, U3 VIN, U3 VOUT |
| JOUTP,JOUTN | 2 | [WAGO; 221-412](https://www.wago.com/global/installation-terminal-blocks-and-connectors/splicing-connector-with-levers/p/221-412) | Separate insulated two-way output connections, one positive and one negative |
| WIRE16R | 2 | specification-selected; 16 AWG stranded copper, red, 105 C insulation | Metres, trunk and fuse/switch connections; no copper-clad aluminium |
| WIRE16B | 2 | specification-selected; 16 AWG stranded copper, black, 105 C insulation | Metres, return conductors |
| WIRE20R | 1 | specification-selected; 20 AWG stranded copper, red, 105 C insulation | Metre, paired 50 mm pigtails at duplicated module power pads |
| WIRE20B | 1 | specification-selected; 20 AWG stranded copper, black, 105 C insulation | Metre, paired 50 mm module ground pigtails |
| WIRE24 | 1 | specification-selected; 24 AWG stranded copper, insulated, 0.5 m | Quantity is one 0.5 m length, EN divider connections only |
| PB1 | 1 | specification-selected; Unconnected-pad FR4 perfboard, 25 x 25 mm minimum | Mount only RUV1 and RUV2; no solderless power breadboard |
| CASE1 | 1 | specification-selected; Insulating enclosure, internal free space at least 300 x 250 x 100 mm | Dry indoor, ventilated, removable insulated lid; no claimed IP rating |
| BASE1 | 1 | specification-selected; Insulating mounting sheet, 250 x 200 x 3 mm | FR4 or polycarbonate mounting plate inside enclosure |
| MOUNT1 | 8 | specification-selected; M2 x 10 mm nylon standoff, matching screws and nuts | Three holes per Pololu board plus two perfboard mounts; eight complete sets |
| MOUNT2 | 4 | [Keystone or specification equivalent; 8833 snap-in nylon standoff](https://www.analog.com/media/en/technical-documentation/user-guides/dc1937bfa.pdf) | Use the four included U2 standoffs if supplied; otherwise procure four matching items |
| CLAMP1 | 12 | specification-selected; Insulating cable tie mounting base with cable tie | Twelve complete strain-relief sets; no adhesive touching hot parts |
| GLAND1 | 2 | specification-selected; Insulating cable gland matched to actual cable jacket diameter | One PV entry and one output exit, jacket retained without exposing conductors |
| INSUL1 | 1 | specification-selected; 3:1 heat-shrink assortment, 2/4/6 mm nominal, 1 m total | Insulate every soldered terminal and all unused live service points |
| SOLDER1 | 1 | specification-selected; Electronics solder and compatible flux, one small pack | Hand assembly of module pigtails and resistor board |
| LABEL1 | 1 | specification-selected; Durable insulated label sheet | PV polarity, 5 V output, input/output fuse values, service bleed switch, unit identifier |
| JC4-JC6 | 3 | [WAGO; 221-415](https://www.wago.com/global/installation-terminal-blocks-and-connectors/splicing-connector-with-levers/p/221-415) | Five-way joins: U1 VIN, U1 GND, U3 GND; accommodate divider and multiple return trunks |
| RFB1 | 1 | [Vishay or exact specification equivalent; CRCW0402715KFKED; 715 kohm, 1%, 0402, at least 1/16 W](https://www.analog.com/media/en/technical-documentation/user-guides/dc1937bfa.pdf) | REPLACES factory U2 R3 (649 kohm); keep factory U2 R4 (162 kohm); not a parallel addition |

## Included storage and regulator values

- U2 stock bank: four 10 F cells in series, 2.5 F equivalent; factory float 10 V. It is not a four-by-3000 F bank.
- U2 R3 replacement: 715 kohm; existing R4: 162 kohm. Nominal backup setpoint is 1.2 x (1 + 715/162) = 6.496 V.
- U2 input-current setting remains factory 2 A. Do not increase it as part of this build.
- U1 divider uses the internal nominal 100 kohm EN pull-up in parallel with external 2.20 kohm. External bottom resistance is 191 ohm. Nominal turn-on is 16.57 V and turn-off 14.72 V, using typical 1.35/1.20 V EN thresholds. These are calculated nominal values, requiring measurement.
- RUV1 maximum dissipation at 30 V PV input is below 0.4 W; its 1 W rating provides margin. The fixed voltage window is not MPPT.
- RDIS dissipates 1 W initially at 10 V. With 2.5 F equivalent capacitance, ideal discharge from 10 to 0.5 V takes about 749 seconds. Verify voltage before work.

## Test apparatus, separate from the installed unit

| Equipment | Quantity | Minimum capability / purpose |
|---|---:|---|
| Current-limited isolated bench supply | 1 | 0-25 V DC, at least 3 A; adjustable voltage and current limit |
| DC voltmeters | 2 | Resolve 10 mV on 0-30 V; calibration/uncertainty recorded |
| Input/output DC power measurement channels | 2 | Cover 0-30 V, 0-5 A, simultaneous logging; record any meter supply power |
| Electronic load | 1 | Constant-power 0-25 W, constant-current 0-5 A, rated for 5 V operation; this is the canonical load for qualification |
| Oscilloscope | 1 | Two or more channels, capture source loss and output rail; use correctly grounded or differential probes |
| Temperature probes | 3 | Monitor U1, U2 and U3; baseline at room ambient, no claimed certification |
| Fine soldering equipment | 1 set | Magnification, tweezers, ESD provisions, solder/flux, fine tip or hot air for 0402 replacement |
| Wire tools | 1 set | Correct stripper, cutter, soldering and mechanical strain-relief tools |

A safe optional passive load is two ARCOL/Ohmite HS50 2R5 F resistors, in parallel, mounted according to the manufacturer thermal instructions: 1.25 ohm nominal and about 20 W at exactly 5 V. Use the actual measured resistance and voltage to compute power. It is not a constant-power load. Do not place hot load resistors inside the power-unit enclosure.

The user equipment to be powered is external to this BOM. The delivered output is labelled 5 V DC through separate insulated terminals; no USB-C PD or charging-protocol implementation is implied.

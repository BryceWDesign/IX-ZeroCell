# ZC-S1000 assembly-scope BOM

Assembly-scope inventory, not a closed component-level BOM for unreleased control/protection assemblies. **Procurement release: NO.** Rows marked Gxx require completed design before purchase/energization. No unselected assembly is represented as a ready-made product. A populated board includes its manufacturer internal BOM; replacement parts are additional. All quantities exclude spares. Prices and availability are not asserted.

| Ref | Per scope | Stack quantity | Part or purchase specification | Status |
|---|---:|---:|---|---|
| PV1-PV3 | 3 / channel | 60 | REC420AA PURE-R, 420 W | specified_component |
| A1-A4 | 4 / channel | 80 | ADI DC1924A populated board | specified_component |
| C01-C60 | 60 / channel | 1200 | Eaton XLR-48R6167-R, 166 F, 48.6 V | specified_component |
| RC01-RC60 | 60 / channel | 1200 | TE HSC2002R2J, 2.2 ohm 200 W 5% | specified_component |
| FC01-FC60 | 60 / channel | 1200 | Littelfuse KLKD, 2 A DC fuse | coordination_pending |
| HC01-HC60 | 60 / channel | 1200 | Finger-safe fuse holder matched to KLKD 10x38 mm; >=100 VDC and bank fault duty | installation_selection |
| D1-D5 | 5 / channel | 100 | STPS10H100CFP; join both anodes; common cathode | specified_component |
| HD1-HD5 | 5 / channel | 100 | Insulated mounting/heat sink assembly for TO-220FP diode; validate junction temperature at measured loss | thermal_selection |
| RB | 1 / channel | 20 | 1.2 ohm, 1%, >=50 W aluminium-housed wirewound resistor; voltage and pulse rating coordinated with fuses | purchase_specification |
| FPV1-FPV3 | 3 / channel | 60 | Littelfuse KLKD, 15 A DC | coordination_pending |
| FPVMAIN | 1 / channel | 20 | Littelfuse KLKD, 30 A DC | coordination_pending |
| FA1 | 1 / channel | 20 | Littelfuse KLKD, 5 A DC | coordination_pending |
| FA2-FA3 | 2 / channel | 40 | Littelfuse KLKD, 10 A DC | coordination_pending |
| FBANK | 1 / channel | 20 | Littelfuse KLKD, 15 A DC | coordination_pending |
| FGATE | 1 / channel | 20 | Littelfuse KLKD, 5 A DC | coordination_pending |
| FA4 | 1 / channel | 20 | Littelfuse KLKD, 5 A DC | coordination_pending |
| FOUT_LOCAL-FOUT_BUS | 2 / channel | 40 | Littelfuse KLKD, 2 A DC | coordination_pending |
| HF | 12 / channel | 240 | DC fuse holders matching non-module KLKD fuses above; verify interrupt duty | installation_selection |
| K1 | 1 / channel | 20 | TE EV200AAANA, normally open; coil fed only from PV auxiliary | driver_coordination_pending |
| AUX12 | 1 / channel | 20 | Traco TEN 60-7212WIR, 36–160 V input, 12 V output | specified_component |
| AUX5P-AUX5B | 2 / channel | 40 | RECOM R-78HB5.0-0.5, 9–72 V input, 5 V output | specified_component |
| AUXPROTECT | 1 / channel | 20 | Dedicated PV/bank auxiliary branch fuses, output OR diodes, decoupling and pickup-current allowance | G01_unreleased |
| A5 | 1 / channel | 20 | LM5069-1 based gate; CSD19536KTT candidate pass FET; independent UVLO/OVLO option | G01_unreleased |
| OVCTRL | 1 / channel | 20 | TLV1702 + LM4040A25; nominal charge divider 178 kohm/10 kohm; latched independent cutoff | G01_unreleased |
| TS01-TS60 | 60 / channel | 1200 | Normally closed, calibrated 45 C body-temperature switch with supervised open-circuit wiring | G01_unreleased |
| ALARM | 1 / channel | 20 | 60-module open-collector alarm and supervised continuity harness; <=5 mA sink per module | G01_unreleased |
| R49_A1 | 1 / channel | 20 | 86.6 kohm, 0.1%, 0603 | specified_component |
| R49_A2_A3 | 2 / channel | 40 | 34.8 kohm, 0.1%, 0603 | specified_component |
| R49_A4 | 1 / channel | 20 | 143 kohm, 0.1%, 0603 plus 10 kohm sealed multi-turn trim | specified_component |
| R13_A1_A4 | 2 / channel | 40 | 392 kohm, 0.1%, 0603 plus 20 kohm sealed multi-turn trim | specified_component |
| R13_A2_A3 | 2 / channel | 40 | 374 kohm, 0.1%, 0603 plus 5 kohm sealed multi-turn trim | specified_component |
| R16_A1_A4 | 4 / channel | 80 | 10.0 kohm, 0.1%, 0603 | specified_component |
| R53_A1 | 1 / channel | 20 | 590 kohm, 0.1%, 0603 | specified_component |
| R53_A2_A3 | 2 / channel | 40 | 649 kohm, 0.1%, 0603 | specified_component |
| R54_A1_A3 | 3 / channel | 60 | 20.0 kohm, 0.1%, 0603 | specified_component |
| R11_A1_A3 | 3 / channel | 60 | 590 kohm, 0.1%, 0603 | specified_component |
| R11_A4 | 1 / channel | 20 | 294 kohm, 0.1%, 0603 | specified_component |
| R14_A1_A4 | 4 / channel | 80 | 20.0 kohm, 0.1%, 0603 | specified_component |
| ISOLATORS | 1 / channel | 20 | Lockable DC-rated PV/bank service isolation set; ratings derived from complete fault study | G03_G06_unreleased |
| RACK | 4 / channel | 80 | Anchored rack >=300 kg rated load, fifteen modules per rack, insulated covers and individual restraints | G06_unreleased |
| CHANNEL_HARNESS | 1 / channel | 20 | Equal-length module branches; 2.5 mm2 copper reference, trunk 6 mm2 reference, >=100 V insulation; final lengths/ampacity site-designed | G06_unreleased |
| SECTION | 4 / stack | 4 | Five-channel busbar/return with covered terminals, rated section disconnect/protection | G05_unreleased |
| MAIN | 1 / stack | 1 | Main DC disconnect, load protection, independent output OV/UV shutdown and precharge | G05_unreleased |
| CENTRAL | 1 / stack | 1 | Metering and optional supervisory logger within total 50 W common loss budget | G05_unreleased |
| SITE | 1 / stack | 1 | PV mounting, matched connectors, conductor routing, bonding, enclosures, cooling and structural plan | G06_unreleased |
| TEST | 1 / stack | 1 | Calibrated 80 V current-limited supply; >=1.5 kW 60 V DC load; synchronized meters; differential probes; temperature logging; limited-energy fault fixture | equipment_specification |

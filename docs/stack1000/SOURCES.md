# Primary design references, checked 26 October 2026

These documents support component facts and circuit selection, not assembled ZeroCell performance. Vendor drawings govern their populated boards. The project-authored topology and calculations are not vendor endorsements. Do not confuse manufacturer typical values with project acceptance bounds.

| Source | Use |
|---|---|
| [ADI DC1924A manual and schematic](https://www.analog.com/media/en/technical-documentation/user-guides/dc1924afa.pdf) | Populated board, terminal/rework designators, reduced-load low-input operation |
| [LT8705 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/8705ff.pdf) | Voltage/current feedback, UVLO and mode behavior |
| [Eaton XLR-48 datasheet](https://www.eaton.com/content/dam/eaton/products/electronic-components/resources/data-sheet/eaton-xlr-48-supercapacitor-module-data-sheet.pdf) | Module capacitance, voltage, ESR/leakage reference |
| [Eaton installation manual](https://www.eaton.com/content/dam/eaton/products/electronic-components/resources/technical/eaton-xlr-48-energy-storage-module-instruction-manual.pdf) | Module alarm, mounting, handling/discharge requirements |
| [Eaton product aid](https://www.eaton.com/content/dam/eaton/products/electronic-components/resources/product-aid/eaton-xlr-supercapacitor-module-product-aid.pdf) | 14.7 kg module mass reference |
| [REC Alpha Pure-R](https://www.recgroup.com/sites/default/files/2025-01/Web_DS_REC_Alpha_Pure-R_EN.pdf) | 420 W panel electrical and mechanical data |
| [TI LM5069](https://www.ti.com/lit/ds/symlink/lm5069.pdf) | Bank gate reference, timing/SOA requirements |
| [TI CSD19536KTT](https://www.ti.com/lit/ds/symlink/csd19536ktt.pdf) | Candidate pass FET, not an approved SOA selection |
| [ST STPS10H100C](https://www.st.com/resource/en/datasheet/stps10h100c.pdf) | Blocking diode package/ratings |
| [Littelfuse KLKD](https://www.littelfuse.com/assetdocs/klkd-datasheet?assetguid=7b52eebb-c7cc-43df-a8da-9682a338e0f6) | DC fuse family; coordination remains required |
| [TE HSC2002R2J](https://www.te.com/en/product-1-1630019-6.html) | Module branch resistor identity |
| [TE EV200AAANA](https://www.te.com/en/product-1618002-7.html) | Source contactor reference |
| [Traco TEN 60WIR](https://www.tracopower.com/ten60wir-datasheet) | PV-only auxiliary converter |
| [RECOM R-78HB5.0-0.5](https://recom-power.com/en/products/switching-regulators/switching-regulators-sip/rec-p-R-78HB5.0-0.5.html) | Logic auxiliary regulators |
| [TLV1702](https://www.ti.com/product/TLV1702) and [LM4040](https://www.ti.com/lit/ds/symlink/lm4040.pdf) | Independent cutoff reference components |

Alternative screened but not selected: [Bel VHK100W-Q48-S48](https://www.belfuse.com/media/datasheets/products/power-supplies/VHK100W.pdf). Its typical 85% module efficiency leaves no established margin to an 85% complete-path floor after sharing/blocking losses; selection would require a revised energy budget. Do not treat it as a drop-in interchangeable BOM item.

Prior 50 W and stack concept A documents are included locally for traceability. Revision B settings and quantities take precedence. No third-party proprietary CAD or SPICE models were copied into this Apache-2.0 repository; project SPICE files are independently authored behavioral models.

> HISTORICAL CONCEPT A. Superseded by [revision B](DESIGN.md). Do not use its quantities or custom output-stage instructions for assembly.

# IX-ZeroCell: twenty-channel 1,000 W functional design

26 October 2026. Revision A. Calculated architecture; not a tested assembly or fabrication release.

This scales the solar/supercapacitor 50 W design into one battery-free, nominal 48 V DC supply delivering 1,000 W at the load terminals. “United” means electrically combined operation. It does not mean US mains output: no 120 V AC inverter or grid interface is included. Sunlight supplies the energy. The original RF/static harvesting claims are not established by this design.

The original 50 W unit was itself an unbuilt functional design. Twenty copies do not convert that status into verified hardware. This document specifies the revised interfaces, energy sizing, controls and validation needed for an integrated prototype.

## Output and operating envelope

| Parameter | Requirement |
|---|---|
| Useful continuous output | 1,000 W DC at the external terminals |
| Output voltage | Nominal 48 V; accepted steady range 46.5–50.5 V |
| Load current | 20.83 A at 48 V; 21.51 A at 46.5 V |
| Channels | 20 independently protected source/storage channels |
| Channel delivery | Approximately 52.5 W normally; qualify 55 W continuous per channel |
| Combined channel capacity | 1,100 W; reserve 50 W for shared losses/controls and 50 W additional headroom |
| No-sun service | 16 hours, starting with every bank at or above 45.5 V |
| Storage temperature | Retain prior qualified target of 10–35 °C |
| Replenishment envelope | Each channel receives 320 W of conditioned source power for eight hours per day |
| Battery | None; electrostatic EDLC storage |

The replenishment requirement is an actual power/time envelope, not eight hours of daylight or a panel nameplate claim. Site weather has not been qualified. Unequal shade can exhaust one channel earlier even when total sunlight appears adequate. All twenty channels must satisfy their individual energy envelope.

## Architecture and changes from the 50 W design

Repeat the following channel twenty times:

1. Three parallel REC420AA PURE-R panels feed the existing A1 direct-supply and A2/A3 capacitor-charge architecture.
2. Retain the separate bank of 56 Eaton XLR-48R6167-R modules, branch fuses/resistors, charge cutoff and alarms.
3. Replace the Traco 12 V output stage A4 with a **custom LT8705-based, nonisolated, current-controlled buck-boost stage**. Required input range is 18–55 V, operating bank range approximately 22–46 V, and output range extends to 50.5 V. Specify a 100 W power-stage thermal capability, operated at no more than 55 W continuous channel delivery. The existing DC1924A is not approved unchanged for the low-input end of this new role.
4. Feed its output through reverse-current blocking, an independent overvoltage/disconnect stage and a branch fuse to the common output bus. Use LM5050-1 with an appropriately rated external MOSFET as the reverse-blocking reference. This device does not perform current sharing, forward overvoltage isolation or fault-current limiting by itself.
5. Use a separate back-to-back MOSFET disconnect with independent comparator/latch to interrupt forward faults. Set the channel overvoltage trip target to 52 V, with component tolerances and turnoff overshoot qualified below downstream limits. Select 100 V power semiconductors and appropriately derated capacitors after the transient study.

Connect output returns to a defined star return. This is not galvanic isolation: positive storage buses remain separate, and each connects to the common bus only through its controlled converter and protective devices. Do not parallel the twenty raw capacitor positive buses. Use isolated communication interfaces where required by ground offsets and wiring routes.

Combine channels into four five-channel distribution sections for wiring and service, then connect those sections to the main bus. These are electrical sections, not five-unit structural stacks. Add a main load disconnect and metering at the external load terminals. A failed branch must be disconnected at the combiner end as well as protected against its own source: a source-end fuse alone does not protect a cable from bus backfeed.

## Sharing and regulation

Implement local output droop using measured output current:

`V_channel_command = 50.0 V - (1.2 ohm × I_channel)`

At approximately 1.08 A per channel, this gives approximately 48.7 V before feeder drop. The resistance is a control law, not a dissipative 1.2 ohm series resistor. Feed the measured-current correction into the LT8705 voltage-command circuit; independently enforce the 55 W output ceiling and a 1.25 A maximum output-current ceiling. Power and current limits take priority over droop.

Calibrate channel intercept error to no more than ±20 mV and droop slope error to ±1%; constrain unequal feeder drop so the combined sharing error remains within the available 55 W per-channel ceiling. These are requirements, not assumed manufacturer guarantees. A slow supervisory trim may equalize energy use, but local droop and hardware limits must operate without communications. Clamp supervisory trim authority and qualify stability of all twenty interacting loops. Do not tie together twenty unmodified voltage-feedback outputs and assume they share equally.

At a normal total channel delivery of 1,050 W, the shared combiner, controls and distribution may consume no more than 50 W. Meter actual useful output independently. Target main output loop resistance at or below 0.02 ohm, which dissipates approximately 9.3 W at 21.51 A; remaining loss allowance covers branch paths, contacts and central electronics. Select final wire cross-sections from route, temperature, installation and voltage drop; this is not a wire-ampacity release.

All channels start with their output disconnects open. Precharge the common output capacitance under current limit, establish a valid bus, then enable channels in sequence with soft start. Qualify startup into an already energized bus and a constant-power load. Avoid startup hunting by keeping the external load disconnected until the available channels can support it. During source loss, each channel transfers to its own bank using its retained direct/storage supply selection.

If a channel fails, isolate it. With nineteen channels, 19 × 55 = 1,045 W, less than the 1,050 W worst-case internal requirement. Therefore this design does **not** promise full-power single-channel-fault operation. Conservatively reduce useful load to at most 950 W after one loss, and further if any remaining channel lacks energy. A twenty-first complete channel is the straightforward expansion for a separately qualified N+1 design.

## Energy calculation

Keep all 56 capacitor modules per channel. Use 80% of nominal capacitance, so effective channel capacitance is 7,436.8 F. The conservative usable window remains 45.5 V to 22 V:

`E_channel = 0.5 × 7436.8 × (45.5² - 22²) / 3600 = 1,638.42 Wh`

Budget at the full 55 W channel delivery, even though normal operation calls for about 52.5 W:

| Per-channel term | Allowance |
|---|---:|
| Output path input at 85% minimum efficiency | 64.706 W |
| Local controls, including new sharing circuits | 4.000 W |
| Leakage, 56 × 10 mA × 47.5 V | 26.600 W |
| Branch resistance/ESR loss | 0.800 W |
| Total conservative storage draw | 96.106 W |
| Sixteen-hour storage demand | 1,537.69 Wh |
| Remaining usable energy | 100.73 Wh |

Across twenty channels, usable storage is **32.7684 kWh**, against **30.7539 kWh** of conservatively bounded sixteen-hour demand. Margin is approximately 6.55% of demand. The leakage ceiling is a required measured acceptance condition, not a guaranteed Eaton maximum. Any failed efficiency, leakage, capacitance or auxiliary-power bound invalidates this sizing.

Twenty-four-hour conservative demand is 46.1308 kWh. The stipulated conditioned source supplies 20 × 320 W × 8 h = 51.2 kWh. Applying a further pessimistic 95% charge efficiency to all that energy leaves 48.64 kWh, above the daily bound. This is an energy check; charger current limits and the timing of solar delivery still require verification.

As a screening input, require at least 380 W actual PV electrical power per channel during that window. Reserving 10 W for daylight auxiliaries and assuming 90% source conversion leaves 333 W, above the 320 W conditioned-power requirement. Verify these separate path measurements rather than counting the same energy twice. Empty-bank initial charging can take more than one day.

Requalify A1 delivery, A5 pass-device SOA/current limit and input inrush for the new load. Do not carry over the previous 12 V converter, output fuse or A5 timing values without rechecking them. The 85% efficiency bound includes the revised useful-output path and blocking losses up to the channel connector; the 50 W shared allowance covers downstream distribution and central control.

## Physical scale

| Item | Twenty-channel total |
|---|---:|
| Solar panels | 60 × 420 W = 25.2 kWp |
| Panel surface | About 116.05 m² / 1,249 ft², excluding gaps, access and tilt spacing |
| Eaton capacitor modules | 1,120 |
| Capacitor mass | 16,464 kg / 16.46 metric tonnes, excluding frames |
| Storage racks at previous allocation | 80 racks, fourteen modules each |
| Existing PV conversion boards | 60, before new output circuitry |
| New output converters | 20 |
| Module branch resistor/fuse pairs | 1,120 |

The earlier 2 × 2 × 6 ft cabinet size was only a planning allowance. Eighty such footprints would total 320 ft² before aisles or electronics, but no rack/floor/anchorage design has been completed. This is a stationary installation. Multiplying the earlier architecture establishes a baseline, not the smallest or cheapest possible 1 kW system.

## Repository material actually used

Reviewed the supplied IX-ZeroCell-v0.2.0-Emergency-Power-Engineering ZIP. Executed its unmodified `ix_zerocell/power.py` and supporting package in scratch with new sizing parameters; the original repository/ZIP was not modified.

Model settings: one equivalent module in series, 56 parallel; 132.8 F per module; 45.5 V maximum; 22 V cutoff; 2.32 ohm per branch including conservative resistance allowance; 0.56 A aggregate leakage; 9 A charge limit; 4.5 A discharge limit; 95% charge efficiency; 85% output efficiency; 55 W delivered; 4 W local controls. Each 60-second step used sixteen hours without source followed by eight hours of a 380 W source, 90% source efficiency and a 320 W conditioned-output cap. Repeat three times.

Calculated minimum bank voltage was 26.2023 V each cycle, returning to 45.5 V at each day's end. Unserved output was zero to floating-point precision; maximum per-step energy residual was 4.66e-10 J. The time-step model uses voltage-dependent leakage, so it is less pessimistic than the constant worst-case leakage bound above. It models one representative channel; multiplying results does not simulate twenty converter control loops, unequal channels, faults or weather.

Reviewed `firmware/power_guard.h`. Reuse its principles of stale-data rejection, hardware permits, latched faults and conservative energy budgeting. Do not deploy it unchanged: it explicitly supports at most four sensed cells, with a four-element sample array and low-power default limits. Eaton internal cell monitoring, twenty-channel dispatch and bus protection need a new instrumentation/control mapping. No firmware port or bench validation was performed here.

Also read the available `zeroCell-integrated-feedback.md` and Solar Thermoacoustic “Bagpipe” Generator README. The former does not provide measured harvest curves establishing power for this stack; the latter describes an evaluation concept with unresolved geometry. Neither is credited with additional watts. This review covers retrieved materials, not every repository ever created.

## Required hardware release work

The new output stage is specified functionally, **not circuit-complete**. Outstanding work includes its power-component selection, current-sense/feedback schematic, compensation and layout; forward-fault disconnect; precharge and bus capacitance; fuse coordination and bus interrupt ratings; and mechanical/thermal design. The prior 50 W design's unresolved leakage, alarms, thermal switches, pass-FET SOA and resistor/fuse pulse checks also remain open.

Validate in this order: one revised 55 W channel over full input/temperature range; two-channel sharing and startup; five-channel section; twenty-channel combined operation. Demonstrate tolerance extremes and weak-bank load reduction. Test fault isolation using bounded-energy fixtures before connecting full storage. Then run 1,000 W at the external terminals for sixteen hours with solar disconnected, followed by at least three documented replenishment cycles without declining energy. Record per-channel energy, maximum temperatures, output voltage, actual input power and every auxiliary feed.

A 1,000 W AC load would require a separate inverter design and extra energy/loss allowance; it is not interchangeable with this 1,000 W DC rating. No physical construction, certification or successful hardware test is claimed.

## Manufacturer references

- Analog Devices LT8705: https://www.analog.com/en/products/lt8705.html
- LT8705 datasheet, input/output voltage and current regulation: https://www.analog.com/media/en/technical-documentation/data-sheets/8705ff.pdf
- TI LM5050-1 reverse-blocking controller: https://www.ti.com/product/LM5050-1
- REC Alpha Pure-R panel data: https://www.recgroup.com/sites/default/files/2025-01/Web_DS_REC_Alpha_Pure-R_EN.pdf
- Eaton XLR-48 module data: https://www.eaton.com/content/dam/eaton/products/electronic-components/resources/data-sheet/eaton-xlr-48-supercapacitor-module-data-sheet.pdf
- Eaton module mass reference: https://www.eaton.com/content/dam/eaton/products/electronic-components/resources/product-aid/eaton-xlr-supercapacitor-module-product-aid.pdf

Component capabilities support selecting these design approaches. They do not validate this new assembly. The earlier 50 W functional-design PDF remains the baseline reference for unchanged source and storage details.

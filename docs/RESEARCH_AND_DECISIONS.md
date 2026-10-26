# ZeroCell research and concrete construction decision

Version 0.2.0, expanded in place on 25 October 2026. The objective now explicitly
includes ordinary everyday use, not just emergencies. No 3.0 release is created.

The uploaded baseline had conflicting output claims without raw measurements,
an incorrect series-capacitance value and voltage-monitor firmware described as
if it performed wider power-management functions. Those claims remain withdrawn.
The original archive and its SHA-256 record are retained.

The useful design is source-dependent: capture real external energy, convert it
within component limits, buffer it without rechargeable batteries and spend it
on matched loads. For the original 7-20 W ambition, sunlight is a practical source
at the required scale. Internally recycled coil or thermal energy does not fund
a net output. A source-specific small harvester is a different power class.

## The concrete release

ZC-D10 uses the specified ACOPOWER panel, Pololu 12 V regulator, ADI DC1937B
supercapacitor power path and Pololu 5 V regulator. The feedback modification
and input voltage window are specified, with exact terminal routes, parts,
switch/fuse states, mechanical requirements and a staged assembly walkthrough.
The initial power path no longer depends on an unbuilt MCU or an unspecified
power-multiplexer circuit. The stock bank is 2.5 F equivalent at 10 V.

The 6 V factory backup setting leaves limited final-regulator headroom, so the
released reference changes R3 to 715 kohm with R4 unchanged, targeting about
6.5 V. That change is a ZeroCell engineering selection requiring physical
verification. It is not falsely described as a factory-qualified board setting.

The base service target is 5 V / 10 W, subject to actual input, losses and tests.
The 20 W point is a separate qualification target because the 2 A / 12 V input
budget leaves limited headroom for losses and recharge. Stock storage bridges
seconds, not an overnight interval. Scaling is calculated explicitly rather
than implied by adding source labels or more bins.

## New donor findings

Read [DAILY_USE_AND_SCALING.md](build/DAILY_USE_AND_SCALING.md) for the detailed
transfer decisions. ZeroCell-72 supplied source-matched rails and mission
concepts, but no circuit or executable hardware controller. IX-Vahdat supplied
load/energy concepts; its 399 existing tests passed. Its battery percentages
cannot substitute for capacitor energy. CF-X1 supplied metadata/provenance
and repository checks; its 18 tests passed, with no operational power engine
found in that snapshot. Nothing in these three archives demonstrates physical
power production by ZeroCell.

The earlier fusion/support audit remains in results/donor_audit.json: 249 tests
passed across IX-Fusion, IX-MicroFusion, ClosedLoop and the bridge. General
accounting/fault concepts were independently adapted. Restricted reactor source
and license-unresolved inherited source are not redistributed as Apache code.

## What was tested here

The new ngspice files actually ran. They account for input/store power consumed
by their idealized output rails, exercise source removal and empty-bank startup,
and include zero-input and overload controls. Their detailed limits are stated
in [PROOF_OF_CONCEPT.md](build/PROOF_OF_CONCEPT.md). The source-divider circuit
also ran and agrees with the specified resistor calculation. No physical meter
reading or ZeroCell hardware test has been invented.

[PRIMARY_SOURCES.md](build/PRIMARY_SOURCES.md) links the vendor documentation
used to choose actual components. The [complete BOM](../hardware/reference_build/BOM.md),
[system wiring](build/SYSTEM_WIRING.pdf) and [assembly guide](build/ASSEMBLY_GUIDE.md)
make the next physical action concrete. After construction, source-fed steady
load, capacitor trend, interruption, recovery, temperature and fault tests are
needed to establish a rating. No more donor repositories are required for that
specific reference build; the outstanding evidence is measured assembly behaviour.

## Integrated twenty-channel design, still v0.2.0

The current authoritative stack design is `stack1000/DESIGN.md` revision B. It selects solar as abundant external input, replaces the conceptual active sharing stage with modified populated DC1924A boards and passive sharing, and expands the bank to 60 modules/channel. `ix_zerocell.power` is reused as executed independent-channel energy accounting. The original firmware contributes fault-policy principles, not a deployable twenty-channel controller. Other retrieved RF/static and thermoacoustic concept material provided no measured source curve that could be credited with watts. No new fusion power source is asserted.

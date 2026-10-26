# Firmware and advisory control scope

`firmware/main.cpp` and `power_guard.h` retain the small-bank Uno monitor. It compiles for ATmega328P but was not flashed or hardware-tested. It accepts instrument-fed samples, and physical actuation remains disabled. It does not acquire all twenty stack banks or sixty internal modules per channel.

`firmware/stack_supervisor.h` is new host-testable advisory policy for twenty channel samples. It rejects invalid/stale/out-of-range data, latches unhealthy channels, requires healthy reset conditions and computes a conservative load cap from healthy count, minimum channel current, minimum bus voltage and the 50 W common allowance. Its useful-power cap is rounded down in 50 W increments. With twenty qualified channels it allows 1,000 W; with nineteen, 950 W; with ten, 450 W.

The stack header has no GPIO, ADC/CAN drivers, contactor outputs or real load-control interface. It is not deployment firmware for a 1 kW device. Hardwired overvoltage, thermal, current and fault protection remain necessary and must not depend on a host computer. G01/G05 describe the unfinished acquisition/protection integration. Native tests validate the implemented policy, not its physical execution.

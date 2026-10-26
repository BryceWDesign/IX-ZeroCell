// IX-ZeroCell Firmware – config.h
// Author: Bryce Wooster
// License: Apache-2.0
// Purpose: Hardware abstraction and constants for firmware control

#ifndef IX_ZEROCELL_CONFIG_H
#define IX_ZEROCELL_CONFIG_H

// ------------------
// 🔌 Pin Definitions
// ------------------

#define PIN_VCAP        A0  // Analog input from voltage divider
#define PIN_LED_OK      9   // LED: system good
#define PIN_LED_LOW     8   // LED: low power
#define PIN_MPPT_PULSE  2   // Optional: MPPT activity detect

// ------------------
// ⚙️ System Constants
// ------------------

#define ADC_REF_VOLTAGE     5.00  // ADC reference voltage (V)
#define DIVIDER_R1_OHMS     47000 // Upper resistor in divider (Ω)
#define DIVIDER_R2_OHMS     10000 // Lower resistor in divider (Ω)

// Voltage calculation factor (precomputed for speed)
#define VOLTAGE_SCALE ((ADC_REF_VOLTAGE / 1023.0) * \
                      ((DIVIDER_R1_OHMS + DIVIDER_R2_OHMS) / DIVIDER_R2_OHMS))

// ------------------
// 🔋 Voltage Thresholds
// ------------------

#define V_THRESH_LOW     5.5   // Minimum safe supercap voltage (V)
#define V_THRESH_GOOD    7.2   // Healthy operating cap voltage (V)

// ------------------
// ⏲️ Timing Constants
// ------------------

#define LOOP_DELAY_MS    1000  // Delay between loop cycles (ms)

#endif  // IX_ZEROCELL_CONFIG_H

// IX-ZeroCell Firmware – utils.h
// Author: Bryce Wooster
// License: Apache-2.0
// Description: Declarations for utility functions used in main firmware

#ifndef IX_ZEROCELL_UTILS_H
#define IX_ZEROCELL_UTILS_H

#include <Arduino.h>

// --------------------------
// 🔋 Voltage Measurement
// --------------------------
/**
 * Reads and returns supercapacitor voltage
 * based on the analog pin and voltage divider.
 * @return float voltage in volts
 */
float readSupercapVoltage();

// --------------------------
// 💡 LED Blinking Utility
// --------------------------
/**
 * Blinks the given digital pin at 1Hz using millis().
 * Meant for status indicators.
 * @param pin digital pin to blink
 */
void blinkStatusLED(uint8_t pin);

// --------------------------
// 🚥 System LED Status Control
// --------------------------
/**
 * Sets LED output states based on current voltage level:
 * - OK (green) LED if voltage >= good threshold
 * - Low (red) LED if voltage < low threshold
 * - Blinks both alternately if in between
 * @param voltage current supercap voltage
 */
void updateSystemLEDs(float voltage);

#endif  // IX_ZEROCELL_UTILS_H

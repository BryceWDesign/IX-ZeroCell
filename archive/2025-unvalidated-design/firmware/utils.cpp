// IX-ZeroCell Firmware – utils.cpp
// Author: Bryce Wooster
// License: Apache-2.0
// Utility functions for sensor readings, LED control, and system logic

#include <Arduino.h>
#include "config.h"
#include "utils.h"

// -------------------------------------------
// 🔋 Read actual voltage from divider on A0
// -------------------------------------------
float readSupercapVoltage() {
  int adcVal = analogRead(PIN_VCAP);
  float voltage = adcVal * VOLTAGE_SCALE;
  return voltage;
}

// --------------------------------------------------------
// 💡 Blink LED on a given pin at 1Hz using millis()
// --------------------------------------------------------
void blinkStatusLED(uint8_t pin) {
  static unsigned long lastToggleTime = 0;
  static bool ledState = false;
  if (millis() - lastToggleTime >= 500) {
    ledState = !ledState;
    digitalWrite(pin, ledState ? HIGH : LOW);
    lastToggleTime = millis();
  }
}

// --------------------------------------------------------
// 🚥 Update LED indicators based on cap voltage level
// --------------------------------------------------------
void updateSystemLEDs(float voltage) {
  if (voltage < V_THRESH_LOW) {
    digitalWrite(PIN_LED_LOW, HIGH);
    digitalWrite(PIN_LED_OK, LOW);
  } else if (voltage >= V_THRESH_GOOD) {
    digitalWrite(PIN_LED_LOW, LOW);
    digitalWrite(PIN_LED_OK, HIGH);
  } else {
    // Intermediate range — blink both alternately
    blinkStatusLED(PIN_LED_OK);
    digitalWrite(PIN_LED_LOW, !digitalRead(PIN_LED_OK));
  }
}

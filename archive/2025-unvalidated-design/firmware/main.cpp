// IX-ZeroCell Firmware – main.cpp
// Author: Bryce Wooster
// License: Apache-2.0
// Platform: ATmega328P (Arduino-compatible, ultra-low-power variant)

// This firmware monitors voltage levels on supercapacitor bank,
// detects MPPT activity, and blinks status LEDs accordingly.
// Expandable for future telemetry or USB enumeration.

#include <Arduino.h>

// Pin Definitions
const int pin_vCap    = A0;     // Analog voltage from supercap divider
const int pin_ledOK   = 9;      // LED: system good
const int pin_ledLow  = 8;      // LED: low power
const int pin_mpptPulse = 2;    // Digital in: MPPT boost activity signal

// Constants
const float vRef       = 5.00;  // ADC reference voltage
const float vDividerR1 = 47000; // Upper resistor (47k)
const float vDividerR2 = 10000; // Lower resistor (10k)
const float scaleFactor = (vRef / 1023.0) * ((vDividerR1 + vDividerR2) / vDividerR2);

// Voltage Thresholds
const float V_LOW  = 5.5;   // Warning: cap getting low
const float V_GOOD = 7.2;   // Nominal range OK

void setup() {
  pinMode(pin_ledOK, OUTPUT);
  pinMode(pin_ledLow, OUTPUT);
  pinMode(pin_mpptPulse, INPUT);
  digitalWrite(pin_ledOK, LOW);
  digitalWrite(pin_ledLow, LOW);
  Serial.begin(9600);
}

void loop() {
  // Measure voltage
  int adcValue = analogRead(pin_vCap);
  float vCap = adcValue * scaleFactor;

  // Display status
  if (vCap < V_LOW) {
    digitalWrite(pin_ledLow, HIGH);
    digitalWrite(pin_ledOK, LOW);
  } else if (vCap >= V_GOOD) {
    digitalWrite(pin_ledLow, LOW);
    digitalWrite(pin_ledOK, HIGH);
  } else {
    // Midrange — blink both
    digitalWrite(pin_ledOK, millis() % 1000 < 500);
    digitalWrite(pin_ledLow, !digitalRead(pin_ledOK));
  }

  // Print debug info
  Serial.print("Cap Voltage: ");
  Serial.println(vCap);

  delay(1000);
}

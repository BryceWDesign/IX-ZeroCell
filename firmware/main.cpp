// Instrument-fed supervisor for Arduino Uno. Does not implement a charger.
// The calibrated instrument supplies four cell readings, an independent bank
// reading, temperature, requested watts and requested seconds as one CSV line.
// Receiving a line stamps LOCAL arrival time. This cannot establish remote
// acquisition freshness; the external instrumentation must enforce that.
#include <Arduino.h>
#include <stdlib.h>
#include <string.h>
#include "power_guard.h"

#ifndef ZEROCELL_ACTUATION_COMMISSIONED
#define ZEROCELL_ACTUATION_COMMISSIONED 0
#endif

static const uint8_t kEnable = 5, kPermit = 2, kReset = 7;
zerocell::PowerGuard guard;
zerocell::Sample sample;
float requested_w = 0, requested_s = 1;
char line_buffer[120];
uint8_t line_length = 0;
bool line_overflow = false, invalid_line = false, last_frame_valid = false;

bool parse_line() {
    float fields[8];
    char* cursor = line_buffer;
    for (uint8_t i = 0; i < 8; ++i) {
        char* end = nullptr;
        fields[i] = strtod(cursor, &end);
        if (end == cursor || !zerocell::finite_value(fields[i])) return false;
        if (i < 7) { if (*end != ',') return false; cursor = end + 1; }
        else if (*end != '\0') return false;
    }
    for (uint8_t i = 0; i < 4; ++i) sample.cell_v[i] = fields[i];
    sample.bank_v = fields[4]; sample.temperature_c = fields[5];
    requested_w = fields[6]; requested_s = fields[7];
    sample.timestamp_ms = millis(); sample.instrumentation_ok = true;
    return true;
}

void setup() {
    digitalWrite(kEnable, LOW); pinMode(kEnable, OUTPUT);
    pinMode(kPermit, INPUT); // External pulldown: disconnected wire cannot grant permit.
    pinMode(kReset, INPUT_PULLUP);
    Serial.begin(115200);
}

void loop() {
    while (Serial.available()) {
        const char ch = static_cast<char>(Serial.read());
        if (ch == '\r') continue;
        if (ch == '\n') {
            line_buffer[line_length] = '\0';
            last_frame_valid = !line_overflow && parse_line();
            if (!last_frame_valid) invalid_line = true;
            sample.instrumentation_ok = last_frame_valid && !invalid_line;
            line_length = 0; line_overflow = false;
        } else if (line_length < sizeof(line_buffer) - 1) line_buffer[line_length++] = ch;
        else line_overflow = true;
    }
    static uint32_t previous = 0;
    const uint32_t now = millis();
    if (now - previous < 100) return;
    previous = now;
    sample.hardware_permit = digitalRead(kPermit) == HIGH;
    if (digitalRead(kReset) == LOW && last_frame_valid) {
        sample.instrumentation_ok = true;
        invalid_line = false;
        guard.reset(now - 1, sample);
    }
    const auto decision = guard.update(now, sample, requested_w, requested_s);
    digitalWrite(kEnable, ZEROCELL_ACTUATION_COMMISSIONED && decision.enable ? HIGH : LOW);
    Serial.print("permit="); Serial.print(decision.enable);
    Serial.print(",tripped="); Serial.print(decision.tripped);
    Serial.print(",reason="); Serial.println(static_cast<int>(decision.reason));
}

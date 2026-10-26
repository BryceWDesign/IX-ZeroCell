#ifndef ZEROCELL_STACK_SUPERVISOR_H
#define ZEROCELL_STACK_SUPERVISOR_H
#include <stdint.h>
#include <math.h>
namespace zerocell {
// Host-testable advisory logic. No GPIO or contactor actuation is implemented.
struct ChannelSample {
    float bank_v, temperature_c, output_a;
    uint32_t timestamp_ms;
    bool present, instrumentation_ok, hardware_permit;
};
struct StackDecision { uint32_t enabled_mask; unsigned healthy; float maximum_useful_w; bool request_allowed; };
class StackSupervisor {
    uint32_t latched_ = 0;
public:
    StackDecision update(uint32_t now, const ChannelSample (&s)[20], float requested_w) {
        uint32_t mask = 0; unsigned n = 0;
        for (unsigned i=0;i<20;++i) {
            const ChannelSample &c=s[i];
            const bool valid = c.present && c.instrumentation_ok && c.hardware_permit &&
                isfinite(c.bank_v) && isfinite(c.temperature_c) && isfinite(c.output_a) &&
                (now-c.timestamp_ms <= 1500u) && c.bank_v>=22.0f && c.bank_v<=47.3f &&
                c.temperature_c>=10.0f && c.temperature_c<=35.0f && c.output_a>=0 && c.output_a<=1.20f;
            if (!valid) latched_ |= (uint32_t(1)<<i);
            if (valid && !(latched_ & (uint32_t(1)<<i))) {mask|=(uint32_t(1)<<i);++n;}
        }
        // Conservative discrete load service. Full service requires all twenty channels.
        const float available = float(n)*1.14f*46.5f-50.0f;
        float capacity = available>0 ? floorf(available/50.0f)*50.0f : 0.0f;
        if (capacity>1000.0f) capacity=1000.0f;
        StackDecision d={mask,n,capacity,isfinite(requested_w) && requested_w>=0 && requested_w<=capacity};
        return d;
    }
    bool reset_channel(unsigned i, uint32_t now, const ChannelSample &s) {
        if (i>=20 || !s.present || !s.instrumentation_ok || !s.hardware_permit ||
            !isfinite(s.bank_v) || !isfinite(s.temperature_c) || !isfinite(s.output_a) ||
            s.bank_v<32 || s.bank_v>46.8 || s.temperature_c<10 || s.temperature_c>35 ||
            s.output_a<0 || s.output_a>1.20f || now-s.timestamp_ms>1500u) return false;
        latched_ &= ~(uint32_t(1)<<i); return true;
    }
};
}
#endif

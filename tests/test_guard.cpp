#include <assert.h>
#include <limits>
#include <iostream>
#include "power_guard.h"
using namespace zerocell;

Sample good(uint32_t time = 100) {
    Sample s; s.timestamp_ms = time; s.cells = 4; s.bank_v = 8.8f;
    for (auto& v : s.cell_v) v = 2.2f;
    s.temperature_c = 25; s.instrumentation_ok = true; s.hardware_permit = true;
    return s;
}

int main() {
    unsigned cases = 0;
    { PowerGuard g; assert(g.update(100, good(), 5, 3).enable); ++cases; }
    { PowerGuard g; auto s = good(); s.hardware_permit = false;
      assert(g.update(100,s,1,10).tripped); s = good(200);
      assert(!g.update(200,s,1,10).enable);
      assert(g.reset(300,good(300))); assert(g.update(400,good(400),1,10).enable); ++cases; }
    { PowerGuard g; assert(g.update(2000, good(100), 1,10).tripped); ++cases; }
    { PowerGuard g; assert(g.update(100, good(101), 1,10).tripped); ++cases; }
    { PowerGuard g; auto s=good(); s.temperature_c=60;
      assert(g.update(100,s,1,10).tripped); ++cases; }
    { PowerGuard g; auto s=good(); s.cell_v[0]=2.6f;
      assert(g.update(100,s,1,10).reason==Reason::Overvoltage); ++cases; }
    { PowerGuard g; auto s=good(); s.cell_v[0]=1.9f;
      assert(g.update(100,s,1,10).reason==Reason::Imbalance); ++cases; }
    { PowerGuard g; auto s=good(); s.cell_v[1]=std::numeric_limits<float>::quiet_NaN();
      assert(g.update(100,s,1,10).tripped); ++cases; }
    { PowerGuard g; auto s=good(); s.bank_v=7;
      assert(g.update(100,s,1,10).reason==Reason::VoltageMismatch); ++cases; }
    { PowerGuard g; auto s=good(); for(auto& v:s.cell_v)v=1; s.bank_v=4;
      assert(!g.update(100,s,1,10).enable); ++cases; }
    { PowerGuard g; assert(g.update(100,good(),11,1).reason==Reason::OutputLimit); ++cases; }
    { PowerGuard g; assert(g.update(100,good(),5,100000).reason==Reason::EnergyReserve); ++cases; }
    { PowerGuard g; assert(g.update(100,good(),-1,1).tripped); ++cases; }
    { PowerGuard g; g.update(100,good(),1,1);
      assert(g.update(99,good(99),1,1).reason==Reason::Clock); ++cases; }
    { PowerGuard g; g.update(0xfffffff0UL,good(0xfffffff0UL),1,1);
      assert(g.update(32,good(32),1,1).enable); ++cases; }
    { Limits l; l.bank_capacitance_lower_f=-1; PowerGuard g(l);
      assert(g.update(100,good(),1,1).reason==Reason::Configuration); ++cases; }
    { Limits l; l.maximum_bank_current_a=.1f; PowerGuard g(l);
      assert(g.update(100,good(),5,1).reason==Reason::CurrentLimit); ++cases; }
    { Limits l; l.emergency_reserve_j=100000; PowerGuard g(l);
      assert(!g.update(100,good(),1,1).enable);
      assert(g.update(200,good(200),1,1,true).enable); ++cases; }
    { PowerGuard g; auto s=good(); s.instrumentation_ok=false;
      assert(g.update(100,s,1,1).tripped); assert(!g.reset(101,s)); ++cases; }
    { PowerGuard g; auto s=good(); s.cells=0;
      assert(g.update(100,s,1,1).tripped); ++cases; }
    { PowerGuard g; auto s=good(); for(auto& v:s.cell_v)v=2.5f; s.bank_v=10;
      assert(g.update(100,s,5,3).enable); ++cases; }
    { PowerGuard g; auto s=good(); for(auto& v:s.cell_v)v=2.58f; s.bank_v=10.32f;
      assert(g.update(100,s,1,1).reason==Reason::Overvoltage); ++cases; }
    { PowerGuard g; auto s=good(); for(auto& v:s.cell_v)v=2.5f; s.bank_v=10;
      assert(g.update(100,s,5,30).reason==Reason::EnergyReserve); ++cases; }
    std::cout << cases << " firmware fault/energy cases passed\n";
}

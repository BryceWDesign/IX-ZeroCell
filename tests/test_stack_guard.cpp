#include "stack_supervisor.h"
#include <assert.h>
#include <limits>
#include <iostream>
int main(){
 using namespace zerocell;
 ChannelSample s[20];for(unsigned i=0;i<20;++i)s[i]={45.5f,25,1.08f,1000,true,true,true};
 StackSupervisor guard;unsigned checks=0;
 assert(guard.update(1001,s,1000).request_allowed);++checks;
 s[19].hardware_permit=false;auto d=guard.update(1002,s,1000);
 assert(!d.request_allowed && d.healthy==19 && d.maximum_useful_w==950);++checks;
 s[19].hardware_permit=true;assert(guard.update(1003,s,950).healthy==19);++checks;
 assert(guard.reset_channel(19,1004,s[19]));++checks;
 assert(guard.update(1005,s,1000).healthy==20);++checks;
 s[0].bank_v=std::numeric_limits<float>::quiet_NaN();assert(guard.update(1006,s,1000).healthy==19);++checks;
 assert(!guard.reset_channel(0,1007,s[0]));++checks;
 assert(guard.update(3000,s,1).healthy==0);++checks;
 assert(!guard.update(3001,s,-1).request_allowed);++checks;
 assert(!guard.update(3002,s,std::numeric_limits<float>::infinity()).request_allowed);++checks;
 s[0].bank_v=31; s[0].timestamp_ms=3002;assert(!guard.reset_channel(0,3003,s[0]));++checks;
 assert(!guard.reset_channel(20,3003,s[0]));++checks;
 StackSupervisor wrap;for(unsigned i=0;i<20;++i){s[i].bank_v=45;s[i].timestamp_ms=0xfffffff0u;}
 assert(wrap.update(5,s,1000).healthy==20);++checks;
 StackSupervisor half;for(unsigned i=10;i<20;++i)s[i].present=false;
 assert(half.update(6,s,450).request_allowed);++checks;
 assert(!half.update(7,s,500).request_allowed);++checks;
 std::cout<<checks<<" stack advisory cases passed; no actuation or hardware validation\n";
}

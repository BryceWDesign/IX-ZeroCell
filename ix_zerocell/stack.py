"""Twenty-channel sizing and power accounting, not a switching or hardware model."""
from dataclasses import dataclass, asdict
import math
from .power import Bank, Bus, Source
from .validation import positive, number, integer

@dataclass(frozen=True)
class StackDesign:
    channels: int = 20
    modules_per_channel: int = 60
    module_f: float = 166.0
    capacity_fraction: float = .8
    high_v: float = 45.5
    low_v: float = 22.0
    channel_budget_w: float = 60.0
    output_efficiency: float = .85
    local_aux_w: float = 4.0
    module_leakage_a: float = .01
    leakage_bound_v: float = 47.5
    branch_loss_w: float = .8
    branch_r_ohm: float = 2.32
    charge_efficiency: float = .95
    conditioned_source_w: float = 340.0
    pv_w: float = 400.0
    source_efficiency: float = .9
    day_aux_w: float = 10.0
    dark_hours: float = 16.0
    light_hours: float = 8.0
    net_output_w: float = 1000.0
    shared_allowance_w: float = 50.0

    def __post_init__(self):
        integer(self.channels, 'channels'); integer(self.modules_per_channel,'modules_per_channel')
        for k,v in asdict(self).items():
            if k not in ('channels','modules_per_channel'): positive(v,k)
        for k in ('capacity_fraction','output_efficiency','charge_efficiency','source_efficiency'):
            if getattr(self,k)>1: raise ValueError(k+' must not exceed 1')
        if self.high_v<=self.low_v: raise ValueError('invalid voltage window')
        if self.leakage_bound_v<self.high_v: raise ValueError('leakage bound below operating voltage')
        if self.pv_w*self.source_efficiency-self.day_aux_w<self.conditioned_source_w:
            raise ValueError('conditioned source exceeds available input after day auxiliaries')

    @property
    def effective_f(self):return self.modules_per_channel*self.module_f*self.capacity_fraction

    def bounds(self):
        e=.5*self.effective_f*(self.high_v**2-self.low_v**2)/3600
        p=self.channel_budget_w/self.output_efficiency+self.local_aux_w+self.modules_per_channel*self.module_leakage_a*self.leakage_bound_v+self.branch_loss_w
        need=p*self.dark_hours
        daily=p*(self.dark_hours+self.light_hours)
        replenishment=self.conditioned_source_w*self.light_hours*self.charge_efficiency
        return {'origin':'calculation','configuration':asdict(self),'effective_channel_f':self.effective_f,
                'usable_channel_wh':e,'channel_draw_bound_w':p,'night_channel_wh':need,
                'night_margin_wh':e-need,'usable_stack_kwh':e*self.channels/1000,
                'night_stack_kwh':need*self.channels/1000,'daily_stack_kwh':daily*self.channels/1000,
                'replenishment_lower_kwh':replenishment*self.channels/1000,
                'capacity_check':e>=need,'daily_energy_check':replenishment>=daily,
                'storage_stress_budget_headroom_w':self.channels*self.channel_budget_w-self.shared_allowance_w-self.net_output_w,
                'hardware_validated':False}

def solve_combiner(intercepts, resistances, limits, target_w, vmin=46.5, vmax=50.5):
    """DC load-line balance with unilateral current-limited sources.
    Intercepts include a measured/equivalent blocking diode offset; no diode dynamics.
    Returns the high-voltage root only. A rejected target is not silently served.
    """
    if not(len(intercepts)==len(resistances)==len(limits)) or not intercepts:
        raise ValueError('matching nonempty source vectors required')
    number(target_w,'target_w');positive(vmin,'vmin');positive(vmax,'vmax')
    if vmax<=vmin:raise ValueError('invalid bus window')
    for e,r,i in zip(intercepts,resistances,limits):
        number(e,'intercept');positive(r,'resistance');number(i,'limit')
    def currents(v):return [min(i,max(0,(e-v)/r)) for e,r,i in zip(intercepts,resistances,limits)]
    def power(v):return v*sum(currents(v))
    points=[vmax-(vmax-vmin)*k/2000 for k in range(2001)]
    bracket=None
    if target_w==0:return {'supplied':True,'bus_v':min(vmax,max(intercepts)), 'channel_a':[0.]*len(limits),'output_w':0.}
    for a,b in zip(points,points[1:]):
        if power(a)<=target_w<=power(b):bracket=(b,a);break
    if bracket is None:return {'supplied':False,'bus_v':None,'channel_a':[], 'output_w':0.,'max_available_in_window_w':max(map(power,points))}
    lo,hi=bracket
    for _ in range(70):
        m=(lo+hi)/2
        if power(m)>=target_w:lo=m
        else:hi=m
    v=(lo+hi)/2;ii=currents(v)
    return {'supplied':True,'bus_v':v,'channel_a':ii,'output_w':v*sum(ii),
            'max_channel_w':max(ii)*v,'min_channel_w':min(ii)*v}

def simulate(design=StackDesign(), days=3, step_s=60, source_factors=None,
             initial_v=None, capacity_factors=None, continuous_dark=False):
    integer(days,'days');positive(step_s,'step_s')
    n=design.channels
    source_factors=[1.]*n if source_factors is None else source_factors
    capacity_factors=[1.]*n if capacity_factors is None else capacity_factors
    if len(source_factors)!=n or len(capacity_factors)!=n:raise ValueError('one factor per channel required')
    for x in source_factors:number(x,'source_factor',0,1)
    for x in capacity_factors:positive(x,'capacity_factor')
    if step_s>60:raise ValueError('step must be <=60 seconds')
    initial_v=design.high_v if initial_v is None else number(initial_v,'initial_v',0,design.high_v)
    channels=[]
    for f in capacity_factors:
        bank=Bank(series=1,parallel=design.modules_per_channel,cell_f=design.module_f*design.capacity_fraction*f,
                  cell_max_v=design.high_v,cutoff_v=design.low_v,cell_dc_resistance_ohm=design.branch_r_ohm,
                  leakage_bank_a=design.module_leakage_a*design.modules_per_channel,max_charge_a=9,max_discharge_a=4.5)
        channels.append(Bus(bank,initial_v,design.charge_efficiency,design.output_efficiency,design.channel_budget_w))
    period=(design.dark_hours+design.light_hours)*3600
    t=0.;end=period*days;miss=[0.]*n;mi=[initial_v]*n;maxres=0.;logs=[];last_hour=-1
    e_in=e_out=e_loss=0.;start_e=sum(x.energy for x in channels)
    # Run each channel independently: aggregate sunshine cannot charge another bank.
    while t<end-1e-8:
        phase=t%period;boundary=design.dark_hours*3600 if phase<design.dark_hours*3600 else period
        dt=min(step_s,end-t,boundary-phase)
        if dt<1e-7:dt=min(step_s,end-t)
        dark=continuous_dark or phase<design.dark_hours*3600
        for i,bus in enumerate(channels):
            f=0. if dark else source_factors[i]
            # Gross harvested source less the separately metered daytime auxiliary feed.
            net=max(0.,design.pv_w*f-design.day_aux_w/design.source_efficiency) if f else 0.
            src=[Source('channel-'+str(i+1),net,design.source_efficiency,design.conditioned_source_w*f)] if net else []
            r=bus.step(src,design.channel_budget_w,dt,design.local_aux_w)
            miss[i]+=r.unmet_output_j;mi[i]=min(mi[i],bus.voltage);maxres=max(maxres,abs(r.residual_j))
            e_in+=r.input_j;e_out+=r.output_j
            e_loss+=sum((r.source_loss_j,r.source_rejected_j,r.output_loss_j,r.controller_j,r.leakage_j,r.capacitor_resistance_loss_j,r.charge_conversion_loss_j,r.curtailed_j))
        t+=dt
        hour=int((t+1e-6)//3600)
        if hour!=last_hour:
            logs.append({'time_s':round(t,6),'min_bank_v':min(b.voltage for b in channels),'max_bank_v':max(b.voltage for b in channels),'unserved_wh':sum(miss)/3600});last_hour=hour
    delta=sum(x.energy for x in channels)-start_e
    closure=e_in-e_out-e_loss-delta
    return {'origin':'numerical_simulation','hours':end/3600,'step_s':step_s,'source_factors':source_factors,
            'initial_v':initial_v,'min_bank_v':mi,'final_bank_v':[b.voltage for b in channels],
            'unserved_channel_wh':[x/3600 for x in miss],'unserved_total_wh':sum(miss)/3600,
            'served_all_budgeted_load':sum(miss)<.01,'net_source_input_j':e_in,'channel_output_j':e_out,
            'loss_and_curtailment_j':e_loss,'storage_change_j':delta,'closure_j':closure,
            'max_step_residual_j':maxres,'trace':logs,'hardware_validated':False,
            'excludes':'switching, controller stability, bus transients, faults, temperature and measured solar IV behavior'}

def rf_budget(density_w_m2,effective_area_m2,efficiency,aux_w=0):
    number(density_w_m2,'density');number(effective_area_m2,'effective_area');number(efficiency,'efficiency',0,1);number(aux_w,'aux')
    return max(0,density_w_m2*effective_area_m2*efficiency-aux_w)

def static_budget(capacitance_f,high_v,low_v,events_per_s,efficiency,aux_w=0):
    positive(capacitance_f,'capacitance');number(high_v,'high');number(low_v,'low');number(events_per_s,'events');number(efficiency,'efficiency',0,1);number(aux_w,'aux')
    if low_v>high_v:raise ValueError('low voltage above high voltage')
    return max(0,.5*capacitance_f*(high_v**2-low_v**2)*events_per_s*efficiency-aux_w)

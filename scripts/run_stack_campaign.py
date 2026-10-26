"""Reproducible 20-channel sizing and negative controls. No measurements generated."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from ix_zerocell.stack import StackDesign,simulate,solve_combiner

def main():
    d=StackDesign();out=ROOT/'results/stack1000';out.mkdir(parents=True,exist_ok=True)
    cases={
      'qualified_envelope':simulate(d),
      'four_shaded_channels':simulate(d,source_factors=[.2]*4+[1.]*16),
      '48h_darkness':simulate(d,days=2,continuous_dark=True),
      'empty_no_source':simulate(d,days=1,initial_v=0,continuous_dark=True),
      'weak_capacitance':simulate(d,days=1,capacity_factors=[.6]+[1.]*19),
    }
    assert cases['qualified_envelope']['served_all_budgeted_load']
    assert min(cases['qualified_envelope']['final_bank_v'])>45.49
    for k in cases:
        if k!='qualified_envelope':assert not cases[k]['served_all_budgeted_load'],k
        assert abs(cases[k]['closure_j'])<.1
        (out/(k+'.json')).write_text(json.dumps(cases[k],indent=2)+'\n')
    combiners={
      'nominal':solve_combiner([49.5]*20,[1.25]*20,[1.17]*20,1050),
      'qualified_extremes':solve_combiner([49.4]*10+[49.6]*10,[1.27]*10+[1.23]*10,[1.14]*10+[1.20]*10,1050),
      '19_low_current_units_full_load':solve_combiner([49.4]*19,[1.27]*19,[1.14]*19,1050),
      '19_units_derated':solve_combiner([49.4]*19,[1.27]*19,[1.14]*19,1000),
      'zero_sources':solve_combiner([0]*20,[1.25]*20,[0]*20,1050),
    }
    assert combiners['nominal']['supplied'] and combiners['qualified_extremes']['supplied']
    assert not combiners['19_low_current_units_full_load']['supplied']
    assert combiners['19_units_derated']['supplied'] and not combiners['zero_sources']['supplied']
    report={'schema':1,'origin':'calculation_and_simulation','bounds':d.bounds(),'combiner_cases':combiners,
            'scenario_summary':{k:{x:v for x,v in c.items() if x not in ('trace','min_bank_v','final_bank_v','source_factors')} for k,c in cases.items()},
            'hardware_validated':False,'checks_passed':True}
    (out/'campaign.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'bounds':d.bounds(),'combiner_cases':combiners,'cases':{k:v['unserved_total_wh'] for k,v in cases.items()}},indent=2))
if __name__=='__main__':main()

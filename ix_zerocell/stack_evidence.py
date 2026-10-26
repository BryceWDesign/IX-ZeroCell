"""Twenty-bank measurement review. Never authenticates or certifies hardware."""
import csv,json
from pathlib import Path
from .evidence import artifact,digest
from .validation import number,positive,load_json

BANKS=[f'bank_{i:02}_v' for i in range(1,21)]
COLUMNS=['time_s','external_input_w','useful_output_w','external_auxiliary_w','output_v',*BANKS]

def review_stack(bundle):
 p=Path(bundle);m=load_json(p)
 required={'schema','origin','serial_numbers','capacitance_f','capacitance_relative_error','voltage_error_v',
 'power_relative_error','power_error_w','max_gap_s','instrument_ids','artifacts'}
 if not isinstance(m,dict) or set(m)!=required:raise ValueError('stack measurement metadata schema mismatch')
 if m['schema']!='stack-1' or m['origin'] not in ('measured','synthetic'):raise ValueError('invalid schema or origin')
 serials=m['serial_numbers']
 if not isinstance(serials,list) or len(serials)!=20 or any(not isinstance(x,str) or not x.strip() for x in serials) or len(set(serials))!=20:raise ValueError('20 distinct channel assembly serial numbers required')
 cc=m['capacitance_f']
 if not isinstance(cc,list) or len(cc)!=20:raise ValueError('20 measured bank capacitances required')
 for c in cc:positive(c,'capacitance')
 for k in ('capacitance_relative_error','power_relative_error'):number(m[k],k,0,1)
 for k in ('voltage_error_v','power_error_w'):number(m[k],k)
 positive(m['max_gap_s'],'max_gap_s')
 if m['max_gap_s']>1:raise ValueError('rating review requires sample intervals <=1 second')
 ids=m['instrument_ids']
 if not isinstance(ids,list) or not ids or any(not isinstance(x,str) or not x.strip() for x in ids):raise ValueError('instrument identities required')
 if not isinstance(m['artifacts'],dict) or set(m['artifacts'])!={'samples','calibration','protocol'}:raise ValueError('sample/calibration/protocol artifacts required')
 paths={k:artifact(p.parent,v) for k,v in m['artifacts'].items()}
 energy={k:0. for k in ('external_input_w','useful_output_w','external_auxiliary_w')}
 first=previous=last=None;count=0;gap_ok=True;load_ok=True;voltage_ok=True;no_input=True;bank_ok=True
 ep=m['power_relative_error'];ew=m['power_error_w'];ev=m['voltage_error_v']
 with paths['samples'].open(newline='',encoding='utf-8') as f:
  rd=csv.DictReader(f)
  if rd.fieldnames!=COLUMNS:raise ValueError('CSV columns do not match 20-bank schema')
  for raw in rd:
   if None in raw or any(v is None for v in raw.values()):raise ValueError('ragged measurement row')
   row={k:number(float(v),k) for k,v in raw.items()};count+=1
   if first is None:first=row
   if previous is not None:
    dt=row['time_s']-previous['time_s']
    if dt<=0:raise ValueError('timestamps must increase')
    gap_ok &= dt<=m['max_gap_s']
    for k in energy:energy[k]+=.5*(previous[k]+row[k])*dt
   load_ok &= row['useful_output_w']*(1-ep)-ew>=1000
   voltage_ok &= row['output_v']-ev>=46.5 and row['output_v']+ev<=50.5
   no_input &= row['external_input_w']<=ew and row['external_auxiliary_w']<=ew
   bank_ok &= all(row[k]-ev>=22 and row[k]+ev<=47.3 for k in BANKS)
   previous=last=row
 if count<2:raise ValueError('at least two rows required')
 elapsed=last['time_s']-first['time_s']
 delta=sum(.5*c*(last[k]**2-first[k]**2) for c,k in zip(cc,BANKS))
 storage_error=sum(abs(.5*c*(last[k]**2-first[k]**2))*m['capacitance_relative_error']+c*(last[k]+first[k])*ev+c*ev*ev for c,k in zip(cc,BANKS))
 # Auxiliary column is externally injected test/utility energy, not internal parasitic load.
 residual=energy['external_input_w']+energy['external_auxiliary_w']-energy['useful_output_w']-delta
 error=sum(energy.values())*ep+3*ew*elapsed+storage_error
 checks={'declared_measured_origin':m['origin']=='measured','sixteen_hours':elapsed>=57600,
         'resolved_samples':gap_ok,'1000W_at_samples':load_ok,'voltage_at_samples':voltage_ok,
         'no_detectable_external_power':no_input,'storage_limits_at_samples':bank_ok,
         'initial_ready':all(first[k]-ev>=45.5 for k in BANKS),
         'energy_closure':-error<=residual<=2000*elapsed+error}
 return {'schema':'stack-review-1','origin':m['origin'],'samples':count,'elapsed_s':elapsed,
 'storage_change_j':delta,'input_j':energy['external_input_w'],'external_auxiliary_j':energy['external_auxiliary_w'],
 'useful_output_j':energy['useful_output_w'],'unmetered_dissipation_j':residual,'error_bound_j':error,'checks':checks,
 'verdict':'MEASUREMENT_REVIEW_CANDIDATE' if all(checks.values()) else 'NOT_VALIDATED',
 'hardware_validated':False,'independent_review_required':True,'between_sample_behavior_verified':False,
 'hashes_authenticate_measurements':False,'bundle_sha256':digest(p)}

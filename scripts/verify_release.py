"""Execute all available release checks, refusing to relabel software as hardware proof."""
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--ngspice',default='ngspice');p.add_argument('--library-path');p.add_argument('--avr-fetch',action='store_true')
 a=p.parse_args();results={};failed=False
 cmds=[('software',[sys.executable,'scripts/verify.py']),
       ('small_reference_circuit',[sys.executable,'scripts/run_reference_poc.py','--ngspice',a.ngspice]),
       ('stack_output_circuit',[sys.executable,'scripts/run_stack_spice.py','--ngspice',a.ngspice])]
 if a.library_path:
  for _,c in cmds[1:]:c.extend(['--library-path',a.library_path])
 if a.avr_fetch:cmds.append(('avr_monitor_compile',[sys.executable,'scripts/build_avr.py','--fetch']))
 for name,c in cmds:
  r=subprocess.run(c,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  (ROOT/'results'/('release-'+name+'.log')).write_text(r.stdout,encoding='utf-8')
  results[name]={'executed':True,'passed':r.returncode==0,'exit_code':r.returncode}
  print(name,results[name],flush=True);failed|=r.returncode!=0
 if not a.avr_fetch:results['avr_monitor_compile']={'executed':False,'passed':False,'reason':'--avr-fetch not supplied'}
 all_pass=all(x['passed'] for x in results.values())
 report={'version':'0.2.0','checks':results,'all_release_software_checks_passed':all_pass,
         'hardware_validated':False,'construction_released':False,'hosted_ci_status':'not_observed_for_this_unpushed_update',
         'evidence':'computed, simulated and compiled only; no physical unit tested'}
 (ROOT/'results/release_verification.json').write_text(json.dumps(report,indent=2)+'\n')
 return 1 if failed or not all_pass else 0
if __name__=='__main__':raise SystemExit(main())

"""Executed analog combiner screen; generic diode and behavioral converter limits.
Not an LT8705 switching model, storage model, or component qualification.
"""
import argparse,json,os,subprocess,tempfile,sys,math,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def circuit(count,load,limit,intercept):
 s=['* Twenty-channel output combiner, behavioral populated converter output ports',
    '* Every source is explicit test-fixture power. No ambient power inference.',
    '.options reltol=0.0001 abstol=1n',
    '.model DBLOCK D(Is=1u N=1.2 Rs=0.02 BV=100 Ibv=1u)',
    'Cbus bus 0 470u','Rbleed bus 0 100k','VSLOAD bus load 0']
 for i in range(20):
  e=intercept if i<count else 0
  s += [f'BREG{i} n{i} 0 V=max(0,{e}*min(time/0.02,1)-200*max(0,i(VS{i})-{limit}))',
        f'VS{i} n{i} a{i} 0',f'RSHARE{i} a{i} b{i} 1.2',f'D{i} b{i} c{i} DBLOCK',f'RWIRE{i} c{i} bus 0.05']
 # Fold back below 40 V to avoid an infinite current request at zero. Tests only credit >=46.5V.
 s += [f'BLOAD load 0 I=(time>0.1)*{load}*v(bus)/max(v(bus)*v(bus),1600)',
       '.control','set wr_singlescale','set wr_vecnames','tran 0.0002 0.5 0 0.0002',
       'wrdata trace.dat v(bus) i(VS0) i(VS19) i(VSLOAD)',
       '.endc','.end']
 return '\n'.join(s)+'\n'

def main():
 p=argparse.ArgumentParser();p.add_argument('--ngspice',default='ngspice');p.add_argument('--library-path');a=p.parse_args()
 env=dict(os.environ)
 if a.library_path:env['LD_LIBRARY_PATH']=a.library_path
 out=ROOT/'results/stack1000/spice';out.mkdir(parents=True,exist_ok=True)
 cases=[('nominal',20,1050,1.17,50),('nineteen_full_negative',19,1050,1.14,49.9),
        ('nineteen_derated',19,1000,1.14,49.9),('overload_negative',20,1300,1.17,50),('empty_negative',0,1050,1.17,50)]
 summary=[]
 version=subprocess.run([a.ngspice,'-v'],capture_output=True,text=True,check=True,env=env).stdout
 for name,n,power,limit,intercept in cases:
  text=circuit(n,power,limit,intercept)
  (ROOT/'hardware/stack1000'/(name+'.cir')).write_text(text)
  with tempfile.TemporaryDirectory() as d:
   path=Path(d);(path/'case.cir').write_text(text)
   r=subprocess.run([a.ngspice,'-b','case.cir'],cwd=path,capture_output=True,text=True,env=env)
   log=r.stdout+r.stderr;(out/(name+'.log')).write_text(log)
   if r.returncode or re.search(r'timestep too small|aborted|Error',log):raise RuntimeError(name+' solver failure')
   rows=[[float(x) for x in l.split()] for l in (path/'trace.dat').read_text().splitlines()[1:] if l.strip()]
   if not rows or len(rows[-1])!=5 or rows[-1][0]<.499:raise RuntimeError('incomplete trace')
   tail=[x for x in rows if x[0]>.45];vmin=min(x[1] for x in tail);vmax=max(x[1] for x in tail)
   qualified=vmin>=46.5 and vmax<=50.5
   expected=name in ('nominal','nineteen_derated')
   if qualified!=expected:raise RuntimeError(f'{name} outcome differs: {vmin}..{vmax}')
   if name=='empty_negative' and max(abs(x[1]*x[4]) for x in rows)>.01:raise RuntimeError('unpowered bus made energy')
   trace={'origin':'behavioral_ngspice','columns':['time_s','bus_v','channel1_a','channel20_a','load_a'],'samples':rows[::10]}
   (out/(name+'.trace.json')).write_text(json.dumps(trace,separators=(',',':'))+'\n')
   summary.append({'name':name,'source_count':n,'requested_internal_w':power,'tail_min_v':vmin,'tail_max_v':vmax,
      'tail_load_w':sum(x[1]*x[4] for x in tail)/len(tail),'voltage_window_pass':qualified,
      'expected_window_pass':expected,'hardware_measured':False})
 report={'origin':'behavioral_ngspice','solver':version,'cases':summary,'checks_passed':True,'hardware_validated':False,
 'limitations':['generic diode, not ST qualification model','ideal current-limited regulator ports, not LT8705 switching or compensation','no storage in this output-port circuit','no fault interrupt-energy proof']}
 (out/'summary.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()

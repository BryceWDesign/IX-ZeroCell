"""Execute real ngspice runs of an explicitly idealized module-level circuit.

This program does not label any generated datum as a hardware measurement.
The model pays for every dependent output-source joule at an input or store.
It does not implement vendor switching, thermal, EMI or protection timing.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))


def integrate(rows, function):
    return sum((function(a)+function(b))*.5*(b[0]-a[0])
               for a,b in zip(rows,rows[1:]))


def execute(executable, library_path=None):
    template=(ROOT/"hardware/spice/reference_path.cir").read_text()
    output=ROOT/"results/reference_build"
    output.mkdir(parents=True,exist_ok=True)
    cases=[("10W_source_interruption",2.5,10,False),
           ("20W_source_interruption",1.25,10,False),
           ("10W_empty_bank_start",2.5,0,False),
           ("no_source_empty_bank",2.5,0,True),
           ("25W_overload_negative_control",1.0,10,False)]
    summaries=[]
    env=dict(os.environ)
    if library_path: env["LD_LIBRARY_PATH"]=str(library_path)
    version=subprocess.run([executable,"-v"],capture_output=True,text=True,env=env,check=True).stdout
    for name,resistance,initial,zero_source in cases:
        circuit=template.replace("RLOAD=2.5",f"RLOAD={resistance}")
        circuit=circuit.replace("INITIAL=10",f"INITIAL={initial}")
        if zero_source:
            circuit=re.sub(r"^VRAW .*?$","VRAW raw 0 0",circuit,flags=re.M)
        with tempfile.TemporaryDirectory() as directory:
            directory=Path(directory)
            path=directory/"case.cir";path.write_text(circuit)
            result=subprocess.run([executable,"-b",str(path)],cwd=directory,
                                  env=env,capture_output=True,text=True)
            log=result.stdout+result.stderr
            (output/(name+".log")).write_text(log)
            if result.returncode or re.search(r"aborted|timestep too small|error",log,re.I):
                raise RuntimeError(f"ngspice did not complete {name}; inspect its log")
            data=(directory/"trace.dat").read_text().splitlines()
            rows=[[float(x) for x in line.split()] for line in data[1:] if line.strip()]
            if len(rows)<100 or rows[-1][0]<59.99 or any(len(r)!=7 for r in rows):
                raise RuntimeError("truncated or malformed SPICE trace")
            input_j=integrate(rows,lambda r:-r[1]*r[6])
            output_j=integrate(rows,lambda r:r[5]**2/resistance)
            storage_j=.5*2.5*(rows[-1][4]**2-rows[0][4]**2)
            residual=input_j-output_j-storage_j
            if residual < -max(.01,.001*max(input_j,output_j)):
                raise RuntimeError("behavioral circuit created unaccounted energy")
            source_rows=[r for r in rows if 1<=r[0]<=29]
            all_powered=all(r[5]>=4.75 for r in source_rows)
            backup_rows=[r for r in rows if 30.01<=r[0]<=39.99]
            hold=0.0
            for a,b in zip(backup_rows,backup_rows[1:]):
                if min(a[5],b[5])>=4.75: hold+=b[0]-a[0]
            peak_input=max(-r[6] for r in rows)
            if peak_input>2.03:
                raise RuntimeError("model exceeded configured source current budget")
            if zero_source and (abs(output_j)>.001 or abs(input_j)>.001):
                raise RuntimeError("empty source-free circuit delivered power")
            if name=="25W_overload_negative_control" and all_powered:
                raise RuntimeError("overload was falsely reported fully supplied")
            if name.startswith(("10W_","20W_")) and not all_powered:
                raise RuntimeError("nominal input-powered scenario did not regulate")
            summary={"case":name,"data_origin":"ngspice_behavioral_simulation",
                     "load_ohm":resistance,"initial_cap_v":initial,
                     "trace_end_s":rows[-1][0],"solver_rows":len(rows),
                     "input_j":input_j,"output_j":output_j,"storage_change_j":storage_j,
                     "accounted_dissipation_j":residual,"peak_input_a":peak_input,
                     "input_present_load_in_range":all_powered,
                     "interruption_seconds_at_4_75V_or_above":hold,
                     "hardware_measured":False}
            summaries.append(summary)
            # Keep all transition points plus 20 ms samples, without fake interpolation.
            slim=[];next_time=0
            for row in rows:
                if row[0]>=next_time or (slim and abs(row[5]-slim[-1][5])>.02):
                    slim.append(row);next_time=row[0]+.02
            (output/(name+".trace.json")).write_text(json.dumps({
                "origin":"ngspice_behavioral_simulation",
                "columns":["time_s","u2_input_v","u2_output_v","cap_terminal_v",
                           "internal_store_v","load_v","input_source_current_a"],
                "samples":slim},separators=(",",":"))+"\n")
    report={"schema":"1","solver":version.strip(),"hardware_measured":False,
            "scope":"power-conserving behavioral modules, not vendor switching/qualification models",
            "source_boundary":"U2 12 V input, after the separately designed solar buck",
            "checks_passed":True,"cases":summaries}
    with tempfile.TemporaryDirectory() as directory:
        directory=Path(directory)
        result=subprocess.run([executable,"-b",str(ROOT/"hardware/spice/source_uvlo.cir")],
                              cwd=directory,env=env,capture_output=True,text=True)
        log=result.stdout+result.stderr
        (output/"source_uvlo.log").write_text(log)
        if result.returncode or re.search(r"aborted|error",log,re.I):
            raise RuntimeError("UVLO circuit run failed")
        data=(directory/"uvlo.dat").read_text().splitlines()
        rows=[[float(x) for x in line.split()] for line in data[1:] if line.strip()]
        rising=[];falling=[]
        for first,last in zip(rows,rows[1:]):
            if first[3]<.5<=last[3]:rising.append(last[1])
            if first[3]>=.5>last[3]:falling.append(last[1])
        if len(rising)!=1 or len(falling)!=1 or rows[-1][0]<19.99:
            raise RuntimeError("UVLO hysteresis trace is incomplete or unstable")
        from ix_zerocell.reference_build import source_cutoff
        expected=source_cutoff()
        if abs(rising[0]-expected['rising_v_typical'])>.02 or abs(falling[0]-expected['falling_v_typical'])>.02:
            raise RuntimeError("simulated enable divider disagrees with its declared calculation")
        report['source_uvlo']={"origin":"ideal_hysteresis_circuit_simulation",
                               "rising_pv_v":rising[0],"falling_pv_v":falling[0],
                               "real_IC_threshold_tolerances_validated":False}
        (output/"source_uvlo.trace.json").write_text(json.dumps({
            "origin":"ideal_hysteresis_circuit_simulation",
            "columns":["time_s","pv_v","enable_input_v","enable_state"],
            "samples":rows[::20]},separators=(",",":"))+"\n")
    (output/"spice_poc.json").write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps(report,indent=2))
    return report


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--ngspice",default=shutil.which("ngspice"))
    p.add_argument("--library-path",type=Path)
    a=p.parse_args()
    if not a.ngspice: p.error("ngspice executable required; install it or pass --ngspice")
    execute(a.ngspice,a.library_path)

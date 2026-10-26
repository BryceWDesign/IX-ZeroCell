"""Generate human-readable tables from executable scenarios, not hand-entered results."""
import csv
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ix_zerocell.experiments import campaign, run_scenario
from ix_zerocell.power import Bank

root=Path(__file__).resolve().parents[1]
r=campaign()
(root/"results"/"campaign.json").write_text(json.dumps(r,indent=2,allow_nan=False)+"\n")
lines=["# Simulated service and cold-start results", "",
       "These are assumption-based computations, not measured ZeroCell performance.", "",
       "| Scenario | First full-load time (s) | Full-load seconds | Useful output (Wh) |",
       "|---|---:|---:|---:|"]
for s in r["scenarios"]:
    start=s["first_99_percent_load_s"]
    lines.append(f"| {s['name']} | {start if start is not None else 'never'} | {s['seconds_at_99_percent_load']:.1f} | {s['output_wh']:.6f} |")
lines += ["", "Full load means at least 99% of the requested power in a modeled step. The 5-second direct-source startup is an assumption. Full-load seconds include service while the input remains connected; they are not all post-source runtime.", "",
          "The large empty bank/hand-generator case intentionally fails to start. The starter case charges a smaller separate bank. The model does not claim to implement or experimentally test the complete staged switching circuit.", "",
          "## Sensitivity to unmeasured bank properties", "",
          "Charged 10 V field bank, 5 W load, no external input; each case begins at its declared voltage and runs for two hours.", "",
          "| Per-cell capacitance (F) | Bank leakage (mA) | Full-load minutes | Useful Wh |",
          "|---:|---:|---:|---:|"]
rows=[]
for cap in [2400,3000,3600]:
    for leakage in [.001,.005,.01]:
        s=run_scenario("sensitivity",Bank(cell_f=cap,leakage_bank_a=leakage),lambda t:[],
                       5,7200,initial_v=10,start_v=8)
        row={"cell_f":cap,"leakage_bank_a":leakage,
             "full_load_minutes":s["seconds_at_99_percent_load"]/60,"output_wh":s["output_wh"]}
        rows.append(row)
        lines.append(f"| {cap} | {leakage*1000:.1f} | {row['full_load_minutes']:.2f} | {row['output_wh']:.4f} |")
lines += ["", "This is a parameter sweep, not a statistical confidence interval. Actual capacitance, leakage, efficiency and operating temperature still require measurement.", ""]
(root/"results"/"SCENARIO_RESULTS.md").write_text("\n".join(lines))
with (root/"results"/"sensitivity.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n");w.writeheader();w.writerows(rows)
print(f"Reproduced {len(r['scenarios'])} scenarios and {len(rows)} sensitivity cases.")

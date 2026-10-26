"""Optional exact-data figure. Requires matplotlib; no role in core verification."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[1]
report=json.loads((root/"results"/"campaign.json").read_text())
scenarios={s["name"]:s for s in report["scenarios"]}
fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout="constrained")
for name,label,color in [
    ("20W_panel_daylight_1W_light","Wait for large bank", "#dc6b35"),
    ("20W_panel_priority_direct_path_1W_light","Regulated source to priority load", "#187d78")]:
    s=scenarios[name]
    axes[0].step([r["time_s"]/60 for r in s["samples"]],
                 [r["output_w"] for r in s["samples"]],where="post",label=label,color=color,lw=2)
axes[0].set(title="Cold start: 1 W lighting target",xlabel="Minutes from empty bank",ylabel="Useful load power (W)",ylim=(-.05,1.3))
axes[0].legend(loc="upper center",fontsize=9,frameon=False)
for name,label,color in [
    ("charged_field_bank_dark_5W_USB","5 W load, initially charged bank", "#187d78"),
    ("20W_DC_solar_loss_after_one_hour","20 W load, solar removed at 60 min", "#dc6b35")]:
    s=scenarios[name]
    axes[1].step([r["time_s"]/60 for r in s["samples"]],
                 [r["output_w"] for r in s["samples"]],where="post",label=label,color=color,lw=2)
axes[1].set(title="Stored energy sets the service limit",xlabel="Minutes",ylabel="Useful load power (W)",ylim=(-1,25))
axes[1].legend(loc="upper right",fontsize=8,frameon=False)
for ax in axes:
    ax.grid(axis="y",alpha=.2);ax.spines[["top","right"]].set_visible(False)
fig.suptitle("IX-ZeroCell | Simulation screen, not measured hardware",fontsize=14,fontweight="bold")
fig.savefig(root/"results"/"engineering_screen.png",dpi=160)
print("Saved results/engineering_screen.png")

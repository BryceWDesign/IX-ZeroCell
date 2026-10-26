"""Optional plots from executed results; requires matplotlib."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1];base=R/'results/stack1000'
fig,ax=plt.subplots(1,2,figsize=(12,4.8),constrained_layout=True)
for name,label,color in [('qualified_envelope','Qualified source envelope','#087f8c'),('four_shaded_channels','Four channels at 20% source','#bb572a')]:
 d=json.loads((base/(name+'.json')).read_text());t=d['trace']
 ax[0].plot([x['time_s']/3600 for x in t],[x['min_bank_v'] for x in t],label=label,color=color,lw=2)
ax[0].axhline(22,ls='--',color='#555555',label='Sizing endpoint: 22 V')
ax[0].set(xlabel='Elapsed hours',ylabel='Lowest channel bank voltage (V)',title='Independent-bank energy model')
ax[0].legend(fontsize=8,loc='lower left');ax[0].grid(alpha=.2)
for name,label,color in [('nominal','20 channels / 1,050 W internal','#087f8c'),('nineteen_full_negative','19 channels / full demand fails','#bb572a'),('nineteen_derated','19 channels / reduced demand','#5555aa')]:
 d=json.loads((base/'spice'/(name+'.trace.json')).read_text());t=d['samples']
 ax[1].plot([x[0] for x in t],[x[1] for x in t],label=label,color=color,lw=1.5)
ax[1].axhspan(46.5,50.5,color='#087f8c',alpha=.1)
ax[1].set(xlabel='Elapsed seconds',ylabel='Shared bus voltage (V)',title='Behavioral output-port circuit')
ax[1].legend(fontsize=8,loc='lower right');ax[1].grid(alpha=.2)
fig.suptitle('ZC-S1000 computed proof of concept, not measured hardware',fontsize=13,fontweight='bold')
fig.savefig(base/'computed-proof.png',dpi=160)
fig.savefig(base/'computed-proof.svg')

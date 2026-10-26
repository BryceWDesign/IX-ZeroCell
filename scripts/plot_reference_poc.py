"""Plot executed behavioral circuit traces, with no hardware claim.

Optional document dependency: matplotlib. Run run_reference_poc.py first.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/reference_build'


def main():
    fig,axes=plt.subplots(2,1,figsize=(10,6.6),sharex=True)
    for name,label,color in [('10W_source_interruption','10 W','#087f83'),
                             ('20W_source_interruption','20 W','#ba4934')]:
        trace=json.loads((OUT/(name+'.trace.json')).read_text())
        assert trace['origin']=='ngspice_behavioral_simulation'
        data=trace['samples']
        time=[row[0] for row in data]
        axes[0].plot(time,[row[5] for row in data],color=color,label=label,lw=1.8)
        axes[1].plot(time,[row[4] for row in data],color=color,label=label,lw=1.8)
    axes[0].axhline(4.75,color='#798590',ls=':',lw=1,label='4.75 V screen')
    axes[0].set(ylabel='Useful output (V)',ylim=(-.2,5.6))
    axes[1].set(ylabel='Internal capacitor voltage (V)',xlabel='Time (seconds)',
                ylim=(-.2,10.8),xlim=(0,60))
    for ax in axes:
        ax.axvspan(30,40,color='#738697',alpha=.14)
        ax.grid(alpha=.18)
        ax.spines[['top','right']].set_visible(False)
        ax.legend(loc='lower right',frameon=False,ncol=3)
    axes[0].text(35,5.35,'Input absent',ha='center',color='#445767',fontsize=9)
    fig.suptitle('ZeroCell stock-bank behavioral circuit proof',x=.09,ha='left',
                 fontsize=17,fontweight='bold',color='#173548')
    fig.text(.09,.905,'EXECUTED SIMULATION | 2.5 F nominal bank | No physical measurements',
             fontsize=10,color='#596b79')
    fig.text(.09,.025,'Boundary: U2 12 V input. Idealized converters; declared loss/current assumptions.\n'
             'The 10-second interruption exhausts both modeled reserves. These are not rated backup times.',
             fontsize=9,color='#596b79')
    fig.subplots_adjust(left=.09,right=.98,bottom=.14,top=.86,hspace=.18)
    for suffix in ('png','svg'):
        path=OUT/('spice_source_interruption.'+suffix)
        fig.savefig(path,dpi=160,facecolor='white')
        if suffix=='svg':
            path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n')
    plt.close(fig)


if __name__=='__main__':main()

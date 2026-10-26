from pathlib import Path
import argparse,json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ix_zerocell.stack_evidence import review_stack
p=argparse.ArgumentParser(description='Review a supplied 20-bank no-input experiment; never certify hardware')
p.add_argument('bundle',type=Path);a=p.parse_args()
try:r=review_stack(a.bundle)
except (ValueError,OSError,KeyError,TypeError) as e:p.exit(2,str(e)+'\n')
print(json.dumps(r,indent=2,allow_nan=False))
sys.exit(0 if r['verdict']=='MEASUREMENT_REVIEW_CANDIDATE' else 1)

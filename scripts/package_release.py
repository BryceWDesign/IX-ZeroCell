"""Package the complete v0.2.0 source tree, excluding tool downloads/build products."""
from pathlib import Path
import argparse,hashlib,zipfile
from check_manifest import ROOT,included
p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
out=a.out.resolve()
if out.is_relative_to(ROOT):raise SystemExit('Place release ZIP outside the source tree')
files=sorted(x for x in ROOT.rglob('*') if included(x))
if any(x.is_symlink() for x in files):raise SystemExit('Refusing symlink in release')
manifest=ROOT/'SHA256SUMS.txt'
manifest.write_text(''.join(hashlib.sha256(x.read_bytes()).hexdigest()+'  '+x.relative_to(ROOT).as_posix()+'\n' for x in files),encoding='utf-8')
files.append(manifest);out.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for x in sorted(files):
  name='IX-ZeroCell/'+x.relative_to(ROOT).as_posix();info=zipfile.ZipInfo(name,date_time=(2026,10,26,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
  z.writestr(info,x.read_bytes())
print(f'{out}\n{len(files)} files\nsha256 {hashlib.sha256(out.read_bytes()).hexdigest()}')

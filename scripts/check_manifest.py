"""Verify packaged source bytes; hashes do not authenticate hardware evidence."""
from pathlib import Path
import hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
IGNORE={'build','.git','__pycache__','.pytest_cache'}
def included(p):
 return p.is_file() and not any(x in IGNORE for x in p.relative_to(ROOT).parts) and p.name!='SHA256SUMS.txt' and p.suffix not in ('.pyc','.pyo')
def main():
 manifest=ROOT/'SHA256SUMS.txt';seen=set();errors=[]
 for line in manifest.read_text(encoding='utf-8').splitlines():
  try:expected,name=line.split('  ',1)
  except ValueError:errors.append('malformed manifest line');continue
  p=(ROOT/name).resolve()
  if len(expected)!=64 or name in seen or not p.is_relative_to(ROOT) or not p.is_file():errors.append('invalid/missing entry '+name);continue
  seen.add(name)
  if hashlib.sha256(p.read_bytes()).hexdigest()!=expected:errors.append('hash mismatch '+name)
 actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if included(p)}
 errors+=['unlisted file '+x for x in sorted(actual-seen)]
 if not seen:errors.append('empty manifest')
 if errors:print('\n'.join(errors));return 1
 print(f'PASS: {len(seen)} packaged file hashes; not hardware authentication');return 0
if __name__=='__main__':raise SystemExit(main())

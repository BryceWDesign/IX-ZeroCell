# Apply the full v0.2.0 tree and observe actual CI

Nothing has been pushed. The ZIP contains a complete working tree, not a `.git` folder. The previous `update.patch` was based on an older audited tree and has been removed because it no longer describes this release. Do not apply an old patch to this package.

Keep a backup of any local work. In a clean clone of your existing repository, make a new branch. Verify `git status --short` is empty before replacing tracked files. Copy the release into a separate folder first. The following PowerShell sequence requires you to set `$releaseTree` to the actual extracted `IX-ZeroCell` directory; it deliberately stops if the destination has local changes.

```powershell
$releaseTree = (Resolve-Path 'C:\path\to\extracted\IX-ZeroCell').Path
if (-not (Test-Path (Join-Path $releaseTree 'hardware\stack1000\design.json'))) { throw 'Wrong release folder' }
$cloneRoot = (git rev-parse --show-toplevel)
if ($LASTEXITCODE -ne 0) { throw 'Run inside a Git clone' }
if ($releaseTree.StartsWith($cloneRoot, [System.StringComparison]::OrdinalIgnoreCase)) { throw 'Release source must be outside this clone' }
if (git status --porcelain) { throw 'Commit or back up local changes before replacement' }
git pull --ff-only origin main
if ($LASTEXITCODE -ne 0) { throw 'Pull failed' }
git switch -c zerocell-v020-stack-design
if ($LASTEXITCODE -ne 0) { throw 'Branch creation failed' }
# This removes tracked working files on the new branch; .git and history remain.
git rm -r -- .
if ($LASTEXITCODE -ne 0) { throw 'Tracked-file removal failed' }
Get-ChildItem -LiteralPath $releaseTree -Force | Copy-Item -Destination . -Recurse -Force
python scripts/verify.py
if ($LASTEXITCODE -ne 0) { throw 'Verification failed' }
git add -A
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Diff check failed' }
git diff --cached --stat
```

Review the diff, including removals and all archive files, before committing. The source folder must be outside the clone being replaced. The package does not need a 0.3.0 version bump.

```powershell
git commit -m "Integrate twenty-channel 1 kW ZeroCell design and verification"
git push -u origin zerocell-v020-stack-design
```

Open a pull request and observe every job on that exact commit: Python matrix/native controls, AVR monitor compile, legacy circuit cases and stack output-circuit cases. The live badge links to https://github.com/BryceWDesign/IX-ZeroCell/actions/workflows/verify.yml . Hosted green is unknown until those jobs actually run. Green indicates software/build success, not physical 1,000 W output or closed hardware release gates.

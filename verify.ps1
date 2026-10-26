$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
python scripts/verify.py
if ($LASTEXITCODE -ne 0) { throw "Verification failed. See results/verification.json." }

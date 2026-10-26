# Install and reproduce v0.2.0

Extract the ZIP and work inside `IX-ZeroCell`. Python 3.11+ is required. Core tools have no third-party Python runtime dependencies. Native C++ checks need g++ or clang++. Circuit checks need ngspice.

```powershell
python --version
python scripts/check_manifest.py
python -m unittest discover -s tests -v
python scripts/verify.py
python -m ix_zerocell reference
python -m ix_zerocell stack
python scripts/run_reference_poc.py
python scripts/run_stack_spice.py
```

`verify.ps1` wraps the core verification command and propagates failure. On Windows, install a compatible native compiler and make it available on PATH, or run the full native/circuit suite in the included Ubuntu CI jobs. This delivery did not execute Windows or PowerShell; Linux checks are recorded.

On supported Linux x86_64, the retained AVR monitor build fetches checksum-pinned official compiler/core archives:

```sh
python scripts/build_avr.py --fetch
python scripts/verify_release.py --avr-fetch
```

The latter command runs all local software/circuit/build stages. It requires ngspice on PATH; `--ngspice /actual/path` and `--library-path /actual/lib/path` support a local extracted installation. If AVR is omitted, the report explicitly remains an incomplete full release check. No command flashes hardware or controls a power circuit.

`python scripts/run_stack_campaign.py` reproduces the storage/combiner calculations. `python scripts/review_stack_measurements.py path/to/bundle.json` reviews actual supplied measurement data under the documented schema; no sample measured dataset is fabricated.

Optional plot regeneration: install matplotlib in your chosen environment, then run `python scripts/plot_stack.py`. Plots are not required for core verification. See the two separate assembly guides before working on hardware; software installation is not construction release.

The manifest is a delivered-byte check. Run it before verification commands regenerate result logs. Repackaging uses `python scripts/package_release.py --out ../IX-ZeroCell-v0.2.0.zip`; regenerate only after reviewing and verifying the intended tree.

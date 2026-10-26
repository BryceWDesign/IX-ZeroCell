"""Run actual software checks; report hardware status separately."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(command, log):
    env = dict(os.environ)
    env["PYTHONPATH"] = str(ROOT)
    # LeakSanitizer is incompatible with some instrumented execution hosts.
    # The firmware has no heap allocations; ASan/UBSan checks remain enabled.
    env["ASAN_OPTIONS"] = "detect_leaks=0"
    p = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, env=env)
    (ROOT / "results" / log).write_text(p.stdout, encoding="utf-8")
    print(p.stdout, end="")
    if p.returncode:
        raise RuntimeError(f"check failed ({p.returncode}): {' '.join(command)}")
    return p.stdout


def main():
    (ROOT / "results" / "stack1000").mkdir(parents=True,exist_ok=True)
    (ROOT / "build").mkdir(exist_ok=True)
    report = {"software_checks_passed": False, "hardware_validated": False,
              "hosted_ci_status": "query_GitHub_Actions_for_current_commit"}
    try:
        output = run([sys.executable,"-m","unittest","discover","-s","tests","-v"],"python-tests.log")
        match = re.search(r"Ran (\d+) tests", output)
        report["python_tests_passed"] = int(match.group(1)) if match else None
        compiler = shutil.which("g++") or shutil.which("clang++")
        if not compiler:
            raise RuntimeError("g++ or clang++ required for the native firmware check; use CI on Ubuntu or install a C++ compiler")
        executable = "build/guard-tests.exe" if os.name == "nt" else "build/guard-tests"
        flags = ["-std=c++11","-Wall","-Wextra","-Werror","-pedantic"]
        if os.name != "nt": flags += ["-fsanitize=address,undefined"]
        run([compiler,*flags,"-I","firmware","tests/test_guard.cpp","-o",executable],"firmware-compile.log")
        output = run([str(ROOT/executable)],"firmware-tests.log")
        report["firmware_cases_passed"] = int(output.split()[0])
        stack_executable = "build/stack-guard.exe" if os.name == "nt" else "build/stack-guard"
        run([compiler,*flags,"-I","firmware","tests/test_stack_guard.cpp","-o",stack_executable],"stack1000/firmware-compile.log")
        stack_output = run([str(ROOT/stack_executable)],"stack1000/firmware-tests.log")
        report["stack_advisory_cases_passed"] = int(stack_output.split()[0])
        run([sys.executable,"scripts/run_stack_campaign.py"],"stack1000/campaign.log")
        run([sys.executable,"-m","ix_zerocell","campaign","--out","results/campaign.json"],"campaign.log")
        report["software_checks_passed"] = True
    except (RuntimeError, OSError) as exc:
        report["error"] = str(exc)
        print(str(exc),file=sys.stderr)
    (ROOT/"results"/"verification.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
    return 0 if report["software_checks_passed"] else 1


if __name__ == "__main__": raise SystemExit(main())

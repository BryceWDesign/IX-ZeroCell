"""Compile for the ATmega328P directly, without a build service or telemetry.

Linux x86_64 --fetch obtains checksum-pinned official Arduino archives.
Alternatively supply already-installed toolchain and Arduino AVR core paths.
No flashing or hardware access occurs.
"""
import argparse
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
ARCHIVES = {
    "toolchain": (
        "https://downloads.arduino.cc/tools/avr-gcc-7.3.0-atmel3.6.1-arduino7-x86_64-pc-linux-gnu.tar.bz2",
        "bd8c37f6952a2130ac9ee32c53f6a660feb79bee8353c8e289eb60fdcefed91e"),
    "core": ("https://downloads.arduino.cc/cores/staging/avr-1.8.6.tar.bz2",
             "ff1d17274b5a952f172074bd36c3924336baefded0232e10982f8999c2f7c3b6"),
}


def fetch(kind, destination):
    url, expected = ARCHIVES[kind]
    destination.mkdir(parents=True, exist_ok=True)
    archive = destination / (kind + ".tar.bz2")
    if not archive.exists() or hashlib.sha256(archive.read_bytes()).hexdigest() != expected:
        with urllib.request.urlopen(url, timeout=60) as source, archive.open("wb") as target:
            shutil.copyfileobj(source, target)
    if hashlib.sha256(archive.read_bytes()).hexdigest() != expected:
        raise ValueError("official tool archive checksum mismatch")
    unpack = destination/kind
    if not (unpack/".complete").exists():
        with tempfile.TemporaryDirectory(dir=destination) as temporary:
            staging = Path(temporary)/"payload"
            staging.mkdir()
            with tarfile.open(archive) as package:
                # The standard data filter permits legitimate internal toolchain
                # symlinks while rejecting traversal, devices and escaping links.
                package.extractall(staging, filter="data")
            if unpack.exists(): shutil.rmtree(unpack)
            shutil.move(str(staging),str(unpack))
            (unpack/".complete").write_text(expected)
    target = "bin/avr-g++" if kind == "toolchain" else "cores/arduino/Arduino.h"
    return next(p.parents[1 if kind == "toolchain" else 2]
                for p in unpack.rglob(Path(target).name) if str(p).endswith(target))


def build(toolchain, core):
    out = ROOT/"build"/"avr"
    out.mkdir(parents=True, exist_ok=True)
    include = ["-I"+str(core/"cores"/"arduino"), "-I"+str(core/"variants"/"standard"),
               "-I"+str(ROOT/"firmware")]
    flags = ["-mmcu=atmega328p","-DF_CPU=16000000UL","-DARDUINO=10819",
             "-DARDUINO_AVR_UNO","-DARDUINO_ARCH_AVR","-Os","-ffunction-sections",
             "-fdata-sections","-Wall","-Wextra",*include]
    objects = []
    sources = sorted((core/"cores"/"arduino").glob("*.cpp"))
    sources += sorted((core/"cores"/"arduino").glob("*.c"))
    sources += sorted((core/"cores"/"arduino").glob("*.S"))
    sources += [ROOT/"firmware"/"main.cpp"]
    for i, source in enumerate(sources):
        obj = out/f"unit-{i}.o"
        cpp = source.suffix == ".cpp"
        compiler = toolchain/"bin"/("avr-g++" if cpp else "avr-gcc")
        options = ["-std=gnu++11","-fno-exceptions","-fno-threadsafe-statics"] if cpp else []
        subprocess.run([str(compiler),*flags,*options,"-c",str(source),"-o",str(obj)],check=True)
        objects.append(obj)
    elf = out/"zerocell.elf"
    subprocess.run([str(toolchain/"bin"/"avr-g++"),"-mmcu=atmega328p","-Wl,--gc-sections",
                    *(str(p) for p in objects),"-lm","-o",str(elf)],check=True)
    subprocess.run([str(toolchain/"bin"/"avr-objcopy"),"-O","ihex","-R",".eeprom",
                    str(elf),str(out/"zerocell.hex")],check=True)
    size = subprocess.check_output([str(toolchain/"bin"/"avr-size"),"-A",str(elf)],text=True)
    print(size)
    sections = {}
    for line in size.splitlines():
        fields = line.split()
        if len(fields)>=2 and fields[0] in {".text",".data",".bss"}:
            sections[fields[0]]=int(fields[1])
    flash = sections.get(".text",0)+sections.get(".data",0)
    ram = sections.get(".data",0)+sections.get(".bss",0)
    if not flash or flash>32256 or ram>2048:
        raise RuntimeError("ATmega328P image exceeds flash/SRAM budget")
    print(f"AVR compile PASS: {flash}/32256 flash bytes, {ram}/2048 static SRAM bytes")
    print("Monitor mode. No device was flashed; hardware validation remains false.")


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--fetch",action="store_true",help="download official pinned Linux x86_64 tools")
    parser.add_argument("--toolchain",type=Path)
    parser.add_argument("--core",type=Path)
    args=parser.parse_args()
    if args.fetch:
        toolchain=fetch("toolchain",ROOT/"build"/"tools")
        core=fetch("core",ROOT/"build"/"tools")
    elif args.toolchain and args.core:
        toolchain, core=args.toolchain,args.core
    else: parser.error("use --fetch or both --toolchain and --core")
    build(toolchain,core)


if __name__ == "__main__": main()

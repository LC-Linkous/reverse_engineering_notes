"""
Step 3 (plain) of the AVR firmware-extraction demo: disassemble the raw binary.

This runs avr-objdump on the flat firmware.bin, telling it the bytes are a raw
binary blob ("-b binary") for the AVR5 core (ATmega328P and friends).

Compare with annotate.py, which reads the Intel HEX directly. Both are valid:
  - here, "-b binary" is REQUIRED because a .bin has no format header;
  - avr-objdump can auto-detect the Intel HEX format, so annotate.py needs no -b.

------------------------------------------------------------------------------
FINDING avr-objdump (part of the exercise)
------------------------------------------------------------------------------
avr-objdump ships with the Arduino IDE's AVR toolchain. The default below is a
PLACEHOLDER on purpose — locate it on YOUR machine. On Windows it lives at
roughly:
    C:\\Users\\<YOUR_USERNAME>\\Documents\\ArduinoData\\packages\\arduino\\tools\\avr-gcc\\<VERSION>\\bin\\avr-objdump.exe
(<VERSION> looks like "7.3.0-atmel3.6.1-arduino5" — yours may differ.)
On Linux/macOS it may be on your PATH already; pass  --objdump avr-objdump.
------------------------------------------------------------------------------
"""

import argparse
import subprocess
import sys

DEFAULT_OBJDUMP = r"C:\Users\<YOUR_USERNAME>\Documents\ArduinoData\packages\arduino\tools\avr-gcc\<VERSION>\bin\avr-objdump.exe"


def main():
    ap = argparse.ArgumentParser(description="Disassemble a raw AVR binary with avr-objdump.")
    ap.add_argument("-i", "--input", default="firmware.bin", help="Input raw binary. Default: firmware.bin.")
    ap.add_argument("-o", "--output", default="firmware.asm", help="Output listing. Default: firmware.asm.")
    ap.add_argument("-m", "--march", default="avr5", help="AVR architecture (avr-objdump -m). Default: avr5 (ATmega328P).")
    ap.add_argument("--objdump", default=DEFAULT_OBJDUMP, help="Path to avr-objdump (or 'avr-objdump' if on PATH).")
    args = ap.parse_args()

    if "<YOUR_USERNAME>" in args.objdump:
        sys.exit("avr-objdump path is still a placeholder. Find it on your machine and pass --objdump "
                 "(or edit DEFAULT_OBJDUMP at the top of this file).")

    command = [args.objdump, "-D", "-m", args.march, "-b", "binary", args.input]
    print("Running:", " ".join(command), "\n")
    try:
        result = subprocess.run(command, capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit(f"Could not run avr-objdump at: {args.objdump}")

    with open(args.output, "w") as f:
        f.write(result.stdout)
    print(f"Disassembly saved to {args.output}\n")
    print("First 50 lines:")
    print("\n".join(result.stdout.split("\n")[:50]))
    if result.returncode != 0:
        print(f"\nErrors:\n{result.stderr}")


if __name__ == "__main__":
    main()

"""
Step 3 (annotated) of the AVR firmware-extraction demo.

Disassembles the Intel HEX directly (avr-objdump auto-detects the HEX format, so
no "-b binary" is needed here) and adds human-readable comments from
annotations.py.

  python annotate.py               # generic mnemonic comments
  python annotate.py --arduino     # also add Arduino-specific hints + setup()/loop() banners

This folds the two original "comments" scripts into one: the --arduino flag is
the difference between them. The annotation dictionaries live in annotations.py
so you can read and extend them in one place.

See disassemble.py's header for how to locate avr-objdump on your machine.
"""

import argparse
import subprocess
import sys

from annotations import annotate

DEFAULT_OBJDUMP = r"C:\Users\<YOUR_USERNAME>\Documents\ArduinoData\packages\arduino\tools\avr-gcc\<VERSION>\bin\avr-objdump.exe"


def main():
    ap = argparse.ArgumentParser(description="Disassemble AVR Intel HEX and annotate the listing.")
    ap.add_argument("-i", "--input", default="firmware.hex", help="Input Intel HEX. Default: firmware.hex.")
    ap.add_argument("-o", "--output", default="firmware_annotated.asm", help="Output listing. Default: firmware_annotated.asm.")
    ap.add_argument("-m", "--march", default="avr5", help="AVR architecture (avr-objdump -m). Default: avr5.")
    ap.add_argument("--arduino", action="store_true", help="Add Arduino-specific hints and setup()/loop() banners.")
    ap.add_argument("--objdump", default=DEFAULT_OBJDUMP, help="Path to avr-objdump (or 'avr-objdump' if on PATH).")
    args = ap.parse_args()

    if "<YOUR_USERNAME>" in args.objdump:
        sys.exit("avr-objdump path is still a placeholder. Find it on your machine and pass --objdump "
                 "(or edit DEFAULT_OBJDUMP at the top of this file).")

    # Note: no "-b binary" here — objdump auto-detects the Intel HEX format.
    command = [args.objdump, "-D", "-m", args.march, args.input]
    print("Running:", " ".join(command), "\n")
    try:
        result = subprocess.run(command, capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit(f"Could not run avr-objdump at: {args.objdump}")

    annotated = annotate(result.stdout, arduino=args.arduino)
    with open(args.output, "w") as f:
        f.write(annotated)

    print(f"Annotated disassembly saved to {args.output}\n")
    print("Sample output (first 100 lines):")
    print("=" * 80)
    print("\n".join(annotated.split("\n")[:100]))
    if result.returncode != 0:
        print(f"\nErrors:\n{result.stderr}")


if __name__ == "__main__":
    main()

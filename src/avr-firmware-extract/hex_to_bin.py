"""
Step 2 of the AVR firmware-extraction demo: convert Intel HEX to a raw binary.

The extracted firmware.hex is Intel HEX (text: addresses + data records). Some
tools want a flat binary image instead. This converts .hex -> .bin.

You do NOT strictly need this step to disassemble: avr-objdump can read the
Intel HEX directly (see disassemble.py / annotate.py). We keep the conversion as
its own step so you can see the difference between the two formats.
"""

import argparse
from intelhex import IntelHex


def main():
    ap = argparse.ArgumentParser(description="Convert an Intel HEX file to a raw binary.")
    ap.add_argument("-i", "--input", default="firmware.hex", help="Input HEX file. Default: firmware.hex.")
    ap.add_argument("-o", "--output", default="firmware.bin", help="Output BIN file. Default: firmware.bin.")
    args = ap.parse_args()

    ih = IntelHex(args.input)
    ih.tobinfile(args.output)
    print(f"Converted {args.input} -> {args.output}")
    print("Next step:  python disassemble.py   (or)   python annotate.py --arduino")


if __name__ == "__main__":
    main()

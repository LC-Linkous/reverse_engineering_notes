"""
Step 1 of the AVR firmware-extraction demo: read flash off the target.

Uses avrdude to read the target ATmega's flash into an Intel HEX file, talking
through an Arduino running the ArduinoISP sketch (programmer type stk500v1).

------------------------------------------------------------------------------
FINDING YOUR TOOLS (this is part of the exercise)
------------------------------------------------------------------------------
avrdude ships with the Arduino IDE, tucked away inside your Arduino data folder.
The defaults below are LEFT AS PLACEHOLDERS ON PURPOSE: locating avrdude and its
config on YOUR machine is a file-navigation exercise. Go find them.

On Windows, the Arduino IDE typically installs avrdude somewhere like:
    C:\\Users\\<YOUR_USERNAME>\\Documents\\ArduinoData\\packages\\arduino\\tools\\avrdude\\<VERSION>\\bin\\avrdude.exe
    C:\\Users\\<YOUR_USERNAME>\\Documents\\ArduinoData\\packages\\arduino\\tools\\avrdude\\<VERSION>\\etc\\avrdude.conf
(<VERSION> will look like "6.3.0-arduino17" — yours may differ.)

On Linux/macOS, avrdude is often already on your PATH (just "avrdude"), and the
config is usually found automatically, so you can pass --avrdude avrdude and
skip --config.

You can override any of these with command-line flags (see --help).
------------------------------------------------------------------------------

SCOPE: Only read firmware from microcontrollers you own or are authorized to
work on. Note that lock/fuse bits can disable flash readback on some targets; if
you get back an empty or all-0xFF image, the chip may be read-protected.
"""

import argparse
import subprocess
import sys

# Placeholders — update these to the real paths on YOUR computer (see header).
DEFAULT_AVRDUDE = r"C:\Users\<YOUR_USERNAME>\Documents\ArduinoData\packages\arduino\tools\avrdude\<VERSION>\bin\avrdude.exe"
DEFAULT_CONFIG = r"C:\Users\<YOUR_USERNAME>\Documents\ArduinoData\packages\arduino\tools\avrdude\<VERSION>\etc\avrdude.conf"


def main():
    ap = argparse.ArgumentParser(description="Read AVR flash to an Intel HEX file via ArduinoISP.")
    ap.add_argument("-P", "--port", required=True,
                    help="Serial port of the programming Arduino (e.g., COM29, /dev/ttyUSB0, /dev/tty.usbserial-XXXX).")
    ap.add_argument("-p", "--mcu", default="m328p", help="Target part (avrdude -p value). Default: m328p.")
    ap.add_argument("-c", "--programmer", default="stk500v1",
                    help="Programmer type (avrdude -c value). ArduinoISP = stk500v1. Default: stk500v1.")
    ap.add_argument("-b", "--baud", default="19200", help="Programmer baud. ArduinoISP uses 19200. Default: 19200.")
    ap.add_argument("-o", "--output", default="firmware.hex", help="Output HEX file. Default: firmware.hex.")
    ap.add_argument("--avrdude", default=DEFAULT_AVRDUDE, help="Path to the avrdude executable (or just 'avrdude' if on PATH).")
    ap.add_argument("--config", default=DEFAULT_CONFIG, help="Path to avrdude.conf. Omit/set to '' to let avrdude find it.")
    args = ap.parse_args()

    if "<YOUR_USERNAME>" in args.avrdude:
        sys.exit("avrdude path is still a placeholder. Find avrdude on your machine and pass --avrdude "
                 "(or edit DEFAULT_AVRDUDE at the top of this file). See the header for where to look.")

    command = [args.avrdude]
    if args.config:
        command += ["-C", args.config]
    command += ["-c", args.programmer, "-p", args.mcu, "-P", args.port, "-b", args.baud,
                "-U", f"flash:r:{args.output}:i"]

    print("Running:", " ".join(command), "\n")
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print(f"\nFirmware successfully extracted to {args.output}")
            print("Next step:  python hex_to_bin.py")
        else:
            sys.exit(f"\navrdude failed with return code {result.returncode} (see output above).")
    except FileNotFoundError:
        sys.exit(f"Could not run avrdude at: {args.avrdude}\nCheck the path (see the header of this file).")


if __name__ == "__main__":
    main()

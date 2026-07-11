"""
readCOM.py — read and print lines from a single serial port.

The simplest serial monitor: open one port, print whatever the device sends.
Good for watching an Arduino's Serial.println() output, or a boot log.

Usage:
    python readCOM.py --port COM5              # Windows
    python readCOM.py --port /dev/ttyUSB0      # Linux
    python readCOM.py --port /dev/tty.usbserial-XXXX   # macOS

Port names are machine-specific. If you don't know yours, run loopCOM.py to
list and probe the available ports.
"""

import argparse
import serial


def main():
    ap = argparse.ArgumentParser(description="Print lines from a single serial port.")
    ap.add_argument("-p", "--port", required=True, help="Serial port (e.g., COM5, /dev/ttyUSB0).")
    ap.add_argument("-b", "--baud", type=int, default=9600, help="Baud rate. Default: 9600.")
    args = ap.parse_args()

    ser = serial.Serial(args.port, args.baud, timeout=1)
    print(f"Reading {args.port} @ {args.baud} baud. Ctrl-C to stop.\n")
    try:
        while True:
            if ser.in_waiting > 0:
                # errors='replace' so a stray non-UTF-8 byte won't crash the monitor.
                line = ser.readline().decode("utf-8", errors="replace").rstrip()
                print(line)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        ser.close()


if __name__ == "__main__":
    main()

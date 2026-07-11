"""
twoCOM.py — read two serial ports at once.

Useful when a board exposes two serial streams — for example an Arduino using
hardware Serial (over USB) AND a second SoftwareSerial on other pins. Open both,
label each line by its port so you can tell them apart.

Usage:
    python twoCOM.py --port1 COM5 --port2 COM26
    python twoCOM.py --port1 /dev/ttyUSB0 --port2 /dev/ttyUSB1
"""

import argparse
import serial


def main():
    ap = argparse.ArgumentParser(description="Print lines from two serial ports, labeled by port.")
    ap.add_argument("--port1", required=True, help="First serial port.")
    ap.add_argument("--port2", required=True, help="Second serial port.")
    ap.add_argument("-b", "--baud", type=int, default=9600, help="Baud rate for both ports. Default: 9600.")
    args = ap.parse_args()

    ser1 = serial.Serial(args.port1, args.baud, timeout=1)
    ser2 = serial.Serial(args.port2, args.baud, timeout=1)
    print(f"Reading {args.port1} and {args.port2} @ {args.baud} baud. Ctrl-C to stop.\n")
    try:
        while True:
            if ser1.in_waiting > 0:
                line = ser1.readline().decode("utf-8", errors="replace").rstrip()
                print(f"{args.port1}: {line}")
            if ser2.in_waiting > 0:
                line = ser2.readline().decode("utf-8", errors="replace").rstrip()
                print(f"{args.port2}: {line}")
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        ser1.close()
        ser2.close()


if __name__ == "__main__":
    main()

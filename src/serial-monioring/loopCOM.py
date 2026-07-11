"""
loopCOM.py — scan every serial port to find one that's sending data.

When you don't know which port your device is on, this lists all available
ports, briefly opens each, and reports which ones have data waiting. It then
monitors the first active port it found.

Usage:
    python loopCOM.py
    python loopCOM.py --baud 115200
"""

import argparse
import time
import serial
import serial.tools.list_ports


def scan_ports(baud):
    ports = serial.tools.list_ports.comports()
    active_ports = []

    print("Scanning available serial ports...\n")
    for port in ports:
        print(f"Checking {port.device} - {port.description}")
        try:
            ser = serial.Serial(port.device, baud, timeout=2)
            time.sleep(1)
            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting).decode("utf-8", errors="ignore")
                print(f"  [+] Data found: {data[:50]}...")
                active_ports.append(port.device)
            else:
                print("  [-] No data detected")
            ser.close()
        except Exception as e:
            print(f"  [x] Error: {e}")
        print()

    return active_ports


def main():
    ap = argparse.ArgumentParser(description="Find and monitor a serial port that is sending data.")
    ap.add_argument("-b", "--baud", type=int, default=9600, help="Baud rate to probe with. Default: 9600.")
    args = ap.parse_args()

    active = scan_ports(args.baud)
    if not active:
        print("No active ports found with data.")
        return

    print(f"Ports with data: {', '.join(active)}")
    print(f"\nMonitoring {active[0]}...")
    ser = serial.Serial(active[0], args.baud, timeout=1)
    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode("utf-8", errors="ignore").rstrip()
                print(line)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        ser.close()


if __name__ == "__main__":
    main()

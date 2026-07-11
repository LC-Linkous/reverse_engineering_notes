# this loops over potential COM ports to find one that might be sending data


import serial
import serial.tools.list_ports
import time

def scan_ports():
    ports = serial.tools.list_ports.comports()
    active_ports = []
    
    print("Scanning available COM ports...\n")
    
    for port in ports:
        print(f"Checking {port.device} - {port.description}")
        try:
            ser = serial.Serial(port.device, 9600, timeout=2)
            time.sleep(1)
            
            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore')
                print(f"  ✓ Data found: {data[:50]}...")
                active_ports.append(port.device)
            else:
                print(f"  - No data detected")
            
            ser.close()
        except Exception as e:
            print(f"  ✗ Error: {e}")
        
        print()
    
    return active_ports

if __name__ == "__main__":
    active = scan_ports()
    
    if active:
        print(f"\nPorts with data: {', '.join(active)}")
        
        print(f"\nMonitoring {active[0]}...")
        ser = serial.Serial(active[0], 9600, timeout=1)
        
        try:
            while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8', errors='ignore').rstrip()
                    print(line)
        except KeyboardInterrupt:
            print("\nExiting...")
        finally:
            ser.close()
    else:
        print("\nNo active ports found with data.")
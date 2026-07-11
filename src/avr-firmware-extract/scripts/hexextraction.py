import subprocess

# avrdude_path = r"C:\Program Files (x86)\Arduino\hardware\tools\avr\bin\avrdude.exe"
# config_path = r"C:\Program Files (x86)\Arduino\hardware\tools\avr\etc\avrdude.conf"
avrdude_path = r"C:\\Users\\YOUR USER NAME\\Documents\\ArduinoData\\packages\\arduino\\tools\\avrdude\\6.3.0-arduino17\\bin\\avrdude.exe"
config_path =  r"C:\\Users\\YOUR USER NAME\\Documents\\ArduinoData\\packages\\arduino\\tools\\avrdude\\6.3.0-arduino17\\etc\\avrdude.conf"
port = "COM29"
output_file = "firmware.hex"

command = [
    avrdude_path,
    "-C", config_path,
    "-c", "stk500v1",  # Changed from "avrisp"
    "-p", "m328p",
    "-P", port,
    "-b", "19200",     # Change back to 19200
    "-U", f"flash:r:{output_file}:i"
]

try:
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    
    if result.returncode == 0:
        print(f"\nFirmware successfully extracted to {output_file}")
    else:
        print(f"\nError: Command failed with return code {result.returncode}")
        
except Exception as e:
    print(f"Error executing command: {e}")
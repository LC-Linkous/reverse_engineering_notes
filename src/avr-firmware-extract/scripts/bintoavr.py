import subprocess

# Path to avr-objdump (comes with Arduino)
objdump_path = r"C:\\Users\\YOUR USER NAME\\Documents\\ArduinoData\\packages\\arduino\\tools\\avr-gcc\\7.3.0-atmel3.6.1-arduino5\\bin\\avr-objdump.exe"

bin_file = "firmware.bin"
output_file = "firmware.asm"

command = [
    objdump_path,
    "-D",           # Disassemble all
    "-m", "avr5",   # ATmega328P architecture
    "-b", "binary", # Input is raw binary
    bin_file
]

try:
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Save to file
    with open(output_file, 'w') as f:
        f.write(result.stdout)
    
    print(f"Disassembly saved to {output_file}")
    print("\nFirst 50 lines:")
    print('\n'.join(result.stdout.split('\n')[:50]))
    
    if result.returncode != 0:
        print(f"\nErrors:\n{result.stderr}")
        
except Exception as e:
    print(f"Error executing command: {e}")
import subprocess

objdump_path = r"C:\\Users\\YOUR USER NAME\\Documents\\ArduinoData\\packages\\arduino\\tools\\avr-gcc\\7.3.0-atmel3.6.1-arduino5\\bin\\avr-objdump.exe"

def annotate_assembly(asm_content):
    # Basic instruction descriptions
    common_patterns = {
        'out': 'Output to I/O port',
        'in': 'Input from I/O port',
        'ldi': 'Load immediate value',
        'sts': 'Store to data space',
        'lds': 'Load from data space',
        'call': 'Function call',
        'ret': 'Return from function',
        'rjmp': 'Relative jump',
        'jmp': 'Jump',
        'brne': 'Branch if not equal',
        'breq': 'Branch if equal',
        'cpi': 'Compare with immediate',
        'mov': 'Move register to register',
        'push': 'Push onto stack',
        'pop': 'Pop from stack',
        'cli': 'Clear interrupts (disable)',
        'sei': 'Set interrupts (enable)',
    }
    
    # Arduino-specific patterns based on your code
    arduino_patterns = {
        '9600': 'Serial baud rate (9600)',
        '0x2710': 'delay(1000) - 1000ms in hex',
        '0xfa': 'delay(250) - 250ms in hex',
        '0x7d0': 'delay(2000) - 2000ms in hex',
        'Serial.begin': 'Initialize hardware serial (USB)',
        'Serial1.begin': 'Initialize SoftwareSerial (pins 2,3)',
        'Serial.println': 'Print to hardware serial',
        'Serial1.println': 'Print to SoftwareSerial',
    }
    
    annotated = []
    section_markers = {
        'setup': '========== SETUP() FUNCTION ==========',
        'loop': '========== LOOP() FUNCTION ==========',
    }
    
    for line in asm_content.split('\n'):
        # Check for function markers
        for marker, comment in section_markers.items():
            if f'<{marker}>' in line:
                annotated.append(f"\n{'='*80}")
                annotated.append(f"; {comment}")
                annotated.append(f"{'='*80}")
        
        # Add Arduino-specific comments
        comment_added = False
        for pattern, description in arduino_patterns.items():
            if pattern in line:
                line = f"{line:<60} ; Arduino: {description}"
                comment_added = True
                break
        
        # Add basic instruction comments if no Arduino comment
        if not comment_added:
            for pattern, description in common_patterns.items():
                if f'\t{pattern}\t' in line or f'\t{pattern} ' in line:
                    line = f"{line:<60} ; {description}"
                    break
        
        annotated.append(line)
    
    return '\n'.join(annotated)

hex_file = "firmware.hex"
output_file = "firmware_annotated.asm"

command = [
    objdump_path,
    "-D",
    "-m", "avr5",
    hex_file
]

try:
    result = subprocess.run(command, capture_output=True, text=True)
    
    annotated = annotate_assembly(result.stdout)
    
    with open(output_file, 'w') as f:
        f.write(annotated)
    
    print(f"Annotated disassembly saved to {output_file}\n")
    print("Sample output (first 100 lines):")
    print('=' * 80)
    print('\n'.join(annotated.split('\n')[:100]))
    
    if result.returncode != 0:
        print(f"\nErrors:\n{result.stderr}")
        
except Exception as e:
    print(f"Error executing command: {e}")
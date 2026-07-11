import subprocess

objdump_path = r"C:\\Users\\YOUR USER NAME\\Documents\\ArduinoData\\packages\\arduino\\tools\\avr-gcc\\7.3.0-atmel3.6.1-arduino5\\bin\\avr-objdump.exe"

def annotate_assembly(asm_content):
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
    
    annotated = []
    for line in asm_content.split('\n'):
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
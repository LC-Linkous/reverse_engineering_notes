"""
Annotation pattern maps for AVR disassembly.

These dictionaries add human-readable comments to a raw avr-objdump listing.
They are intentionally simple (substring / mnemonic matching) so you can read
and extend them. Add your own entries as you learn more instructions.
"""

# Common AVR instruction mnemonics -> plain-English description.
COMMON_PATTERNS = {
    "out":  "Output to I/O port",
    "in":   "Input from I/O port",
    "ldi":  "Load immediate value",
    "sts":  "Store to data space",
    "lds":  "Load from data space",
    "call": "Function call",
    "ret":  "Return from function",
    "rjmp": "Relative jump",
    "jmp":  "Jump",
    "brne": "Branch if not equal",
    "breq": "Branch if equal",
    "cpi":  "Compare with immediate",
    "mov":  "Move register to register",
    "push": "Push onto stack",
    "pop":  "Pop from stack",
    "cli":  "Clear interrupts (disable)",
    "sei":  "Set interrupts (enable)",
}

# Arduino/sketch-specific hints. These are guesses that help connect the
# disassembly back to familiar Arduino source; they are NOT guarantees.
ARDUINO_PATTERNS = {
    "9600":          "Possible serial baud rate (9600)",
    "0x2710":        "10000 = delay(1000)? (1000 ms)",
    "0xfa":          "250 = delay(250)? (250 ms)",
    "0x7d0":         "2000 = delay(2000)? (2000 ms)",
    "Serial.begin":  "Initialize hardware serial (USB)",
    "Serial1.begin": "Initialize a second/software serial",
    "Serial.println":  "Print to hardware serial",
    "Serial1.println": "Print to software serial",
}

# Symbol markers -> a banner to drop above that function in the listing.
SECTION_MARKERS = {
    "setup": "========== setup() ==========",
    "loop":  "========== loop() ==========",
}


def annotate(asm_content, arduino=False):
    """Return the disassembly with inline comments added.

    arduino=False -> generic mnemonic comments only.
    arduino=True  -> also add Arduino-specific hints and setup()/loop() banners.
    """
    out_lines = []
    for line in asm_content.split("\n"):
        if arduino:
            # Drop a banner above known function symbols.
            for marker, banner in SECTION_MARKERS.items():
                if f"<{marker}>" in line:
                    out_lines.append("")
                    out_lines.append(f"; {banner}")

        commented = False
        if arduino:
            for pattern, desc in ARDUINO_PATTERNS.items():
                if pattern in line:
                    line = f"{line:<60} ; Arduino: {desc}"
                    commented = True
                    break

        if not commented:
            for mnem, desc in COMMON_PATTERNS.items():
                # Match the mnemonic as its own tab/space-delimited field.
                if f"\t{mnem}\t" in line or f"\t{mnem} " in line:
                    line = f"{line:<60} ; {desc}"
                    break

        out_lines.append(line)

    return "\n".join(out_lines)

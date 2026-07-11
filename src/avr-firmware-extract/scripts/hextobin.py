from intelhex import IntelHex

ih = IntelHex("firmware.hex")
ih.tobinfile("firmware.bin")
print("Converted to binary!")
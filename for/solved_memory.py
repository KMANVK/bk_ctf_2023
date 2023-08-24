def bytes_E21080(byte_array, buf, a3, len_buf):
    a5 = ""
    for i in range(a3):
        a5 += chr(ord(buf[i % len_buf]) ^ byte_array[i])
    return a5

#https://gist.github.com/1259iknowthat/8cb818f0a37566b1fc25151ef074d9af
# buf = "RegSetValue"
# byte_E24038 = b'\x11_;\x03\x17\x1b1\x13\r\x18!3\x11\x06\x0f(\x1d5\x13\x03\x06\n4\x11;\x04\x0c\x1a2\x0e\x1b\x069\x01\x11\x06!\x11T\x1b\x04\x02\x009\x02\x17\x084\x17\x15;\x120&\x113\x17\x13\x06\x15(\x03\x0f\x05\x1e\x00++3}\t\x1a=\x00\x00\x00'
# print(bytes_E21080(byte_E24038, buf, 73, len(buf)))

# a1 = b"\x11_;\x04\x0c\x1a2\x0e\x1b\x069\x01\x1c\x14'\x00\x19\n\x02\x03\x1b\r=\x16\x13}\x00\x0c3\x00\x00\x00"
# print(bytes_E21080(a1, buf, 29, len(buf)))

# buf = "CreateProcessA"
# byte_E240AC = b'\x00H96\x1d\x0b4\x1d\x18\x109 \n27\x17\x08RF93\x1f\x0bM\x00\x0b\x16\x00'
# print(bytes_E21080(byte_E240AC, buf, 27, len(buf)))

buf = "RegQueryValueExA"
byte_E24084 = b'\x10.4\x146\x1e\x11\x188>\x15\x1a\x10\x1a\r27:1>\x19\x04\x06\x10:\x08\x18\x0cZ\x1a\x1eqbUP2E\x07\x0f\x00'
print(bytes_E21080(byte_E24084, buf, 39, len(buf)))

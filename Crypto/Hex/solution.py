def decode_hex(hex_string):
    return bytes.fromhex(hex_string).decode('ascii')

hex_encoded_flag = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

decoded_flag = decode_hex(hex_encoded_flag)

print(f"The decoded flag is: {decoded_flag}")

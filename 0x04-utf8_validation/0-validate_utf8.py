#!/usr/bin/python3
""" UTF-8 Validation """

def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    n_bytes = 0
    for num in data:
        byte = num.to_bytes(1, 'big')
        bits = format(byte[0], '#010b')[-8:]
        if n_bytes == 0:
            if bits[0] == '0':
                continue
            while bits[0] == '1':
                n_bytes += 1
                bits = bits[1:]
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (bits[0] == '1' and bits[1] == '0'):
                return False
        n_bytes -= 1
    return n_bytes == 0

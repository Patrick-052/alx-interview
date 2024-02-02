#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data) -> bool:
    """ Returns True if data is a valid UTF-8 encoding, else return False """
    encoded = []
    for i in data:
        if 0 <= i <= 255:
            enc_bin = bin(i)[2:].zfill(8)
            encoded.append(enc_bin)
        else:
            return False

    i = 0
    while i < len(encoded):
        if encoded[i].startswith('0'):
            i += 1
        elif encoded[i].startswith('110'):
            if i + 1 < len(encoded) and encoded[i + 1].startswith('10'):
                i += 2
            else:
                return False
        elif encoded[i].startswith('1110'):
            if i + 2 < len(encoded) and encoded[i + 1].startswith(
                    '10') and encoded[i + 2].startswith('10'):
                i += 3
            else:
                return False
        elif encoded[i].startswith('11110'):
            if i + 3 < len(encoded) and encoded[i + 1].startswith(
                    '10') and encoded[i + 2].startswith('10') and encoded[
                        i + 3].startswith('10'):
                i += 4
            else:
                return False
        else:
            return False
    return True

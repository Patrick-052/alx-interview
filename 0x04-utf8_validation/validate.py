#!/usr/bin/env python3
""" UTF-8 Validation """


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    bytez = 128
    Bytes = 1920
    for i in data:
        if i >= bytez and i <= Bytes:
            return False
    return True


if __name__ == "__main__":
    """ UTF-8 Validation """
    data = [65]
    print(validUTF8(data))
    data = [80, 121, 116, 104, 111, 110, 32, 105, 115,
            32, 99, 111, 111, 108, 33]
    print(validUTF8(data))
    data = [229, 65, 127, 256]
    print(validUTF8(data))

#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    bytez = 128
    Bytes = 1920
    for i in data:
        if i >= bytez and i <= Bytes:
            return False
    return True

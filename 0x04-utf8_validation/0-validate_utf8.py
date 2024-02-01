#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else return False
    :param data:
    :return:
    """
    last_valid_int = 255
    for i in data:
        enc = bin(i)[2:].zfill(8)
        if len(enc) > len(bin(last_valid_int)[2:].zfill(8)):
            return False
    return True

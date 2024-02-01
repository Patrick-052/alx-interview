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
        if i > last_valid_int:
            return False
    return True

#!/usr/bin/python3
""" Module that contains the alternative solution to the problem (Lockboxes) """


def canUnlockall(boxes):
    """ Alternative soln """
    if not boxes:
        return False
    opened_boxes = [0]
    keys = [key for key in boxes[0] if key < len(boxes)]

    while keys:
        key = keys.pop()
        if key not in opened_boxes:
            opened_boxes.append(key)
            keys.extend([k for k in boxes[key] if k < len(boxes)])

    if len(opened_boxes) == len(boxes):
        return True
    return False


# Test cases
boxes = [[1, 3, 5], [0, 2], [4], [1], [2]]
print(canUnlockall(boxes))

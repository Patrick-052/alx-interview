#!/usr/bin/python3
""" Minimum Operations Interview Question """


def minOperations(n):
    """Finds the minimum number of operations needed to
    result in exactly n H characters in the file."""
    if n <= 1 or type(n) is not int:
        return 0

    operations = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    # If n is a prime number greater than 1
    if n > 1:
        operations += n

    return operations

# def minOperations(n):
#     """Finds the minimum number of operations needed to
#     result in exactly n H characters in the file."""
#     if n <= 1 or type(n) is not int:
#         return 0
#     operations = 0
#     for i in range(2, n + 1):
#         while n % i == 0:
#             operations += i
#             n = n / i
#     return operations

#!/usr/bin/python3
# Minimum Operations Interview Question
"""Overall Produre i used:
    1. Check if n is less than or equal to 1, return 0
    2. Check if n is not an integer, return 0
    3. Initialize operations to 0
    4. *While  - Initialize factor to 2
               - check if factor * factor is less than or equal
                 to n
               - check if n is divisible by factor
               - if yes, add factor to operations and divide n by factor
                 else increment factor by 1
               - if n is a prime number greater than 1, add n to
                 operations
               - return operations
        *For - Initialize i to 2
             - check if i is less than or equal to n
             - check if n is divisible by i
             - if yes, add i to operations and divide n by i
             - return operations
    General:
        Smallest factor(i) of a number(n) must be:
            - i <= sqrt(n)
            - i * i <= n
"""


def minOperations(n):
    """Finds the minimum number of operations needed to
    result in exactly n H characters in the file."""
    if n <= 1 or type(n) is not int:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations


def minOperations_1(n):
    """Finds the minimum number of operations needed to
    result in exactly n H characters in the file."""
    if n <= 1 or type(n) is not int:
        return 0
    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n = n / i
    return operations

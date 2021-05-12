"""
Based on the definition a1 = 1, a2 = 1.

O(n)
"""


def fibonacci(count):
    a = 0
    b = 1
    result = []

    for i in range(count):
        result += [b]
        b += a
        a = b - a

    return result

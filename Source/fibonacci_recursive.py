"""
Based on the definition a1 = 1, a2 = 1.

NOTE:
    Only gives n-th number

O(2ⁿ)
"""


def fibonacci(count):
    if count <= 2:
        return 1

    return fibonacci(count - 1) + fibonacci(count - 2)

"""
Based on the definition a₁ = 1, a₂ = 1
(indexed from 1).

NOTE:
    Only gives n-th number

O(2ⁿ)
"""


def fibonacci(count):
    if count <= 2:
        return 1

    return fibonacci(count - 1) + fibonacci(count - 2)

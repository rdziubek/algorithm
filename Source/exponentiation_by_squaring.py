"""
NOTE:
    Last bit is equal 1 when the modulus 2 of the number yields 1.
    When it is such, returned number is multiplied by its base
    besides squaring it.

O(log n)
"""


def exponentiate(base, power):
    result = 1

    while power > 0:
        if power % 2 == 1:
            result *= base

        result *= result
        power //= 2

    return result

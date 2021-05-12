"""

O(√n)
"""


def is_prime(number):
    if number < 2:
        return False
    k = 2
    while k * k <= number:
        if number % k == 0:
            return False
        k += 1
    return True

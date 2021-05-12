"""

O(√n)
"""


def factorise(number):
    result = []

    k = 2
    while number > 1 and k * k <= number:
        while number % k == 0:
            result += [k]
            number //= k
        k += 1
    if number > 1:
        result += [number]

    return result

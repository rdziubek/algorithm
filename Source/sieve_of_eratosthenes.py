"""
NOTE:
    `limit`'s value denote until what prime (starting from 0) elements are sieved through.

O(n log n)
"""


def sieve(limit):
    array = [True] * (limit + 1)

    i = 2
    while i * i <= limit:
        if array[i] is True:
            for j in range(i * i, limit + 1, i):
                array[j] = False
        i += 1

    result = []
    for i in range(2, len(array)):
        if array[i] is True:
            result += [i]

    return result

"""
NOTE:
    `limit`'s value denotes until which prime
    the elements are sieved through.

    Array of size [0..`limit` + 1] is allocated.
    (Elements' values correspond to their indices.)

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

    _result = []
    for i in range(2, len(array)):
        if array[i] is True:
            _result.append(i)

    return _result

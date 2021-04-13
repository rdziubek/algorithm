"""
(a * b) / NWD

O(log n)
"""


def nww(a, b):
    return a / nwd(a, b) * b


def nwd(a, b):
    if b != 0:
        return nwd(b, a % b)

    return a


print(nww(5, 10))

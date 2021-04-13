"""

O(log n)
"""


def nwd(a, b):
    if b != 0:
        return nwd(b, a % b)

    return a


print(nwd(5, 10))

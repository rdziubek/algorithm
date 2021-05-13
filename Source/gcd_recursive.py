"""
Finds largest gcd(a, b) ∈ ℤ such that
gcd(a, b)|a ∧ gcd(a, b)|b.

O(log n)
"""


def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)

    return a

"""

O(log n)
"""

from gcd_recursive import gcd


def lcm(a, b):
    return a / gcd(a, b) * b

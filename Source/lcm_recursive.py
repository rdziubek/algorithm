"""
Finds smallest lcm(a, b) ∈ ℤ such that
a|lcm(a, b) ∧ b|lcm(a, b).

O(log n)
"""

from gcd_recursive import gcd


def lcm(a, b):
    return a / gcd(a, b) * b

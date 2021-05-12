from gcd_iterative import gcd


def lcm(a, b):
    return a / gcd(a, b) * b

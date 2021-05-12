"""

O(log n)
"""


def change_base(number, base):
    stack = []

    while number > 0:
        stack = [number % base] + stack
        number //= base
    return stack

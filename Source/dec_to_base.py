"""
NOTE:
    `_stack` stores converted number's 'digits'
    so that these don't end up reversed.

O(log n)
"""


def change_base(number, base):
    _stack = []

    while number > 0:
        _stack = [number % base] + _stack
        number //= base
    return _stack

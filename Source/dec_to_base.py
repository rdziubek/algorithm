"""
NOTE:
    `_stack` stores converted number's 'digits'
    so that these don't end up reversed.

O(log n)
"""


def change_base(number, base):
    _returned = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 'A', 'B', 'C', 'D', 'E', 'F']
    _stack = []

    while number > 0:
        _temp = _stack
        _stack = [_returned[number % base]]
        _stack.extend(_temp)
        number //= base

    return _stack

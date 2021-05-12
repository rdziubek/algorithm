"""

O(√n)
"""


def factorise(number):
    _result = []

    k = 2
    while number > 1 and k * k <= number:
        while number % k == 0:
            _result.append(k)
            number //= k
        k += 1
    if number > 1:
        _result.append(number)

    return _result

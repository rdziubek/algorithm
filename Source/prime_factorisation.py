"""

O(√n)
"""


def factorise(n):
    result = []

    k = 2
    while n > 1 and k * k <= n:
        while n % k == 0:
            result += [k]
            n //= k
        k += 1
    if n > 1:
        result += [n]

    return result


print(factorise(100))

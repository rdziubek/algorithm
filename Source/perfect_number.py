"""
NOTE:
    Indexing has to start from the second index, so as not to divide number by 1 when adding two divisors.
    While instead of a for loop is used as for loop cant be constructed without using math.sqrt

    When checking up to the inclusive square of the number, it has to be verified that one divisor
    is not being added 2 times at once.

O(√n)
"""


def is_perfect(number):
    total = 1

    if number == 1:
        return False

    i = 2
    while i * i <= number:
        if number % i == 0:
            total += i + number // i
            if number // i != i:
                total += number // i
        i += 1

    return total == number

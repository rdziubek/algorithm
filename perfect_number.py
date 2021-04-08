"""
NOTE:
    Indexing has to start from the second index, so as not to divide number by 1 when adding two divisors.
    While instead of a for loop is used as for loop cant be constructed without using math.sqrt
"""


def is_perfect(number):
    total = 1

    i = 2
    while i * i < number:
        if number % i == 0:
            total += i + number // i
        i += 1

    return total == number


print(is_perfect(6))

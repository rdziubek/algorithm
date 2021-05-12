def is_perfect(number):
    total = 1

    for i in range(2, number):
        if number % i == 0:
            total += i

    return total == number


"""EVALUATION"""
is_perfect(
    number=6
)

def is_perfect(number):
    total = 1

    for i in range(2, number):
        if number % i == 0:
            total += i

    return total == number


print(is_perfect(6))

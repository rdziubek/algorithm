def exponentiate(base, power):
    result = 1

    while power > 0:
        if power % 2 == 1:
            result *= base

        result *= result
        power //= 2

    return result


print(exponentiate(2, 10))

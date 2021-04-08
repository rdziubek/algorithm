def exponentiate(number, power):
    total = 1

    for i in range(power):
        total *= number

    return total


def change_base(number: list, base):
    result = 0

    for i in range(len(number)):
        result += int(number[len(number) - i - 1]) * (exponentiate(base, i))

    return result


print(change_base(list('101'), 2))

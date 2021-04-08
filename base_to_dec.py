def exponentiate(number, power):
    if power == 0:
        return 1

    result = number

    for i in range(power - 1):
        result *= number

    return result


def change_base(number: str, base):
    result = 0

    for i in range(len(number)):
        result += int(number[len(number) - i - 1]) * (exponentiate(base, i))

    return result


print(change_base('101', 2))

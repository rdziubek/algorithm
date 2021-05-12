def change_base(number: str, base):
    result = 0

    for i in range(len(number)):
        result += int(number[len(number) - i - 1]) * (base ** i)

    return result


"""EVALUATION"""
change_base(
    number='101',
    base=2
)

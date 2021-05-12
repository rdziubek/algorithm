def change_base(number, base):
    if number > 0:
        change_base(number // base, base)
        print(number % base)


"""EVALUATION"""
change_base(
    number=10,
    base=2
)

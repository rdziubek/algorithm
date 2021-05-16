def change_base(number, base):
    _returned = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 'A', 'B', 'C', 'D', 'E', 'F']

    if number > 0:
        change_base(number // base, base)
        print(_returned[number % base])


"""EVALUATION"""
change_base(
    number=10,
    base=2
)

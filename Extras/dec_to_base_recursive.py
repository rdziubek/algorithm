def change_base(number, base):
    if number > 0:
        change_base(number // base, base)
        print(number % base)


change_base(10, 2)

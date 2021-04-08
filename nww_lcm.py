# (a * b) / NWD

def nww(a, b):
    return a / nwd(a, b) * b


def nwd(a, b):
    while b != 0:
        previous_b = b
        b = a % b
        a = previous_b
    return a


print(nww(5, 10))

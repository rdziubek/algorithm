def nwd(a, b):
    while b != 0:
        previous_b = b
        b = a % b
        a = previous_b
    return a


print(nwd(5, 10))


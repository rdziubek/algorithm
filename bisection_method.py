def f(x):
    return x + 2.1


def bisect(a, b, error):
    middle = (a + b) / 2

    while f(a) != 0 and f(b) != 0 and b - a >= error:
        middle = (a + b) / 2

        if f(a) * f(middle) > 0:
            a = middle
        else:
            b = middle

    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    return middle


print(bisect(-4, 4, 0.001))

from nwd_gcd_recursive import nwd


def nww(a, b):
    return a / nwd(a, b) * b


print(nww(5, 10))
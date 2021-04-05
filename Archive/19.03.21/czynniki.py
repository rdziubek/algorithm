
    k = 2
    while (n > 1 && k * k <= n):
        while (n % k == 0):
            print(k)
            n = n // k
        k += 1

    if n > 1:
        print(n)

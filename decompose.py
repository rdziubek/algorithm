def decompose(n):
    k = 2
    while n > 1 and k * k <= n:
        while n % k == 0:
            print(k)
            n //= k
        k += 1
    if n > 1:
        print(n)


decompose(100)


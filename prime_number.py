def is_prime(n):
    if n < 2:
        return False
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True


file = open('in/in_czy_pierwsza.txt')
rows = [int(row.strip()) for row in file.readlines() if row.strip()]

for row in rows:
    print(row, is_prime(row))

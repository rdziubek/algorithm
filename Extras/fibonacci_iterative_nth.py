def fibonacci_nth(count):
    a = 0
    b = 1

    for i in range(count):
        if i == count - 1:
            return b

        b += a
        a = b - a


"""EVALUATION"""
fibonacci_nth(
    count=5
)

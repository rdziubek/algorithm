"""
NOTE:
    Only gives n-th number
"""


def fibonacci(count):
    if count <= 2:
        return 1

    return fibonacci(count - 1) + fibonacci(count - 2)


print(fibonacci(5))

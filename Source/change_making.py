"""

O(mn)
"""


def change(amount):
    coins = [1, 2, 5]
    count = 0

    while amount > 0:
        coin = 0

        for i in range(len(coins)):
            if amount >= coins[i] > coin:
                coin = coins[i]

        amount -= coin
        count += 1

    return count

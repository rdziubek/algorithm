def make_change(amount):
    coins = [1, 2, 5]
    coins_used = 0

    while amount > 0:
        spent = 0

        for i in range(len(coins)):
            if amount >= coins[i] >= spent:
                spent = coins[i]

        amount -= spent
        coins_used += 1

    return coins_used


print(make_change(6))

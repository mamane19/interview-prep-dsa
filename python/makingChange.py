# This question is asked by Facebook. Given an array that represents different coin denominations
# and an amount of change you need to make, return the fewest number of coins it takes to make the given amount of change.
# Note: If it is not possible to create the amount of change with the coins you’re given, return -1.

# Ex: Given the following denominations and amount…

# coins = [1,5, 10, 25], amount = 78, return 6
# Take three 25 coins and three 1 coins for a total of 6 coins.


def makingChange(coins, amount):
    # Write your code here
    # return 0
    if amount == 0:
        return 0
    elif amount < 0:
        return -1
    elif amount in coins:
        return 1
    else:
        min_coins = float("inf")
        for i in range(len(coins)):
            num_coins = makingChange(coins, amount - coins[i])
            if num_coins >= 0 and num_coins < min_coins:
                min_coins = num_coins + 1
        return min_coins


print(makingChange([1, 5, 10, 25], 78))

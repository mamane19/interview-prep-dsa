# This question is asked by Google.
# A company is booking flights to send its employees to its two satellite offices A and B.
# The cost of sending the ith employee to office A and office B is given by prices[i][0]
# and prices[i][1] respectively. Given that half the employees must be sent to office A
# and half the employees must be sent to office B, return the minimum cost the company must
# pay for all their employees’ flights.

# Ex: Give the following prices…

# prices = [[40,30],[300,200],[50,50],[30,60]], return 310
# Fly the first personn to office B.
# Fly the second person to office B.
# Fly the third person to office A.
# Fly the fourth person to office A.


def flightPrices(prices):
    # Write your code here
    if not prices:
        return 0
    n = len(prices)
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = prices[0][0]
    dp[0][1] = prices[0][1]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + prices[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + prices[i][1]
    return min(dp[n - 1][0], dp[n - 1][1])


# Test Cases
print(flightPrices([[40, 30], [300, 200], [50, 50], [30, 60]]))

# You’ve broken into an art gallery and want to maximize the value of the paintings you steal.
# All the paintings you steal you place in your bag which can hold at most W pounds. Given that
# the weight and value of the ith painting is given by weights[i] and values[i] respectively,
# return the maximum value you can steal.

# Ex: Given the following W, weights array and values array…
# W = 10, weights = [4, 1, 3], values = [4, 2, 7], return 13.

# Ex: Given the following W, weights array and values array…
# W = 5, weights = [2, 4, 3], values = [3, 7, 2], return 7.

# Ex: Given the following W, weights array and values array…
# W = 7, weights = [1, 3, 4], values = [3, 5, 6], return 11.


def maximize_value(W, weights, values):
    # Write your code here
    if W == 0 or len(weights) == 0:
        return 0
    if W < weights[0]:
        return maximize_value(W, weights[1:], values[1:])
    else:
        return max(values[0] + maximize_value(W - weights[0], weights[1:], values[1:]), maximize_value(W, weights[1:], values[1:]))


# the itterative solution | none optimal
def maximize_value_iter(W, weights, values):
    # Write your code here
    if W == 0 or len(weights) == 0:
        return 0
    dp = [[0 for _ in range(W + 1)] for _ in range(len(weights) + 1)]
    for i in range(len(weights)):
        for j in range(W + 1):
            if j < weights[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1]
                               [j - weights[i]] + values[i])
    return dp[len(weights) - 1][W]


W = 10
weights = [4, 1, 3]
values = [4, 2, 7]
print(maximize_value(W, weights, values))
print(maximize_value_iter(W, weights, values))


W = 5
weights = [2, 4, 3]
values = [3, 7, 2]
print(maximize_value(W, weights, values))
print(maximize_value_iter(W, weights, values))


W = 7
weights = [1, 3, 4]
values = [3, 5, 6]
print(maximize_value(W, weights, values))
print(maximize_value_iter(W, weights, values))

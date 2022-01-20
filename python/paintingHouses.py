# This question is asked by Apple.
# You are tasked with painting a row of houses in your neighborhood such that each house is painted
# either red, blue, or green. The cost of painting the ith house red, blue or green, is given by costs[i][0],
# costs[i][1], and costs[i][2] respectively. Given that you are required to paint each house and no two adjacent
# houses may be the same color, return the minimum cost to paint all the houses.

# Ex: Given the following costs array…
# costs = [[1, 3, 5],[2, 4, 6],[5, 4, 3]], return 8.
# Paint the first house red, paint the second house blue, and paint the third house green.


def min_cost_to_paint_houses(costs):
    if len(costs) == 0:
        return 0
    dp = [[0 for _ in range(3)] for _ in range(len(costs))]
    for i in range(len(costs)):
        if i == 0:
            dp[i][0] = costs[i][0]
            dp[i][1] = costs[i][1]
            dp[i][2] = costs[i][2]
        else:
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
    return min(dp[len(costs) - 1][0], dp[len(costs) - 1][1], dp[len(costs) - 1][2])


# TODO: Later
# recursive solution


costs = [[1, 3, 5], [2, 4, 6], [5, 4, 3]]
print(min_cost_to_paint_houses(costs))


costs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(min_cost_to_paint_houses(costs))

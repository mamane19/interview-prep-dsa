# This question is asked by Apple. 
# Given a staircase where the ith step has a non-negative 
# cost associated with it given by cost[i], return the minimum cost of climbing to the top 
# of the staircase. You may climb one or two steps at a time and you may start climbing from 
# either the first or second step.

# Ex: Given the following cost array…

# cost = [5, 10, 20], return 10.

# Ex: Given the following cost array…

# cost = [1, 5, 10, 3, 7, 2], return 10.


def minCostClimbingStairs(cost):
     # Write your code here
     # return 0
     if len(cost) == 1:
          return cost[0]
     elif len(cost) == 2:
          return min(cost[0], cost[1])
     else:
          return min(cost[0] + minCostClimbingStairs(cost[1:]), cost[1] + minCostClimbingStairs(cost[2:]))


print(minCostClimbingStairs([1, 5, 10, 3, 7, 2]))
print(minCostClimbingStairs([5, 10, 20]))
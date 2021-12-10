# This question is asked by Amazon.
# You’re running a popsicle stand where each popsicle costs $5.
# Each customer you encountered pays with either a $5 bill, a $10 bill, or a $20 bill and only buys
# a single popsicle. the customers that come to your stand come in the ordered given by the customers
# array where customers[i] represents the bill the ith customer pays with. Starting with $0,
# return whether or not you can serve all the given customers while also giving the correct amount of change.

# Ex: Given the following customers…

# customers = [5, 10], return true
# collect $5 from the first customer, pay no change.
# collet $10 from the second customer and give back $5 change.

# Ex: Given the following customers…

# customers = [10], return false
# collect $10 from the first customer and we cannot give back change.

# Ex: Given the following customers…

# customers = [5,5,5,10,20], return true
# collect $5 from the first 3 customers.
# collect $10 from the fourth customer and give back $5 change.
# collect $20 from the fifth customer and give back $10 change ($10 bill and $5 bill).


def canServe(customers):
     total = 0
     for customer in customers:
          total += customer
     # we check if the existing change is enough to give to the next customer
     # if it is not, we return false
     if customers[-1] > total:
          return False
     # we check if the total change is enough to give to the next customer
     # if it is not, we return false
     if customers[-1] < total:
          return True
     return False

# customers = [5, 5, 5, 10, 20]
# print(canServe(customers))
print(canServe([5, 10]))
print(canServe([10]))
print(canServe([5, 5, 5, 10, 20]))


# Time Complexity: O(n)
# Space Complexity: O(1)

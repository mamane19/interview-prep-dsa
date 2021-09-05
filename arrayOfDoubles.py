import numpy as np
# Given an array of doubles, write a method
# that will return indexes into the array with frequency proportional to their
# value. For example, based on the weights (0.4, 1.2, 0.1), index 0 will be
# returned 4x as often as index 2, and index 1 will be returned 3x as often as
# index 0, etc. This method will be used for load balancing requests to backends.
# Assume that the weights are calculated correctly and externally and can be updated.


# O(n) time, O(n) space 
def getIndexes(weights):
    indeces = []
    min_value = min(weights)
    for weight in range(len(weights)):
        current_weight = weights[weight]
        if min_value == 0:
            break
        potential_return_times = round(current_weight / min_value)
        indeces  += [weight] * (potential_return_times)

    return indeces

def getIndex(weights):
    indeces = []
    min_value = min(weights)
    for weight in range(len(weights)):
        current_weight = weights[weight]
        potential_return_times = (current_weight / min_value)
        potential_return_times = np.ceil(potential_return_times)
        if potential_return_times < 1:
            break
        # elif potential_return_times == 1:
        #     indeces += [weight]
        else:
            indeces  += [weight] * int(potential_return_times)
    return indeces

weights = [0.2, 0.6, 0.05]
print(getIndexes(weights))

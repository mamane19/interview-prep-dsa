# There is an infinite array of integers numbered consecutively from 0.
# . At each step, a pointer can move from index i to index i+j , or remain where it is. The value of i begins at 0.
# the value of j begins at 1, at each step  increments by 1. There is one known index that must be avoided. Determine the highest index that can be reached in a given number of steps.


def maxIndex(n, k):
     """
     :param n: number of elements in the array
     :param k: number of steps
     :return: the highest index that can be reached in a given number of steps
     """
     # Initialize the index
     i = 0
     # Initialize the step
     j = 1
     # Initialize the max index
     max_index = 0
     # While the index is less than the number of elements
     while i < n:
          # If the index is equal to the max index
          if i == max_index:
               # Increment the step
               j += 1
          # If the index is less than the max index
          elif i < max_index:
               # Set the step to 1
               j = 1
          # If the index is greater than the max index
          elif i > max_index:
               # Set the step to 1
               j = 1
          # If the step is less than the number of steps
          if j <= k:
               # Increment the index
               i += j
               # Increment the max index
               max_index += 1
          # If the step is greater than the number of steps
          else:
               # Increment the index
               i += 1
     # Return the max index
     return max_index
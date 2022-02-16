# A Burglar breaks into a house with a bag that can carry a maximum of 20 kg.
# He found a safe with 8 gold pellets with the following weights and their corresponding values in US$:
# 5kg - $2500
# 3kg -$1700
# 1kg-$1200
# 6kg-$3000
# 8kg-$4100
# 4kg-$2000
# 11kg-$7000
# 12kg-$7500

# Using the 0-1 Knapsack Algorithm , which combination of pellets would bring about the highest profit,
# provided the weight does not exceed 20kgs. Print the combination of the pellets and the total value
# accrued by that combination.

def knapsack(weights, weightsValues, capacity):
    # Create a matrix to store the values of the knapsack
    matrix = [[0 for x in range(capacity + 1)] for y in range(len(weights))]

    # Fill the first row and column of the matrix
    for i in range(len(weights)):
        matrix[i][0] = 0

    for j in range(capacity + 1):
        matrix[0][j] = 0

    # Fill the rest of the matrix
    for i in range(1, len(weights)):
        for j in range(1, capacity + 1):
            if weights[i] <= j:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1]
                                   [j - weights[i]] + weightsValues[i])
            else:
                matrix[i][j] = matrix[i - 1][j]

    # Backtrack to find the combination of the pellets
    i = len(weights) - 1
    j = capacity
    pellets = []
    while i > 0 and j > 0:
        if matrix[i][j] != matrix[i - 1][j]:
            # Add the weight of the current pellet to the list
            pellets.append(weights[i])
            j -= weights[i]
        i -= 1

    print("Total value: ${}".format(matrix[len(weights) - 1][capacity]))
    print("Pellets Taken: {}".format(pellets))


if __name__ == "__main__":
    weights = [5, 3, 1, 6, 8, 4, 11, 11]
    weightsValues = [2500, 1700, 1200, 3000, 4100, 2000, 7000, 7500]
    capacity = 20
    knapsack(weights, weightsValues, capacity)




# class UndoableList:
     #     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.undo_stack = []
#         self.redo_stack = []
#         self.size = 0

#     def insert(self, v):
#         if self.head is None:
#             self.head = Node(v)
#             self.tail = self.head
#             self.undo_stack.append(v)
#             self.redo_stack = []
#             self.size += 1
#         else:
#             current = self.head
#             while current.next is not None and current.next.value < v:
#                 current = current.next
#             if current.next is None:
#                 current.next = Node(v)
#                 self.tail = current.next
#                 self.undo_stack.append(v)
#                 self.redo_stack = []
#                 self.size += 1
#             else:
#                 current.next = Node(v, current.next)
#                 self.undo_stack.append(v)
#                 self.redo_stack = []
#                 self.size += 1

#     def delete(self, v):
#         if self.head is None:
#             return
#         else:
#             if self.head.value == v:
#                 self.head = self.head.next
#                 self.undo_stack.append(v)
#                 self.redo_stack = []
#                 self.size -= 1
#             else:
#                 current = self.head
#                 while current.next is not None and current.next.value != v:
#                     current = current.next
#                 if current.next is not None:
#                     current.next = current.next.next
#                     self.undo_stack.append(v)
#                     self.redo_stack = []
#                     self.size -= 1

#     def undo(self):
#         if len(self.undo_stack) > 0:
#             self.redo_stack.append(self.head)
#             self.head = self.undo_stack.pop()
#             self.size -= 1
#           #   print(self.head.value)

#     def redo(self):
#         if len(self.redo_stack) > 0:
#             self.undo_stack.append(self.head)
#             self.head = self.redo_stack.pop()
#             self.size += 1
#           #   print(self.head.value)

#     def print_list(self):
#         current = self.head
#         while current is not None:
#             print(current.value, end=' ')
#             current = current.next
#         print()


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

#     def __str__(self):
#         return str(self.value)

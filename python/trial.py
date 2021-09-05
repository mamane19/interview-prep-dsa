

#  You're given an array of integers and an integer. Write a function that moves
#   all instances of that integer in the array to the end of the array and returns
#   the array

#   The function should perform this in place (i.e., it should mutate the input
#   array) and doesn't need to maintain the order of the other integers.
# Sample input:  = [2, 1, 2, 2, 2, 3, 4, 2], 2
# Sample output: [1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently

# O(n) time and O(1) space
def moveElementToEnd(array, toMove):
    for i in range(len(array)):
        if array[i] == toMove:
            array.remove(array[i])
            array.append(toMove)
    return array

array = []
toMove = 3
print(moveElementToEnd(array, toMove))

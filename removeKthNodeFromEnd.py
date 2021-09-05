# write a function that takes in a head of a singly linked list and an integer k, and
# removes the kth node from the end of the list.
# The removal should be in-place, meaning that the original data structure should be 
# mutated.

# Furthermore, the input head of the the linked list should remain the head of the 
# linked list after the removal is done, even if the the node that's supposed to be
# removed is the head.
# You can assume that the input linked list is not empty and contains at least k nodes.

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
def 
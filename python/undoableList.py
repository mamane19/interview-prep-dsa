# An UndoableList is a linear , singly linked list without dummy nodes.
# It contains integers in increasing sorted order and supports the usual find ,
# insert and delete operations, plus two new operations called undo and redo .
# The undo operation allows us to change the list back to a previous version,
# by reversing the last edit operation. We can call undo n times to reverse the
# last n edit operations. If there is no previous edit operation (because the list is new,
# or because all edit operations have been undone), undo does nothing. A redo operation cancels
# the previous undo operation and is used to update the list back to the next more recent version.
# As an example, consider a list L containing 2, 5, and 7, denoted as [2,5,7]. The following shows
# the sequence of operations executed and the list after each operation.
# Insert (6) // [2,5,6,7]
# delete (5) // [2,6,7]
# undo // [2,5,6,7], delete (5) cancelled.
# Undo // [2,5,7], insert (6) cancelled.
# Redo // [2,5,6,7], last undo cancelled, re-apply insert (6).
# insert (4) // [2,4,5,6,7]
# redo // [2,4,5,6,7], nothing to redo
# delete (3) // [2,4,5,6,7], 3 is not in the list, L remains unchanged.
# Undo // [2,4,5,6,7], delete (3) cancelled.
# Undo // [2,5,6,7], insert (4) cancelled.
# Undo // [2,5,7], insert (6) cancelled ( delete (5) has been cancelled by line 3).
# redo // [2,5,6,7], reapply insert (6).
# redo // [2,4,5,6,7] reapply insert (4).

# You are to add all five methods in class UndoableList listed below using the scheme described  above:
# UndoableList( ) : Constructor for an UndoableList object.
# undo(): Revert the list back to the previous version by canceling the last edit operation.
# If no previous version exists , it has no effect on the list.
# redo(): Reapply the operation cancelled by the last undo operation. It has no effect on the most recent
# version of the list.
# insert(int v): Inserts value v into the list, maintaining sorted order.
# delete(int v): Deletes the first occurrence of value v from the list. If v does not exist in the list, do nothing.


class UndoableList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.undo_stack = []
        self.redo_stack = []

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.head)
            self.head = self.undo_stack.pop()
            self.size -= 1

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.head)
            self.head = self.redo_stack.pop()
            self.size += 1

    def insert(self, v):
        self.undo_stack.append(self.head)
        self.head = Node(v)
        if self.tail is None:
            self.tail = self.head
        self.size += 1

    def delete(self, v):
        if self.head.value == v:
            self.undo_stack.append(self.head)
            self.head = self.head.next
            self.size -= 1
            return
        curr = self.head
        while curr.next is not None:
            if curr.next.value == v:
                self.undo_stack.append(curr.next)
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next

    def __str__(self):
        curr = self.head
        s = ""
        while curr is not None:
            s += str(curr.value) + " "
            curr = curr.next
        return s


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    L = UndoableList()
    L.insert(2)
    L.insert(5)
    L.insert(7)
    print(L)
    L.insert(6)
    print(L)
    L.delete(5)
    print(L)
    L.undo()
    print(L)
    L.undo()
    print(L)
    L.redo()
    print(L)
    L.redo()
    print(L)
    L.insert(4)
    print(L)
    L.redo()
    print(L)
    L.delete(3)
    print(L)
    L.undo()
    print(L)
    L.undo()
    print(L)
    L.undo()
    print(L)
    L.redo()
    print(L)
    L.redo()
    print(L)
    L.redo()
    print(L)
class UndoableList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.undo_stack = []
        self.redo_stack = []

    def undo(self):
        if len(self.undo_stack) == 0:
            return
        else:
            self.redo_stack.append(self.undo_stack.pop())
            self.redo_stack[-1][0]()

    def redo(self):
        if len(self.redo_stack) == 0:
            return
        else:
            self.undo_stack.append(self.redo_stack.pop())
            self.undo_stack[-1][0]()

    def insert(self, v):
        self.undo_stack.append([self.remove, v])
        self.redo_stack = []
        if self.head is None:
            self.head = Node(v)
            self.tail = self.head
        else:
            if self.head.value > v:
                self.head = Node(v, self.head)
            else:
                current = self.head
                while current.next is not None and current.next.value < v:
                    current = current.next
                current.next = Node(v, current.next)
                if current.next.next is None:
                    self.tail = current.next
        self.size += 1

    def remove(self, v):
        if self.head is None:
            return
        else:
            if self.head.value == v:
                self.head = self.head.next
                self.size -= 1
            else:
                current = self.head
                while current.next is not None and current.next.value != v:
                    current = current.next
                if current.next is not None:
                    current.next = current.next.next
                    self.size -= 1
                if current.next is None:
                    self.tail = current
                    if self.size == 0:
                        self.head = None
                        self.tail = None

    def __str__(self):
        if self.head is None:
            return "[]"
        else:
            current = self.head
            s = "["
            while current is not None:
                s += str(current.value)
                if current.next is not None:
                    s += ", "
                current = current.next
            s += "]"
            return s


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

        class UndoableList:

        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0
            self.undo_stack = []
            self.redo_stack = []

        def __str__(self):
            if self.head is None:
                return "[ ]"
            else:
                return "[ " + " ".join([str(x) for x in self.head.to_list()]) + " ]"

        def undo(self):
            if len(self.undo_stack) > 0:
                self.redo_stack.append(self.head)
                self.head = self.undo_stack.pop()
                self.size -= 1

        def redo(self):
            if len(self.redo_stack) > 0:
                self.undo_stack.append(self.head)
                self.head = self.redo_stack.pop()
                self.size += 1

        def insert(self, v):
            if self.head is None:
                self.head = Node(v)
                self.tail = self.head
            else:
                if v <= self.head.value:
                    self.head = Node(v, self.head)
                else:
                    self.tail.next = Node(v)
                    self.tail = self.tail.next
            self.undo_stack.append(self.head)
            self.size += 1

        def delete(self, v):
            if self.head is None:
                return
            elif self.head.value == v:
                self.head = self.head.next
                self.undo_stack.append(self.head)
                self.size -= 1
            else:
                prev = self.head
                curr = self.head.next
                while curr is not None:
                    if curr.value == v:
                        prev.next = curr.next
                        self.undo_stack.append(curr)
                        self.size -= 1
                        return
                    prev = curr
                    curr = curr.next

        def to_list(self):
            if self.head is None:
                return []
            else:
                return self.head.to_list()

        # def to_list_reversed(self):
        #      if self.head is None:
        #           return []
        #      else:
        #           return self.tail.to_list_reversed()

        # def to_list_reversed_with_head(self):
        #      if self.head is None:
        #           return []
        #      else:
        #           return self.head.to_list_reversed_with_head()

        # def to_list_reversed_with_head_and_tail(self ):
        #      if self.head is None:
        #           return []
        #      else:
        #           return self.tail.to_list_reversed_with_head_and_tail()

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def to_list(self):
            if self.next is None:
                return [self.value]
            else:
                return [self.value] + self.next.to_list()

        # def to_list_reversed(self):
        #      if self.next is None:
        #           return [self.value]
        #      else:
        #           return self.next.to_list_reversed() + [self.value]

        # def to_list_reversed_with_head(self):
        #      if self.next is None:
        #           return [self.value]
        #      else:
        #           return self.next.to_list_reversed_with_head() + [self.value]

        # def to_list_reversed_with_head_and_tail(self):
        #      if self.next is None:
        #           return [self.value]
        #      else:
        #           return self.next.to_list_reversed_with_head_and_tail() + [self.value]

    # Test cases

    # Test 1


class UndoableList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.undo_stack = []
        self.redo_stack = []

    def __str__(self):
        if self.head is None:
            return "[ ]"
        else:
            return "[ " + " ".join([str(x) for x in self.head.to_list()]) + " ]"

    def insert(self, v):
        if self.head is None:
            self.head = Node(v)
            self.tail = self.head
        else:
            if v < self.head.value:
                self.head = Node(v, self.head)
            else:
                current = self.head
                while current.next is not None and current.next.value < v:
                    current = current.next
                current.next = Node(v, current.next)
                if current.next.next is None:
                    self.tail = current.next
        self.undo_stack.append(v)
        self.redo_stack = []
        self.size += 1

    def delete(self, v):
        if self.head is None:
            return
        else:
            if self.head.value == v:
                self.head = self.head.next
                self.undo_stack.append(v)
                self.redo_stack = []
                self.size -= 1
            else:
                current = self.head
                while current.next is not None and current.next.value != v:
                    current = current.next
                if current.next is not None:
                    current.next = current.next.next
                    self.undo_stack.append(v)
                    self.redo_stack = []
                    self.size -= 1

    def undo(self):
        if len(self.undo_stack) > 0:
            self.redo_stack.append(self.head)
            self.head = self.undo_stack.pop()
            self.size -= 1

    def redo(self):
        if len(self.redo_stack) > 0:
            self.undo_stack.append(self.head)
            self.head = self.redo_stack.pop()
            self.size += 1

    def to_list(self):
        if self.head is None:
            return []
        else:
            return self.head.to_list()


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def to_list(self):
        if self.next is None:
            return [self.value]
        else:
            return [self.value] + self.next.to_list()


if __name__ == "__main__":
    L = UndoableList()
    L.insert(2)
    L.insert(5)
    L.insert(7)
    print(L)
    L.delete(2)
    print(L)
    L.undo()
    print(L)

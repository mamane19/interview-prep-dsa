class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # The head is the first node in a linked list.
        head = Node("X")
        second_node = Node("Y")
        head.next = second_node
        third_node = Node("Z")
        second_node.next = third_node
        fourth_node = Node("K")
        third_node.next = fourth_node
        node = head
        while node.next != None:
            print(node.data)
            node = node.next



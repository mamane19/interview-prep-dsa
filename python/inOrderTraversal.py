# Given a binary tree, return a list containing its inorder traversal without using recursion.

# Ex: Given the following tree…
#       2
#      / \
#     1   3
# return [1, 2, 3]

# Ex: Given the following tree…
#         2
#        / \
#       1   7
#      / \
#     4   8
# return [4, 1, 8, 2, 7]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root is None:
        return []
    stack = []
    result = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            if not stack:
                break
            current = stack.pop()
            result.append(current.value)
            current = current.right
    return result


# recursive solution | easy to understand
def inorder_traversal_recursive(root):
    result = []
    if root is None:
        return result
    result = inorder_traversal_recursive(root.left)
    result.append(root.value)
    result += inorder_traversal_recursive(root.right)
    return result


root = Node(2)
root.left = Node(1)
root.right = Node(3)
print(inorder_traversal(root))
print(inorder_traversal_recursive(root))


root = Node(2)
root.left = Node(1)
root.right = Node(7)
root.left.left = Node(4)
root.left.right = Node(8)
print(inorder_traversal(root))
print(inorder_traversal_recursive(root))

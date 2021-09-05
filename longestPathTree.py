# Write a function that computes the length of the longest path of consecutive integers
# in a tree.
# A node in the tree has a value and a set of children nodes. A tree has no cycles and
# each node has exactly one parent. A path where each node has a value 1 greater than
# its parent is a path of consecutive integers (e.g. 1,2,3 not 1,3,5).
# A few things to clarify:
# ● Integers are all positive
# ● Integers appear only once in the tree

class Tree:
    def __init__(self, value, *children):
        self.value = value
        self.children = []
    def longest_path(tree):
        def rec(current, parent_value=0, parent_path_length=0):
            # Length of the longest chain this node is a part of.
            current_path_length = (parent_path_length + 1
            if current.value == parent_value + 1 else 1)
            yield current_path_length
            for child in current.children:
                for value in rec(child, current.value, current_path_length):
                    yield value
        return max(*rec(tree))
if __name__ == '__main__':
    tree = Tree(1)
    tree.children.append(Tree(2))
    tree.children.append(Tree(3))
    tree.children[0].children.append(Tree(4))
    tree.children[0].children.append(Tree(5))
    print(tree.longest_path())
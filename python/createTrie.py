# This question is asked by Microsoft.
# Implement a trie class that supports insertion and search functionalities.
# Note: You may assume only lowercase alphabetical characters will added to your trie.

# Ex: Given the following operations on your trie…

# Trie trie = new Trie()
# trie.insert("programming");
# trie.search("computer") // returns false.
# trie.search("programming") // returns true.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


trie = Trie()
trie.insert("programming")  # will insert "programming"
print(trie.search("programming"))  # True
print(trie.search("computer"))  # False
print(trie.starts_with("program"))  # True

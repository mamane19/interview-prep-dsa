from createTrie import *

# let's use the trie we created in createTrie.py
trie = Trie()

# insert some words
trie.insert("programming")
trie.insert("computer")
trie.insert("computers")
trie.insert("Shinigami")
trie.insert("Progate")


# search for some words
print(trie.search("programming"))  # True
print(trie.search("computer"))  # True
print(trie.search("computers"))  # True
print(trie.search("Shinigami"))  # True
print(trie.search("Progate"))  # True
print(trie.search("Python"))  # False

print(trie.starts_with("Pro"))  # True
print(trie.starts_with("Ali"))  # False

from createTrie import *

# let's use the trie we created in createTrie.py
trie = Trie()

# insert some words by asking the user to enter them
word = input("Enter a word to insert into the trie: ")
while word != "":
     trie.insert(word)
     word = input("Enter a word to insert into the trie: ")

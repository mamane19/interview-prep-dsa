// # This question is asked by Microsoft.
// # Implement a trie class that supports insertion and search functionalities.
// # Note: You may assume only lowercase alphabetical characters will added to your trie.

// # Ex: Given the following operations on your trie…

// # Trie trie = new Trie()
// # trie.insert("programming");
// # trie.search("computer") // returns false.
// # trie.search("programming") // returns true.

class TrieNode {
  constructor(public children: object, public isWord: boolean) {
    this.children = {};
    this.isWord = false;
  }
}

class Trie {
  root: TrieNode;
  constructor() {
    this.root = new TrieNode({}, false);
  }

  public insert(word: string) {
    let currentNode = this.root;
    for (const letter of word) {
      if (!currentNode.children[letter]) {
        currentNode.children[letter] = new TrieNode({}, false);
      }
      currentNode = currentNode.children[letter];
    }
    currentNode.isWord = true;
  }

  public search(word: string) {
    let currentNode = this.root;
    for (const letter of word) {
      if (!currentNode.children[letter]) {
        return false;
      }
      currentNode = currentNode.children[letter];
    }
    return currentNode.isWord;
  }

  public startsWith(prefix: string) {
    let currentNode = this.root;
    for (const letter of prefix) {
      if (!currentNode.children[letter]) {
        return false;
      }
      currentNode = currentNode.children[letter];
    }
    return true;
  }
}

const trie = new Trie();
trie.insert("programming");
trie.insert("program");
trie.insert("programmer");
console.log(trie);
console.log(trie.search("programming"));
console.log(trie.search("program"));
console.log(trie.search("programmer"));
console.log(trie.startsWith("program"));
console.log(trie.startsWith("programming"));
console.log(trie.startsWith("programmer"));
console.log(trie.startsWith("programminger"));

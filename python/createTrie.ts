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
    for (let i = 0; i < word.length; i++) {
      const char = word[i];
      if (!currentNode.children.hasOwnProperty(char)) {
        currentNode.children[char] = new TrieNode({}, false);
      }
      currentNode = currentNode.children[char];
    }

    currentNode.isWord = true;
  }

  public search(word: string) {
    let currentNode = this.root;
    for (let i = 0; i < word.length; i++) {
      const char = word[i];
      if (!currentNode.children[char]) {
        return false;
      }
      currentNode = currentNode.children[char];
    }
    return currentNode.isWord;
  }

  public startsWith(prefix: string) {
    let currentNode = this.root;
    for (let i = 0; i < prefix.length; i++) {
      const char = prefix[i];
      if (!currentNode.children[char]) {
        return false;
      }
      currentNode = currentNode.children[char];
    }
    return true;
  }

  public print() {
    console.log(this.root);
  }
}

const trie = new Trie();
trie.insert("programming");
trie.insert("program");
trie.insert("programmer");

trie.search("programming"); // returns true.
trie.search("program"); // returns true.
trie.search("programmer"); // returns true.
trie.search("programmingx"); // returns false.

trie.startsWith("pra"); // returns false.
trie.startsWith("pro"); // returns true.
trie.startsWith("prog"); // returns true.
trie.startsWith("progra"); // returns false.

trie.print();

// const trie = new Trie();
// trie.insert("programming");
// trie.insert("program");
// trie.insert("programmer");
// console.log(trie);
// console.log(trie.search("programming"));
// console.log(trie.search("program"));
// console.log(trie.search("programmer"));
// console.log(trie.startsWith("program"));
// console.log(trie.startsWith("programming"));
// console.log(trie.startsWith("programmer"));
// console.log(trie.startsWith("programminger"));

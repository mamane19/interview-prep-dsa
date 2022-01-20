// # This question is asked by Microsoft.
// # Implement a trie class that supports insertion and search functionalities.
// # Note: You may assume only lowercase alphabetical characters will added to your trie.
// # Ex: Given the following operations on your trie…
// # Trie trie = new Trie()
// # trie.insert("programming");
// # trie.search("computer") // returns false.
// # trie.search("programming") // returns true.
var TrieNode = /** @class */ (function () {
    function TrieNode(children, isWord) {
        this.children = children;
        this.isWord = isWord;
        this.children = {};
        this.isWord = false;
    }
    return TrieNode;
}());
var Trie = /** @class */ (function () {
    function Trie() {
        this.root = new TrieNode({}, false);
    }
    Trie.prototype.insert = function (word) {
        var currentNode = this.root;
        for (var _i = 0, word_1 = word; _i < word_1.length; _i++) {
            var letter = word_1[_i];
            if (!currentNode.children[letter]) {
                currentNode.children[letter] = new TrieNode({}, false);
            }
            currentNode = currentNode.children[letter];
        }
        currentNode.isWord = true;
    };
    Trie.prototype.search = function (word) {
        var currentNode = this.root;
        for (var _i = 0, word_2 = word; _i < word_2.length; _i++) {
            var letter = word_2[_i];
            if (!currentNode.children[letter]) {
                return false;
            }
            currentNode = currentNode.children[letter];
        }
        return currentNode.isWord;
    };
    Trie.prototype.startsWith = function (prefix) {
        var currentNode = this.root;
        for (var _i = 0, prefix_1 = prefix; _i < prefix_1.length; _i++) {
            var letter = prefix_1[_i];
            if (!currentNode.children[letter]) {
                return false;
            }
            currentNode = currentNode.children[letter];
        }
        return true;
    };
    return Trie;
}());
var trie = new Trie();
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

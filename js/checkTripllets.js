// # You are given a sring s containing lowercase English letters.
// # you should check if there are three adjascent letters that are not the same.
// # If so, you count the number of such triplets and return it.
// # If there are no such triplets, return 0.

function checkTripllets(s) {
  var triplets = 0;
  for (var i = 0; i < s.length - 2; i++) {
    if (s[i] !== s[i + 1] && s[i] !== s[i + 2] && s[i + 1] !== s[i + 2]) {
      triplets += 1;
    } else {
      continue;
    }
  }
  return triplets;
}

console.log(checkTripllets('abccc'));
console.log(checkTripllets("abcdd"));
console.log(checkTripllets("abcd"));

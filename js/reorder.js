// # Given an array of objects A, and an array of indexes B, reorder the objects in array A with the given indexes in array B.
// # let a = [C, D, E, F, G, H];
// # let b = [3, 0, 4, 1, 2, 5];

// # $ reorder(a, b) // a is now [D, F, G, C, E, H]

function reorder(a, b) {
  return b.map(function(i) {
    return a[i];
  });
}


console.log(reorder(['C', 'D', 'E', 'F', 'G', 'H'], [3, 0, 4, 1, 2, 5]));

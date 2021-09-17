// # You are given two arrays of strings, A and B.
// # Check if there is a string in array B which is a conatenation of some of the strings in array A.
// # if there is, return true, else return false.
// # For example,
// # A = ["one", "two", "three"]
// # B = ["one", "onetwo", "four"] => return true
// # B = ["one", "two", "three", "four"] => return false
// # B = ["one", "two", "three", "four", "five"] => return false
// # B = ["one", "two", "three", "four", "five", "six"] => return false

function checkConcatenation(A, B) {
       var isConcatenation = false;

  // loop through B
  for (var i = 0; i < B.length; i += 1) {
    var concatenated = B[i];

    // loop through A
    for (var j = 0; j < A.length; j += 1) {
      var string = A[j];

      // if concatenated string is in A, return true
      if (concatenated.indexOf(string) !== -1) {
        isConcatenation = true;
        break;
      }
    }

    // if concatenated string is not in A, return false
    if (!isConcatenation) {
      return false;
    }
  }

  // return true if concatenated string is in A
  return isConcatenation;
}

console.log(checkConcatenation(["one", "two", "three"], ["one", "onetwo", "four"]));
console.log(checkConcatenation(["one", "two", "three", "four"], ["one", "two", "three", "four", "five"]));
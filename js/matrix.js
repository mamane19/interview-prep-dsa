// # You're given a matrix of integers. 0 represents an empty espace.
// # Determine if there are any integers that have at least 4 sequential values across the rows, columns, and diagonals.
// # If there is Return the number.
// # Sample Input1:
// # [[0 1 3 2 1]
// # [0 3 2 4 1]
// # [1 1 1 1 0]]

// # Sample Output1: 1

// # Sample Input2:
// # [[5 1 0 3 2]
// # [0 5 2 4 1]
// # [1 3 5 1 0]
// # [2 2 1 5 0]]

// # Sample Output2: 5

// # Sample Input3:
// # [[2 1 0 3 2]
// # [2 1 2 4 1]
// # [2 3 1 1 0]
// # [2 1 1 0 1]
// # [0 2 1 1 0]]

// # Sample Output3: 2

function matrix(matrix) {
  let count = 0;
  let rows = matrix.length;
  let cols = matrix[0].length;

  // check rows
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      let val = matrix[i][j];
      if (val === 0) continue;
      let count = 1;
      for (let k = j + 1; k < cols; k++) {
        if (matrix[i][k] === val) {
          count++;
        } else {
          break;
        }
      }
      if (count >= 4) return val;
    }
  }

  // check columns
  for (let i = 0; i < cols; i++) {
    for (let j = 0; j < rows; j++) {
      let val = matrix[j][i];
      if (val === 0) continue;
      let count = 1;
      for (let k = j + 1; k < rows; k++) {
        if (matrix[k][i] === val) {
          count++;
        } else {
          break;
        }
      }
      if (count >= 4) return val;
    }
  }

  // check diagonals
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      let val = matrix[i][j];
      if (val === 0) continue;
      let count = 1;
      let k = i + 1;
      let l = j + 1;
      while (k < rows && l < cols) {
        if (matrix[k][l] === val) {
          count++;
        } else {
          break;
        }
        k++;
        l++;
      }
      if (count >= 4) return val;
    }
  }

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      let val = matrix[i][j];
      if (val === 0) continue;
      let count = 1;
      let k = i - 1;
      let l = j + 1;
      while (k >= 0 && l < cols) {
        if (matrix[k][l] === val) {
          count++;
        } else {
          break;
        }
        k--;
        l++;
      }
      if (count >= 4) return val;
    }
  }

  return 0;
}

console.log(
  matrix([
    [0, 1, 3, 2, 1],
    [0, 3, 2, 4, 1],
    [1, 1, 1, 1, 0],
  ])
);
console.log(
  matrix([
    [5, 1, 0, 3, 2],
    [0, 5, 3, 2, 1],
    [1, 3, 2, 1, 0],
    [3, 0, 1, 5, 0],
  ])
);
console.log(
  matrix([
    [2, 1, 0, 3, 2],
    [2, 1, 2, 4, 1],
    [2, 3, 1, 1, 0],
    [2, 1, 1, 0, 1],
    [0, 2, 1, 1, 0],
  ])
);

// console.log(findLongestSequence([[0, 1, 3, 2, 1], [0, 3, 2, 4, 1], [1, 1, 1, 1, 0]]));
// console.log(findLongestSequence([[5, 1, 0, 3, 2], [0, 5, 2, 4, 1], [1, 3, 5, 1, 0], [2, 2, 1, 5, 0]]));
// console.log(findLongestSequence([[2, 1, 0, 3, 2], [2, 1, 2, 4, 1], [2, 3, 1, 1, 0], [2, 1 ,1, 0, 1], [0, 2, 1, 1, 0]]));

// Write a function that takes a 2D array and returns a 1D array of all the array's elements in spiral order.

function spiralTraversal(array) {
  let result = [];
  let startRow = 0;
  let endRow = array.length - 1;
  let startCol = 0;
  let endCol = array[0].length - 1;

  while (startRow <= endRow && startCol <= endCol) {
    // top row
    for (let i = startCol; i <= endCol; i++) {
      result.push(array[startRow][i]);
    }
    startRow++;

    // right column
    for (let i = startRow; i <= endRow; i++) {
      result.push(array[i][endCol]);
    }
    endCol--;

    // bottom row
    for (let i = endCol; i >= startCol; i--) {
      result.push(array[endRow][i]);
    }
    endRow--;

    // left column
    for (let i = endRow; i >= startRow; i--) {
      result.push(array[i][startCol]);
    }
    startCol++;
  }

  return result;
}

// Test Cases
console.log(
  spiralTraversal([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
  ])
);
// [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

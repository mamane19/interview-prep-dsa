// # # Given a 2D matrix, rotate the image by 90 degrees (clockwise).
// # # 
// # # Example:
// # # [
// # # [1,2,3],
// # # [4,5,6],
// # # [7,8,9]] 
// # # -> [
// # # [7,4,1],
// # # [8,5,2],
// # # [9,6,3]]
// # # e.g2:
// # # [
// # # [ 5, 1, 9,11],
// # # [ 2, 4, 8,10],
// # # [13, 3, 6, 7],
// # # [15,14,12,16]
// # # ]
// # # -> [
// # # [15,13, 2, 5],
// # # [14, 3, 4, 1],
// # # [12, 6, 8, 9],
// # # [16, 7,10,11]
// # # ]

function rotateImage(matrix) {
  var n = matrix.length;
  for (var layer = 0; layer < n / 2; layer++) {
    var first = layer;
    var last = n - 1 - layer;
    for (var i = first; i < last; i++) {
      var offset = i - first;
      var top = matrix[first][i];
      matrix[first][i] = matrix[last - offset][first];
      matrix[last - offset][first] = matrix[last][last - offset];
      matrix[last][last - offset] = matrix[i][last];
      matrix[i][last] = top;
    }
  }
  return matrix;
}

var matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

console.log(rotateImage(matrix));

var matrix2 = [
  [5, 1, 9, 11],
  [2, 4, 8, 10],
  [13, 3, 6, 7],
  [15, 14, 12, 16]
];


console.log(rotateImage(matrix2));
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

public class rotateImage {
     // let's have an O(n) solution
     // we can do this by swapping the elements in the matrix
     public void rotate(int[][] matrix) {
        int n = matrix.length;
        for(int i = 0; i < n; i++) {
            for(int j = i; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n/2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n-j-1];
                matrix[i][n-j-1] = temp;
            }
        }
    }
    // let's test it
    public static void main(String[] args) {
        int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
        rotateImage ri = new rotateImage();
        ri.rotate(matrix);
        for(int i = 0; i < matrix.length; i++) {
            for(int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
        int[][] matrix2 = {{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}};
        ri.rotate(matrix2);
        for(int i = 0; i < matrix2.length; i++) {
            for(int j = 0; j < matrix2[i].length; j++) {
                System.out.print(matrix2[i][j] + " ");
            }
            System.out.println();
        }
    }
}
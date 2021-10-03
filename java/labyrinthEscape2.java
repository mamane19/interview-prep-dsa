// You're exploring a mysterious labyrinth in the shape of a rectangular matrix, containing obstacles and teleports. Starting from the upper-left corner, you're wondering if it's possible to reach the lower-right corner by only moving to the right.

// You are given integers n and m representing the dimensions of the labyrinth, as well as obstacles and teleports, which are lists containing the coordinates of all the obstacles and teleports respectively.

// Here's how everything in the labyrinth works:

// An obstacle cannot be traversed - you must stop immediately if you reach a cell containing an obstacle.
// A teleport is a pair of cells (start, end), where start is the starting cell of teleportation, and end is the destination cell. If you reach the start cell, you are immediately teleported to the end cell.
// Note that it doesn't work backwards: you cannot teleport from the end point to the start point.
// It is guaranteed that there are no teleports with the same starting points (i.e. each cell has at most one option for teleportation).
// It is guaranteed that the destination cell for a teleport cannot be a starting cell for another teleport.
// It is also guaranteed that both the starting and destination cells of the teleport do not contain obstacles.
// Any cell that doesn't contain an obstacle or a teleport is considered a free cell, and you can walk through it normally.
// You start at the upper-left corner cell with coordinates (0, 0) and the goal is located at the cell with coordinates (n - 1, m - 1). You move according to the following rules:

// You will always move to the right: if you're currently standing on the cell with coordinates (row, col), you will try moving to the cell with coordinates (row, col + 1).
// If the destination cell is the starting point of a teleport, proceed to the teleportation end point.
// If the destination cell contains an obstacle, stop moving and stay where you are.
// If the destination cell is outside the labyrinth bounds, try moving to the beginning of the next row - cell with coordinates (row + 1, 0).
// Your task is to check whether you can reach the exit of the labyrinth by following the algorithm above. Return true if you will eventually reach the goal, and false otherwise.

// It's guaranteed that the starting cell (0, 0) and the goal cell (n - 1, m - 1) do not contain an obstacle or the start point of a teleport.

// Example

// For n = 3, m = 3, obstacles = [[2, 1]], and teleports = [[0, 1, 2, 0]], the output should be labyrinthEscape2(n, m, obstacles, teleports) = false

public class labyrinthEscape2 {
     public boolean labyrinthEscape(int m, int n, int[][] obstacles, int[][] teleports) {
          Node[][] grid = new Node[m][n];
          for (int i = 0; i < m; i++) {
               for (int j = 0; j < n; j++) {
                    Node node = new Node();
                    grid[i][j] = node;
               }
          }

          for (int[] obstacle : obstacles) {
               Node curr = grid[obstacle[0]][obstacle[1]];
               curr.hasObstacle = true;
          }

          for (int[] teleport : teleports) {
               Node curr = grid[teleport[0]][teleport[1]];
               curr.hasTeleport = true;
               curr.teleX = teleport[2];
               curr.teleY = teleport[3];
          }

          int x = 0, y = 0;
          while (true) {
               if (x == m - 1 && y == n - 1)
                    return true;

               Node curr = grid[x][y];
               if (curr.isVisited)
                    return false;

               if (curr.hasObstacle)
                    return false;

               curr.isVisited = true;

               if (curr.hasTeleport) {
                    x = curr.teleX;
                    y = curr.teleY;
               } else {
                    y += 1;
                    if (y == n)
                         return false;
               }
          }

     }

     class Node {
          boolean hasObstacle;
          boolean hasTeleport;
          int teleX;
          int teleY;
          boolean isVisited;

          public Node() {

          }
     }
}
// # Two players are playing a game where white or black pieces are represented by a string, colors.
// # The game rules are as follows:
// # - Wendy  moves first and then they take alternate turns.
// # - With each move Wendy may remove a white piece that has adjacent white pieces on both sides.
// # - Likewise, with each move, Bob may remove a black piece that has adjacent black pieces on both sides.
// # - After a piece is removed, the string is reduced in size by one piece. For instance, removing 'Y' from 
// # 'XYZ' results in 'XZ'.
// # - When a player can no longer move, they have lost the game.

// # Example: 
// # colors = 'wwwbbbbwww'
// # Wendy  removes the piece 'w' at index 1, colors = 'wwbbbwww'.
// # Bob removes the piece 'b' at index 3, colors = 'wwbbbwww'.
// # Wendy removes the piece 'w' at index 6, colors = 'wwbbbww'.
// # Bob removes the piece 'b' at index 3, colors = 'wwbbww'.
// # Wendy has no more moves and is out of the game. Bob wins.

// # Determine who wins if Wendy and Bob play with optimum skill.
// # Return "Bob" if Bob wins and "Wendy" if Wendy wins.

// # Function description:
// # Complete the function gameWinner in the editor below. It must return a string, either "Bob" or "Wendy".
// # GameWinner has the following parameter(s):
// # String colors: each colors[i] represents the color located at index i within the colors string.
// # returns : A string: the winner of the game either "Bob" or "Wendy".

// # Sample Case 0:
// # STDIN: wwwbb --> Function: colors = 'wwwbb'
// # Sample Output 0:
// # Wendy
// # Explanation 0:
// # There are five colors in the string. Wendy can remove any of the white pieces in the first move. 
// # After that, the colors string becomes 'wwbb'.  Bob has no move since there is no black piece with 
// # exactly two black adjacent pieces. So Wendy wins.

public class Solution {
    /*
     * Complete the 'gameWinner' function below.
     *
     * The function is expected to return a STRING. The function accepts STRING
     * colors as parameter.
     */
    public static String gameWinner(String colors) {
        // Let's check if colors contain 'b'
        if (!colors.contains("b") && colors.length() == 2) {
            return "bob";
        }
        int wendy = 0;
        int bob = 0;
        for (int i = 0; i < colors.length(); i++) {
            if (colors.charAt(i) == 'w') {
                wendy++;
            } else if (colors.charAt(i) == 'b') {
                bob++;
            }
        }
        if (wendy < bob) {
            return "bob";
        } else if (wendy > bob) {
            return "wendy";
        } else {
            return "bob";
        }
    }

    public static void main(String[] args) {
        System.out.println(gameWinner("wwwbbbbwww"));
    }
}

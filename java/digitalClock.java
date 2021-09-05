// Programming challenge description:
// Take a time as an input and output a multiline string representing the input, each digit made up from a 5 by 5 grid with a single space between each digit.

// The separator represented as a colon ":", in its own 5 by 5 grid.

// Input:
// 88:88
// Output:
// ##### #####       ##### #####
// #   # #   #   #   #   # #   #
// ##### #####       ##### #####
// #   # #   #   #   #   # #   #
// ##### #####       ##### #####
// Example
// Input:

// 14:79
// Output:

//     # #   #       ##### ##### 
//     # #   #   #       # #   # 
//     # #####           # ##### 
//     #     #   #       #     # 
//     #     #           #     # 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.stream.IntStream;

public class digitalClock {
  /**
   * Iterate through each line of input.
   */
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    while ((line = in.readLine()) != null) {
      createClock(line);
    }
  }
  
  public static void createClock(String input) {
      
  }
}
// # You are given a sring s containing lowercase English letters.
// # you should check if there are three adjascent letters that are not the same.
// # If so, you count the number of such triplets and return it.
// # If there are no such triplets, return 0.

class CheckTriplets {
     public static void triplets(String s) {
          int count = 0;
          for (int i = 0; i < s.length() - 2; i++) {
               if (s.charAt(i) != s.charAt(i + 1) && s.charAt(i) != s.charAt(i + 2)
                         && s.charAt(i + 1) != s.charAt(i + 2)) {
                    count++;
               } else {
                    continue;
               }
          }
          System.out.println(count);
     }

     // let's try it
     public static void main(String[] args) {
          String s = "aabbcc";
          triplets(s);
          String l = "abcdef";
          triplets(l);
     }

}
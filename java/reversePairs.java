public class reversePairs {
     public int reverseDigitsInPairs(int n) {
          String str = n + "";
          StringBuilder sb = new StringBuilder();
          for (int i = 0; i < str.length(); i = i + 2) {
               if (i + 1 < str.length()) {
                    sb.append(str.charAt(i + 1));
                    sb.append(str.charAt(i));
               } else {
                    sb.append(str.charAt(i));
               }
          }
          return Integer.parseInt(sb.toString());
     }
}

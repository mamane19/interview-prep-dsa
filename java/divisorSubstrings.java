import java.util.*;

public class divisorSubstrings {
     public static int countSubStr(int n, int k) {
          String str = String.valueOf(n);
          int count = 0;
          long strNum = Long.parseLong(str);
          Set<String> set = new HashSet<>();
          for (int i = 0; i < str.length(); i++) {
              for (int j = i + 1; j <= str.length(); j++) {
                  String sub = str.substring(i, j);
                  if(sub.length() == k) {
                      long num = Long.parseLong(sub);
                      if (num != 0 && strNum % num == 0 && !set.contains(sub)) {
                          count++;
                          set.add(sub);
                      }
                  }
              }
          }
          return count;
      }
}

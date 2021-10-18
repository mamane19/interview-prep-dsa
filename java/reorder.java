// # Given an array of objects A, and an array of indexes B, reorder the objects in array A with the given indexes in array B.
// # let a = [C, D, E, F, G, H];
// # let b = [3, 0, 4, 1, 2, 5];

// # $ reorder(a, b) // a is now [D, F, G, C, E, H]

public class reorder {
     public static void Reorder(Object[] a, int[] b) {
          Object[] c = new Object[a.length];
          for (int i = 0; i < b.length; i++) {
               c[i] = a[b[i]];
          }
          for (int i = 0; i < a.length; i++) {
               a[i] = c[i];
          }
     }

     public static void main(String[] args) {
          Object[] a = { "C", "D", "E", "F", "G", "H" };
          int[] b = { 3, 0, 4, 1, 2, 5 };
          Reorder(a, b);
          for (int i = 0; i < a.length; i++) {
               System.out.print(a[i] + " ");
          }
     }
}

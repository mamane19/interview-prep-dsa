
function mutateTheArray(n, a) {
     b = [0] * n;
     for (i = 0; i < n; i++) {
         b[i] = a[i];
     }
     for (i = 0; i < n; i++) {
         if (b[i] % 2 == 1) {
             b[i] = b[i] + 1;
         }
     }
     return b;
 }   



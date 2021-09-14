import java.util.List;
import java.util.Map;

// # Write a function that asks a user to input a number, and you need to print it in words.
// # If the number is less than or equal to zero, your function should print "minus".

public class convertNumberToString {
     public static void convertNumberToString(double d) {
        if (d < 0) {
            return "minus" + convertNumberToString(-d);
        } else if (d == 0) {
            System.out.println("zero");
        } 
        // let's have a list of strings numbersToString
        List<String> numbersToString = List.of("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine");
        // let's a list of the tens
        List<String> tens = List.of("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen");

        final String result = "";
        if (d >= 1e12) {
            result += convertNumberToString(d / 1e12) + " trillion ";
            d %= 1e12;
        }


}

// // separate a string into two equal parts
// // for example, NOKNOK returns (NOK, NOK)

// public class splite {
//   public static String[] sep(String s) {
//     String[] result = new String[2];
//     result[0] = s.substring(0, s.length() / 2);
//     result[1] = s.substring(s.length() / 2);
//     return result;
//   }
//   public static void main(String[] args) {
//     String s = "NOKEUR";
//     String[] result = sep(s);
//     System.out.println(result[0]);
//     System.out.println(result[1]);
//   }


// public static void determineExchangeRate(String line) {
//   String[] rates = line.split(";");
//   String[] rate2Parts = rates[2].split("|");
//   String rate2 = rate2Parts[0];
//   // String rate2Pair = rate2Parts[1];
//   String[] currencyPair = line.split("\\|");
//   String currentPair = currencyPair[1];
//   // split the currentPair into two equal parts for ex: if we have NOKNOK we split
//   // it into NOK and NOK
//   String[] currentPairParts = new String[2];
//   currentPairParts[0] = currentPair.substring(0, 3);
//   currentPairParts[1] = currentPair.substring(3);
//   String baseCurrency = rate2.split(":")[0];
//   // split the baseCurrency into two equal parts for ex: if we have NOK we split
//   // it into NOK and NOK
//   String[] baseCurrencyParts = new String[2];
//   baseCurrencyParts[0] = baseCurrency.substring(0, 3);
//   baseCurrencyParts[1] = baseCurrency.substring(3);
//   // String quoteCurrency = rates[2].split(":")[1];

//  // if the currentPair is equal to the baseCurrency, the rate is the same
//   if (currentPair == baseCurrency ) {
//     System.out.println(currentPair + ":" + rate2.split(":")[1]);
//   }
//   // if the the first part of the currenPair is equal to the second part of the
//   // currentPair
//   // then the rate is 1.00
//   else if (currentPairParts[0].equals(currentPairParts[1])) {
//     System.out.println(currentPair + ":1.00");
//   }
//   // if currentPair[0] is equal to baseCurrent[1] and currentPair[1] is equal to
//   // baseCurrent[0]
//   // then the rate is the reverse of the quoteCurrency
//   else if (currentPairParts[0].equals(baseCurrencyParts[1]) && currentPairParts[1].equals(baseCurrencyParts[0])) {
//     System.out.println(currentPair + ":" + 1 / Double.parseDouble(rate2.split(":")[1]));
//   } else {
//     // if we can not find the rate for the currentPair, we print the error message
//     System.out.println("Unable to determine rate for " + currentPair);
//   }
// }
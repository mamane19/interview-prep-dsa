
// Programming challenge description:
// A currency pair is the quotation of two currencies, with the value of one currency being 
// quoted against the other. Currencies are identified by a three letter alphabetic ISO code 
// they are associated with on the international market.

// The first listed currency of a currency pair is called the base currency and the second currency 
// is called the quote currency. It indicates how much of the quote currency is needed to purchase 
// one unit of the base currency.

// For example, the quotation EURUSD 1.25 means that one Euro is exchanged for 1.25 US Dollars. EUR is 
// the base currency and USD is the quote currency.

// Given a list of currency pair quotations calculate the provided exchange rate.

// If the requested currency pairs are the same, for example, USDUSD, then the exchange rate is always 1.00

// Likewise if you have a rate for USDGBP and you need GBPUSD then you can invert the rate to obtain the 
// exchange rate.

// Input:
// A list of currency exchange rates separated by ';'. A currency pair to calculate separated by '|' from 
// the rest of the input.

// Output:
// Calculated exchange rate for the provided currency pair. Required precision is 2 decimal points.

// If you cannot calculate the exchange rate the expected output should be:

// 'Unable to determine rate for <currency pair>'.

// Examples

// Example 1
// Input:
// EURUSD:1.20;USDGBP:0.70|EURGBP
// Output:
// EURGBP:0.84

// Example 2
// Input:
// EURUSD:1.20;USDGBP:0.70|GBPEUR
// Output:
// GBPEUR:1.19

// Example 3
// Input:
// EURUSD:1.20;USDGBP:0.70|GBPJPY
// Output:
// Unable to determine rate for GBPJPY

// Example 4
// Input:
// EURUSD:1.20;USDGBP:0.70;GBPJPY:154.92|EURJPY
// Output:
// EURJPY:130.13

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.text.DecimalFormat;
import java.util.*;

public class Main {
  /**
   * Iterate through each line of input.
   */
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    while ((line = in.readLine()) != null) {
      determineExchangeRate(line);
    }
  }

  /**
   * Iterate through each line of input.
   */
  public static void determineExchangeRate(String line) {
    String[] rates = line.split(";");
    String[] rate2Parts = rates[2].split("\\|");
    String rate2 = rate2Parts[0];
    // String rate2Pair = rate2Parts[1];
    String[] currencyPair = line.split("\\|");
    String currentPair = currencyPair[1];
    // split the currentPair into two equal parts for ex: if we have NOKNOK we split
    // it into NOK and NOK
    String[] currentPairParts = new String[2];
    currentPairParts[0] = currentPair.substring(0, 3);
    currentPairParts[1] = currentPair.substring(3);
    String baseCurrency = rate2.split(":")[0];
    // split the baseCurrency into two equal parts for ex: if we have NOK we split
    // it into NOK and NOK
    String[] baseCurrencyParts = new String[2];
    baseCurrencyParts[0] = baseCurrency.substring(0, 3);
    baseCurrencyParts[1] = baseCurrency.substring(3);
    // String quoteCurrency = rates[2].split(":")[1];

    // if the currentPair is equal to the baseCurrency, the rate is the same
    if (currentPair.equals(baseCurrency)) {
      System.out.println(currentPair + ":" + rate2.split(":")[1]);
    }
    // if the the first part of the currenPair is equal to the second part of the
    // currentPair
    // then the rate is 1.00
    else if (currentPairParts[0].equals(currentPairParts[1])) {
      System.out.println(currentPair + ":1.00");
    }
    // if currentPair[0] is equal to baseCurrent[1] and currentPair[1] is equal to
    // baseCurrent[0]
    // then the rate is the reverse of the quoteCurrency
    else if (currentPairParts[0].equals(baseCurrencyParts[1]) && currentPairParts[1].equals(baseCurrencyParts[0])) {
      // Let's print at 2 decimal points precision
      double rate = 1 / Double.parseDouble(rate2.split(":")[1]);
      DecimalFormat f = new DecimalFormat("#.##");
      System.out.println(currentPair + ":" + f.format(rate));
    } else {
      // if we can not find the rate for the currentPair, we print the error message
      System.out.println("Unable to determine rate for " + currentPair);
    }
  }
}

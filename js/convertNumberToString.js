// # Write a function that asks a user to input a number, and you need to print it in words.
// # If the number is less than or equal to zero, your function should print "minus".

// A recursive approach is used to solve this problem. (A recursive function is a function that calls itself.). 
// Lol Knowing this, does not mean you undertand recursion haha.
function convertNumberToString(number) {
  // base cases
  if (number === 0) {
    return "zero";
  } else if (number < 0) {
    return "minus " + convertNumberToString(-number);
  }
  var string = "";
  // let's handle the trillions
  if (number >= 1e12) {
    string += convertNumberToString(Math.floor(number / 1e12)) + " trillion "; 
    number %= 1e12;
  }
  // let's handle the billions
  if (number >= 1e9) {
    string += convertNumberToString(Math.floor(number / 1e9)) + " billion ";
    number %= 1e9;
  }
  // let's handle the millions
  if (number >= 1e6) {
    string += convertNumberToString(Math.floor(number / 1e6)) + " million ";
    number %= 1e6;
  }
  // let's handle the thousands
  if (number >= 1000) {
    string += convertNumberToString(Math.floor(number / 1000)) + " thousand ";
    number %= 1000;
  }
  // let's handle the hundreds
  if (number >= 100) {
    string += convertNumberToString(Math.floor(number / 100)) + " hundred ";
    number %= 100;
  }
  // let's handle the tens
  if (number > 0) {
    if (string != "") {
      string += "and "; // add the "and" if we already have some number
    }
    // we need to handle the teens
    if (number < 20) {
      string += numberToString[number]; // add the number
    } else {
      string += tensToString[Math.floor(number / 10)];
      if (number % 10 > 0) {
        // add the remainder
        string += "-" + numberToString[number % 10];
      }
    }
  }
  return string;
}

var numberToString = [
  "zero",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
  "ten",
  "eleven",
  "twelve",
  "thirteen",
  "fourteen",
  "fifteen",
  "sixteen",
  "seventeen",
  "eighteen",
  "nineteen",
];
var tensToString = [
  "zero",
  "ten",
  "twenty",
  "thirty",
  "forty",
  "fifty",
  "sixty",
  "seventy",
  "eighty",
  "ninety",
];

// let's try to run some tests
console.log(convertNumberToString(0));
console.log(convertNumberToString(3));
console.log(convertNumberToString(10));
console.log(convertNumberToString(11));
console.log(convertNumberToString(12));
console.log(convertNumberToString(20));
console.log(convertNumberToString(21));
console.log(convertNumberToString(30));
console.log(convertNumberToString(40));
console.log(convertNumberToString(50));
console.log(convertNumberToString(60));
console.log(convertNumberToString(70));
console.log(convertNumberToString(80));
console.log(convertNumberToString(90));
console.log(convertNumberToString(100));
console.log(convertNumberToString(101));
console.log(convertNumberToString(110));
console.log(convertNumberToString(2001));
console.log(convertNumberToString(10000));
console.log(convertNumberToString(10001));
console.log(convertNumberToString(100000));
console.log(convertNumberToString(100007));
console.log(convertNumberToString(1000000));
console.log(convertNumberToString(10000007));
console.log(convertNumberToString(10000000));
console.log(convertNumberToString(100000000));
console.log(convertNumberToString(1000000000));
console.log(convertNumberToString(1000000007));
console.log(convertNumberToString(10000000000));
console.log(convertNumberToString(145767457291));
console.log(convertNumberToString(1000000000000));
console.log(convertNumberToString(1454674572915,23));
console.log(convertNumberToString(-3));
console.log(convertNumberToString(-10));
console.log(convertNumberToString(-11));

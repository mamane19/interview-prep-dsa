# Write a function that asks a user to input a number, and you need to print it in words.
# If the number is less than or equal to zero, your function should print "minus".


def convert_to_words(num):
    
    l = len(num)

    # Base or edge case
    if l == 0:
        print("empty string")
        return

    if l > 4:
        print("Chill! We do not do that here!")
        return

    
    single_digits = [
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
    ]

    
    two_digits = [
        "",
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
    ]

    
    tens_multiple = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    tens_power = ["hundred", "thousand"]

    # Used for debugging purpose only
    print(num, ":", end=" ")

    # For single digit number
    if l == 1:
        print(single_digits[ord(num[0]) - 48])
        return

    # In other cases (not 0)
    x = 0
    while x < len(num):

        if l >= 3:
            if ord(num[x]) - 48 != 0:
                print(single_digits[ord(num[x]) - 48], end=" ")
                print(tens_power[l - 3], end=" ")
                # here len can be 3 or 4

            l -= 1
        else:
            if ord(num[x]) - 48 == 1:
                print(two_digits[ord(num[x + 1]) - 48], end=" ")
                l -= 1
            else:
                print(tens_multiple[ord(num[x]) - 48], end=" ")
                l -= 1
        x += 1
    print()
    return

if __name__ == "__main__":
    num = input("Enter a number: ")
    convert_to_words(num)

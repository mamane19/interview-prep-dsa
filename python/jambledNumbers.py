# Programming challenge description:
# In this challenge, you're given a string containing jumbled letters from several concatenated words.
# Each word is a numeral from zero to nine. Each numeral may be used multiple times in the jumbled string.

# Write a program that returns integers corresponding to the numerals used to form the jumbled string.
# Integers must be sorted in ascending order.

# For example, reuonnoinfe are shuffled letters of the strings one four nine.
# Your program's output should be 149.

# An example of a jumbled string is:
# "fviefuro" and this is the jumbled string of 4 and 5

# Input:
# A string formed from jumbled letters of numerals. For example:

# reuonnoinfe
# Output:
# A sequence of integers used to form the string in ascending order. For example:
# 149

# * Test 1
# Test Input:
# reuonnoinfe
# Expected Output:
# 149

# * Test 2
# Test Input:
# oeisowufxrzohgiettr
# Expected Output
# 02468

# * Test 3
# Test Input:
# veiifogvweesotwnetnvfeheiot
# Expected Output:
# 1225578

# * Test 4
# Test Input:
# xtneiootnrnoeneeeeuoeoheetehounzoiuetrhfefeezuivirfwieotgoottfnrnneghetserhrwsgesfherhtiitrerevreernhveo
# Expected Output:
# 0011122333334444567788899


def finddigits(s):

    # Strings of digits 0-9
    num = [
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

    # Initialize vector
    arr = [0] * (10)

    # Initialize answer
    ans = ""

    # Size of the string
    n = len(s)

    # Traverse the string
    for i in range(n):
        if s[i] == "z":
            arr[0] += 1
        if s[i] == "w":
            arr[2] += 1
        if s[i] == "g":
            arr[8] += 1
        if s[i] == "x":
            arr[6] += 1
        if s[i] == "v":
            arr[5] += 1
        if s[i] == "o":
            arr[1] += 1
        if s[i] == "s":
            arr[7] += 1
        if s[i] == "f":
            arr[4] += 1
        if s[i] == "h":
            arr[3] += 1
        if s[i] == "i":
            arr[9] += 1

    # Update the elements of the vector
    arr[7] -= arr[6]
    arr[5] -= arr[7]
    arr[4] -= arr[5]
    arr[1] -= arr[2] + arr[4] + arr[0]
    arr[3] -= arr[8]
    arr[9] -= arr[5] + arr[6] + arr[8]

    # Print the digits into their
    # original format
    for i in range(10):
           for j in range(arr[i]):
                ans += chr((i) + ord("0"))

    # Return answer
    return ans


if __name__ == "__main__":
    print(
        finddigits(
            "xtneiootnrnoeneeeeuoeoheetehounzoiuetrhfefeezuivirfwieotgoottfnrnneghetserhrwsgesfherhtiitrerevreernhveo"
        )
    )

# Given a positive integer n, write a function that finds the number of zeros at the end of n! in base 10.
# Example:
#  zerosEndingFactorial(1)
#  0

# zerosEndingFactorial(5)
#  1

# zerosEndingFactorial(100)
# 24

def zerosEndingFactorial(n):
    return n // 5 + zerosEndingFactorial(n // 5) if n > 1 else 0
if __name__ == '__main__':
    print(zerosEndingFactorial(int(input())))
# Implemenet a basic measure of tracking the time taken by an algorithm


import sys
import time


def trackTime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return ("Time taken by function: {}".format(end - start))
    return wrapper


@trackTime
def sumOfSquares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum


@trackTime
def sumOfCubes(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3
    return sum


if __name__ == "__main__":
    print(sumOfSquares(100))
    print(sumOfCubes(100))


# Implement a basic measure of tracking the space used by an algorithm

def trackSpace(func):
    def wrapper(*args, **kwargs):
        sys.setrecursionlimit(10000)
        start = sys.getsizeof(sys.getrecursionlimit())
        func(*args, **kwargs)
        end = sys.getsizeof(sys.getrecursionlimit())
        return ("Space taken by function: {}".format(end - start))
    return wrapper


@trackSpace
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(100))

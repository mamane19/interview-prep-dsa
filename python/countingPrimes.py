# This question is asked by Google. Given a positive integer N, return the number of prime numbers less than N.

# Ex: Given the following N…
# N = 3, return 1.
# 2 is the only prime number less than 3.

# Ex: Given the following N…
# N = 7, return 3.
# 2, 3, and 5 are the only prime numbers less than 7.


def count_primes(n):
    # Write your code here
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count


def is_prime(n):

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


print(count_primes(3))
print(count_primes(7))
print(count_primes(10))

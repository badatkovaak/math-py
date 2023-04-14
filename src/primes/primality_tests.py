import math


def isPrime(n):
    k = 2
    for i in range(2, n):
        if n % i == 0:
            k += 1
    return k == 2


def isPrime1(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

from general.genericFunctions import factorial
from general.constants import PHI, INVERSE_PHI, SQRT5


def binomialCoefficients(n, k):
    if k <= n:
        return int(factorial(n)/(factorial(k)*factorial(n-k)))
    else:
        return -1


# Cn counts the number of expressions containing n pairs of parentheses
# which are correctly matched.
def nthCatalanNumber1(n):
    return int(factorial(2*n)/(factorial(n+1)*factorial(n)))


# The Stirling numbers of the second kind,
# count the number of ways to partition a set of n labelled objects into
# k nonempty unlabelled subsets.
def nthStirlingNumber2kind(n, k):
    if k > n:
        return -1
    result = 0
    for i in range(k+1):
        result += ((-1)**i) * binomialCoefficients(k, i) * (k-i) ** n
    return int(result)


def nthBernoulliNumber(n):
    if n < 1:
        return -1
    result = 0
    for k in range(n+1):
        for v in range(k+1):
            result += ((-1)**v) * binomialCoefficients(k, v) * ((v**n)/(k+1))
    return result


def nthFibonacciNumber(n):
    if n == 1 or n == 2:
        return 1
    elif n < 1:
        return -1
    return int((PHI**n - INVERSE_PHI**n)/SQRT5)

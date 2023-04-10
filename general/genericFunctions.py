def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def exponent(x):
    result = 1
    for i in range(1, 20):
        result += x/factorial(i)
    return result


def sqrt(x):
    if x <= 0:
        return -1
    result = x
    for i in range(30):
        result = 1/2*(result + x/result)
    return result

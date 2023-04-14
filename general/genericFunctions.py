import math


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def exp(x):
    result = 1
    for i in range(1, 50):
        result += (x**i)/factorial(i)
    return result


def sqrt(x):
    if x <= 0:
        return -1
    result = x
    for i in range(30):
        result = 1/2*(result + x/result)
    return result


def integrate(f, a, b, dx=0.0001):
    result = 0
    for i in range(math.floor((b-a)/dx)+1):
        result += dx * f(a + dx*i)
    return result


def integrate1(f, a, b, n=-1):
    result = f(a)/2 + f(b)/2
    if n == -1:
        n = math.floor((b-a)/0.0001)
    for i in range(1, n):
        result += f(a + i*(b-a)/n)
    return result * ((b-a)/n)


# def naturalLog(x, dx=0.0001):
#     if x <= 0:
#         raise ValueError
#     result = 0
#     if x >= 1:
#         for i in range(math.floor((x-1)/dx)+1):
#             print(i)
#             result += dx * (1/(1 + i*dx))
#     return result


# def naturalLog1(x):
#     if x == 0:
#         raise ValueError
#     if

#     while abs(x) > 1


def f1(x):
    result = 0
    for i in range(1, 20):
        result += ((-1)**(i-1)/i)*(x**i)
    return result


def AGM(x, y):
    result, x1, y1 = 0, x, y
    for _ in range(10):
        x = x1
        y = y1
        x1 = (x + y)/2
        y1 = math.sqrt(x*y)
    result = (x1 + y1)/2
    return result

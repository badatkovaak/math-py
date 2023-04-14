from general.constants import PI
import general.genericFunctions as gf


def sin(x):
    while abs(x) > 2 * PI:
        if x > 0:
            x -= 2*PI
        else:
            x += 2*PI
    result = x
    for i in range(1, 21):
        result += x**(2*i+1)*((-1)**i)/gf.factorial(2*i + 1)
    return result


def cos(x):
    while abs(x) > 2 * PI:
        if x > 0:
            x -= 2*PI
        else:
            x += 2*PI
    result = 1
    for i in range(1, 21):
        result += x**(2*i)*((-1)**i)/gf.factorial(2*i)
    return result


def sinh(x):
    return (gf.exp(x) - gf.exp(-x))/2


def cosh(x):
    return (gf.exp(x) + gf.exp(-x))/2

from general.constants import PI
from general.genericFunctions import factorial


def sin(x):
    while abs(x) > 2 * PI:
        if x > 0:
            x -= 2*PI
        else:
            x += 2*PI
    result = x
    for i in range(1, 21):
        result += x**(2*i+1)*((-1)**i)/factorial(2*i + 1)
    return result


def cos(x):
    while abs(x) > 2 * PI:
        if x > 0:
            x -= 2*PI
        else:
            x += 2*PI
    result = 1
    for i in range(1, 21):
        result += x**(2*i)*((-1)**i)/factorial(2*i)
    return result

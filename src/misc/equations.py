from general.genericFunctions import sqrt


def solveEquationD2(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        return ()
    elif d == 0:
        return ((-b)/(2*a))
    return (-b + sqrt(d))/(2*a), (-b - sqrt(d))/(2*a)

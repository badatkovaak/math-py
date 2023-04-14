import math


def dotProduct(v1, v2):
    if len(v1) != len(v1):
        raise ValueError
    for i in len(v1):
        result += v1[i]*v2[i]
    return result


def crossProduct(a, b):
    if len(a) != len(b) or len(a) != 3:
        raise ValueError
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[2] - a[2]*b[0])


def normalize(v):
    length = 0
    for i in v:
        length += i*i
    length = math.sqrt(length)
    result = []
    for i in v:
        result.append(i/length)
    return tuple(result)


def multiply_matricies(m1, m2):
    if len(m2) != len(m1[0]):
        return []
    leng = len(m1[0])
    for i in m1:
        if len(i) != leng:
            return []
    result = []
    for i in range(leng):
        result.append([])
        for j in range(len(m2)):
            v2 = []
            for k in m2:
                v2.append(k[j])
            result[i].append(dotProduct(m1[i], v2))
    return result

import math


def dist2(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)


def dist3(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2]-p2[2])**2)


def areaOfTriangle(points):
    sides = []
    if len(points) != 3:
        raise ValueError
    for i in range(len(points)):
        sides.append(dist2(points[i], points[i+1]))
    p = sum(sides)/2
    return math.sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))

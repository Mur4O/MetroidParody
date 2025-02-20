import math
from math import *

def degree_beetwen_vectors(point1, point2, point3):

    p1_p2_vector = (point1[0] - point2[0], point1[1] - point2[1])
    p1_p3_vector = (point1[0] - point3[0], point1[1] - point3[1])

    scalar = p1_p2_vector[0] * p1_p3_vector[0] + p1_p2_vector[1] * p1_p3_vector[1]
    mod_p1_p2 = sqrt(p1_p2_vector[0] ** 2 + p1_p2_vector[1] ** 2)
    mod_p1_p3 = sqrt(p1_p3_vector[0] ** 2 + p1_p3_vector[1] ** 2)

    if mod_p1_p2 * mod_p1_p3 == 0:
        cos = 0
    else:
        cos = scalar / (mod_p1_p2 * mod_p1_p3)

    if point1[1] >= point3[1]:
        is_lower: bool = True
    else:
        is_lower: bool = False

    in_deg = degrees(math.acos(cos))

    if is_lower:
        angle = 360 - in_deg
    else:
        angle = in_deg

    return angle

def find_coordinates(centr, radius, angle):

    x = centr[0] + radius * cos(angle)
    y = centr[1] + radius * sin(angle)

    return x, y

print(find_coordinates((0,0), 10, 80))
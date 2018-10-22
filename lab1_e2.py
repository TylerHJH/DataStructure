"""
Input:
x1, y1, x2, y2: We have a line segment defined by its two terminal point A(x1, y1) B(x2, y2).
Output:
Two third equal division points C(x3, y3) D(x4, y4).
"""


def find_third_equal_division_points():
    print("Please enter two terminal points A(x1, y1) B(x2, y2) of the segment.")
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    print("The line segment is between A({}, {}) and B({}, {}).".format(x1, y1, x2, y2))
    x3 = (x1 + x2)/3
    y3 = (y1 + y2)/3
    x4 = 2*(x1 + x2)/3
    y4 = 2*(y1 + y2)/3
    print("C({}, {}) and D({}, {}) divide the segment equally in three parts".format(x3, y3, x4, y4))
    return x3, y3, x4, y4


find_third_equal_division_points()
"""
Input:
a, b: line1 represented as y1 = a*x1 + b
x, y: point A(x,y), which is on the line above
Output:
the line and c, d or none: line2 represented as y2 = c*x2 + d, which point A is on the line,
                      and line2 is perpendicular to line1 or line2 represented as y2 = y.
"""


# Here is a function to find a vertical of a line on a certain point.
def find_vertical():
    print("Please input the parameter of line y1 = ax1 + b.")
    a = int(input("a = "))
    b = int(input("b = "))  # Input parameter a and b of line y1 = ax1 + b.
    while True:  # Enter the point on the line.
        print("Enter the point(x, y) on line1.")
        x = int(input("x = "))
        y = int(input("y = "))
        if y == a*x + b:  # Judge if the input point makes sense.
            print("Set up.")
            break
        else:
            print("The point is not on the line1.")
    # To use mathematical way to find the vertical we should know whether parameter a is zero. Then give the vertical.
    if a != 0:
        c = -1/a
        d = y + x/a
        print("The vertical is y2 = {}x2 + {}".format(c, d) + ", which c is {} and d is {}".format(c, d))
        return c, d
    else:
        print("The vertical is x = {}".format(x))


#  We can run the function.
find_vertical()

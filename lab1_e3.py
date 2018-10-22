"""
Input:
First we have a empty list Hailstone.
n: Get a number n and put it into the list, then judge whether is even or odd.
       If it's even, put n/2 into the list Hailstone, else put 3n+1 into the list.
       Then continue to judge whether the calculated number n/2 or 3n+1 is odd or even and do the same operation as
       before.
Output:
length: When the number becomes 1 finally, put 1 into the list and get the length of the list.
"""


Hailstone = []
n = int(input("Enter a number n of Hailstone(n):"))
n0 = n
Hailstone.append(n)
while n != 1:
    if n % 2 == 0:
        n = n/2

    else:
        n = 3 * n + 1
    Hailstone.append(n)
length = len(Hailstone)
print("The length of Hailstone({}) is {}".format(n0, length))

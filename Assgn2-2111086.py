r1 = int(input("input x cordinate of upper right corner of first rectangle: "))
t1 = int(input("input y cordinate of upper right corner of first rectangle: "))
l1 = int(input("input x cordinate of lower left corner of first rectangle: "))
b1 = int(input("input y cordinate of lower left corner of first rectangle: "))

r2 = int(input("input x cordinate of upper right corner of second rectangle: "))
t2 = int(input("input y cordinate of upper right corner of second rectangle: "))
l2 = int(input("input x cordinate of lower left corner of second rectangle: "))
b2 = int(input("input y cordinate of lower left corner of second rectangle: "))

if r1 > l2 and l1 < r2:
    if t1 > b2 and b1 < t2:
        print("The rectangles overlap.")
    elif t1 < b2 and b1 > t2:
        print("The rectangles overlap.")
    else:
        print("The rectangles don’t overlap.")
elif r1 < l2 and l1 > r2:
    if t1 > b2 and b1 < t2:
        print("The rectangles overlap.")
    elif t1 < b2 and b1 > t2:
        print("The rectangles overlap.")
    else:
        print("The rectangles don’t overlap.")
else:
    print("The rectangles don’t overlap.")

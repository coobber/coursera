l1 = int(input())
r1 = int(input())

l2 = int(input())
r2 = int(input())

l3 = int(input())
r3 = int(input())

d1 = r1 - l1
d2 = r2 - l2
d3 = r3 - l3


delta = r1 - l2

if delta <= 0:
    t = delta * -1
    if d3 <= t:
        print(3)
    elif d2 <= t:
        print(2)
    else:
        print(0)
elif delta > 0:
    # если левый край спички2 лежит внутри спички1
    if r1 >= l2 and r1 < r2:
        t = r2 - l3
        if t < 0:
            print(3)
        else:
            t = r3 - l1
            if t < 0:
                print(3)
            else: print(0)
    # если правый край спички2 лежит внутри спички1
    if l1 >= l2 and l1 <= r2:
        t = r2 - l3
        if t < 0:
            print(3)
        else:
            t = r3 - l1
            if t < 0:
                print(3)
            else:
                print(0)
    # если правый край спички2 слева от левого края спички1
    if r2 - l1 < 0:
        t = -1 * (r2 - l1)
        if t >= d3:
            print(3)
        else:
            t = r3 - l1
            if t < 0:
                print(3)
            else:
                print(0)












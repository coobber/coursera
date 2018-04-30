a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and b == 0:
    print("INF")
elif a == 0 and b != 0:
    print("NO")
elif d == 0 and ((-b) // a) == 0:
    print("NO")
elif (c * ((-b) // a)) + d == 0:
    print("NO")
# elif (-b) % a != 0:
#     print("NO")
# x = (-b) // a
else:
    if ((-b) % a) != 0:
        print("NO")
    else:
        print(((-b) // a))

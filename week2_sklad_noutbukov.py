d1 = int(input())
s1 = int(input())
v1 = int(input())
d2 = int(input())
s2 = int(input())
v2 = int(input())

var1 = d1 // d2
var1 = var1 * (s1 // s2)
var1 = var1 * (v1 // v2)

var2 = d1 // s2
var2 = var2 * (s1 // d2)
var2 = var2 * (v1 // v2)

var3 = d1 // d2
var3 = var3 * (s1 // v2)
var3 = var3 * (v1 // s2)

var4 = s1 // d2
var4 = var4 * (d1 // v2)
var4 = var4 * (v1 // s2)

var5 = s1 // s2
var5 = var5 * (d1 // v2)
var5 = var5 * (v1 // d2)

var6 = d1 // s2
var6 = var6 * (s1 // v2)
var6 = var6 * (v1 // d2)

var7 = v1 // v2
var7 = var7 * (s1 // d2)
var7 = var7 * (d1 // s2)

var8 = v1 // s2
var8 = var8 * (s1 // d2)
var8 = var8 * (d1 // v2)

var9 = v1 // d2
var9 = var9 * (s1 // s2)
var9 = var9 * (d1 // v2)


var0 = (s1 // s2) * (d1 // d2)
if var1 >= var2:
    final = var1
else:
    final = var1

if final >= var3:
    final = final
else:
    final = var3

if final >= var4:
    final = final
else:
    final = var4

if final >= var5:
    final = final
else:
    final = var5

if final >= var6:
    final = final
else:
    final = var6

if final >= var7:
    final = final
else:
    final = var7

if final >= var8:
    final = final
else:
    final = var8

if final >= var9:
    final = final
else:
    final = var9

print(final)

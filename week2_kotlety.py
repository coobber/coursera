k = int(input())
m = int(input())
n = int(input())

if n % k == 0:
    time = (n // k) * 2 * m
elif n < k:
    time = 2 * m
elif n % k > k // 2:
    time = (n // k + 1) * 2 * m
else:
    time = (n // k) * 2 * m + m

print(time)

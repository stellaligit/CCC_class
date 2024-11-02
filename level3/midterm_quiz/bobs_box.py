n, a, b = [int(i) for i in input().split()]
x = n // 2
if n % 2 == 0:
    print(a * x + b * x)
else:
    print(a * (x + 1) + b * x)
n = int(input())

x0 = 1000000
x1 = -1000000
y0 = 1000000
y1 = -1000000

for i in range(n):
    x, y = [int(i) for i in input().split()]
    if x < x0:
        x0 = x
    if x > x1:
        x1 = x
    if y < y0:
        y0 = y
    if y > y1:
        y1 = y

print(2 * (x1 - x0 + y1 - y0))

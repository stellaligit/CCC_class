n = int(input())

a = []
for i in range(n):
    t = int(input())
    a.append(t)

smallestsize = 0
for i in range(1, n-1):
    size = (a[i+1] - a[i-1]) / 2
    if i == 1:
        smallestsize = size
    elif size < smallestsize:
        smallestsize = size

print(smallestsize)

import math
n, q = [int(i) for i in input().split()]
playdoughs = [int(i) for i in input().split()]
m = {}
for i in playdoughs:
    m[i] = m.get(i, 0) + 1

for j in range(q):
    a, b = [int(i) for i in input().split()]
    if a == 1:
        x, y = math.ceil(b/2), math.floor(b/2)
        t = m.get(b, 0)
        m[b] = 0
        m[x] = m.get(x, 0) + t
        m[y] = m.get(y, 0) + t
    elif a == 2:
        print(m.get(b, 0))
import math
n, q = [int(i) for i in input().split()]
playdoughs = [int(i) for i in input().split()]
for i in range(q):
    t = [int(i) for i in input().split()]
    a, b = t[0], t[1]
    if a == 1:
        x, y = math.ceil(b/2), math.floor(b/2)
        for j in playdoughs:
            if j == b:
                playdoughs.remove(j)
                playdoughs.append(x)
                playdoughs.append(y)
        continue
    elif a == 2:
        count = 0
        for j in playdoughs:
            if j == b:
                count += 1
    print(count)
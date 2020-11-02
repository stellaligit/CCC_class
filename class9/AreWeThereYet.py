n = [int(i) for i in input().split()]

d = 0
a = [0]
for i in range(4):
    d += n[i]
    a.append(d)
print(*a)

for i in range(1, 5):
    t = a[i]
    for j in range(5):
        if j < i:
            a[j] = a[j] + t
        else:
            a[j] = a[j] - t
    print(*a)

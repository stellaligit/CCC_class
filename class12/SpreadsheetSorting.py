r, c = [int(i) for i in input().split()]

a = []
for i in range(r):
    t1 = [int(i) for i in input().split()]
    a.append(t1)

n = int(input())
b = []
for i in range(n):
    t2 = int(input())
    b.append(t2)

for i in range(n):
    a = sorted(a, key=lambda x: x[b[i]-1])

for i in a:
    print(*i)

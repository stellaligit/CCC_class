n, y = [int(i) for i in input().split()]
names = []
m = {}
for i in range(n):
    s = input()
    names.append(s)
    m[s] = 0

enjoyment = [int(i) for i in input().split()]
r = {}
for i in range(n):
    r[names[i]] = enjoyment[i]

ans = 0
for i in range(y):
    s = input()
    if m[s] == 0:
        m[s] = 1
        ans += r[s]
    else:
        pass

print(ans)

t = int(input())

a = {}
shopping_list = {}
for i in range(t):
    n = int(input())
    for j in range(n):
        m = int(input())
        for k in range(m):
            s, p, q = input().split()
            info = a.get(s, [])
            info.append((p, q))
            a[s] = info
    k = int(input())
    for i in range(k):
        t, r = input().split()
        info = a[t]

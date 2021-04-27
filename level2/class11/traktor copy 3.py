n, k = [int(i) for i in input().split()]
a = []
for i in range(n):
    x, y = [int(i) for i in input().split()]
    a.append([x, y])

ans = -1

t_map = {}
for i in range(n):
    x, y = a[i]
    v = x
    t = t_map.get(v, 0)
    if t == k - 1:
        if i + 1 < ans or ans == -1:
            ans = i + 1
        break
    else:
        t_map[v] = t + 1

t_map = {}
for i in range(n):
    x, y = a[i]
    v = y
    t = t_map.get(v, 0)
    if t == k - 1:
        if i + 1 < ans or ans == -1:
            ans = i + 1
        break
    else:
        t_map[v] = t + 1

t_map = {}
for i in range(n):
    x, y = a[i]
    v = x + y
    t = t_map.get(v, 0)
    if t == k - 1:
        if i + 1 < ans or ans == -1:
            ans = i + 1
        break
    else:
        t_map[v] = t + 1
    
t_map = {}
for i in range(n):
    x, y = a[i]
    v = x - y
    t = t_map.get(v, 0)
    if t == k - 1:
        if i + 1 < ans or ans == -1:
            ans = i + 1
        break
    else:
        t_map[v] = t + 1

print(ans)
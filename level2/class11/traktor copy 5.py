n, k = [int(i) for i in input().split()]

x_map = {}
y_map = {}
s_map = {}
d_map = {}

ans = -1
for i in range(n):
    x, y = [int(i) for i in input().split()]

    v = x
    t_map = x_map
    t = t_map.get(v, 0)
    if t == k - 1:
        if i + 1 < ans or ans == -1:
            ans = i + 1
        break
    elif t + n - i < k:
        t_map.pop(v, None)
    else:
        t_map[v] = t + 1

    v = y
    t_map = y_map
    t = t_map.get(v, 0)
    if t == k - 1:
        if i + 1 < ans or ans == -1:
            ans = i + 1
        break
    elif t + n - i < k:
        t_map.pop(v, None)
    else:
        t_map[v] = t + 1

    v = x + y
    t_map = s_map
    t = t_map.get(v, 0)
    if t == k - 1:
        if i + 1 < ans or ans == -1:
            ans = i + 1
        flag = True
        break
    elif t + n - i < k:
        t_map.pop(v, None)
    else:
        t_map[v] = t + 1

    v = x - y
    t_map = d_map
    t = t_map.get(v, 0)
    if t == k - 1:
        if i + 1 < ans or ans == -1:
            ans = i + 1
        flag = True
        break
    elif t + n - i < k:
        t_map.pop(v, None)
    else:
        t_map[v] = t + 1

print(ans)
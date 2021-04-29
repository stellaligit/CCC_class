n, k = [int(i) for i in input().split()]

x_map = {}
y_map = {}
s_map = {}
d_map = {}

def testVal(t_map, v, k, r): # k + i - n
    t = t_map.get(v, 0)
    if t == k - 1:
        return True
    # elif t + n - i < k:
    elif t < r: # k + i - n
        t_map.pop(v, None)
    else:
        t_map[v] = t + 1
    return False

ans = -1
for i in range(n):
    x, y = [int(i) for i in input().split()]

    if testVal(x_map, x, k, k + i - n):
        ans = i + 1
        break

    if testVal(y_map, y, k, k + i - n):
        ans = i + 1
        break

    if testVal(s_map, x + y, k, k + i - n):
        ans = i + 1
        break

    if testVal(d_map, x - y, k, k + i - n):
        ans = i + 1
        break

print(ans)
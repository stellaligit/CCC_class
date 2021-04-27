n, k = [int(i) for i in input().split()]
a = []
for i in range(n):
    x, y = [int(i) for i in input().split()]
    a.append([x, y, x + y, x - y])

x_map = {}
y_map = {}
s_map = {}
d_map = {}

def solution(a, x_map, y_map, s_map, d_map, i, k):
    # global a, x_map, y_map, s_map, d_map
    x, y, s, d = a[i]

    t = x_map.get(x, 0)
    if t == k - 1:
        return True
    else:
        x_map[x] = t + 1

    t = y_map.get(y, 0)
    if t == k - 1:
        return True
    else:
        y_map[y] = t + 1

    t = s_map.get(s, 0)
    if t == k - 1:
        return True
    else:
        s_map[s] = t + 1
    
    t = d_map.get(d, 0)
    if t == k - 1:
        return True
    else:
        d_map[d] = t + 1
    
    return False

for i in range(n):
    if solution(a, x_map, y_map, s_map, d_map, i, k) == True:
        print(i + 1)
        break
else:
    print("-1")
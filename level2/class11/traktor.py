n, k = [int(i) for i in input().split()]
a = []
for i in range(n):
    x, y = [int(i) for i in input().split()]
    a.append([x, y, x + y, x - y])

def solution(a, i, k):
    x, y, s, d = a[i]
    count_x = 0
    count_y = 0
    count_s = 0
    count_d = 0
    for j in range(i):
        if a[j][0] == x:
            count_x += 1
        elif a[j][1] == y:
            count_y += 1
        elif a[j][2] == s:
            count_s += 1
        elif a[j][3] == d:
            count_d += 1
    if count_x >= k or count_y >= k or count_s >= k or count_d >= k:
        return True
    else:
        return False

for i in range(k - 1, n):
    if solution(a, i, k) == True:
        print(i + 1)
else:
    print(-1)
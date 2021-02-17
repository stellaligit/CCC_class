n = int(input())

a = []
for i in range(n):
    t = [int(x) for x in input().split()]
    a.append(t)

b = [[0] * n for i in range(n)]


def need_to_rotate(a):
    return a[0][0] > a[0][1] or a[0][0] > a[1][0]


while need_to_rotate(a):
    # b[j][n-1-i] = a[i][j]
    for i in range(n):
        for j in range(n):
            b[j][n-1-i] = a[i][j]
    a, b = b, a

for x in a:
    print(*x)

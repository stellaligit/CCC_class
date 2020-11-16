# method 1
for i in range(5):
    m = int(input())
    a = []
    for j in range(m):
        t = int(input())
        a.append(t)

    for j in range(1, m + 2):
        if j not in a:
            print(j)
            break

# method 2
for i in range(5):
    m = int(input())
    f = [False] * (m + 1)
    for j in range(m):
        t = int(input())
        f[t - 1] = True

    for j in range(m + 1):
        if not f[j]:
            print(j + 1)
            break

t = int(input())

for i in range(t):
    n = int(input())
    a = []
    for j in range(n):
        a.append(int(input()))

    expect = 1
    top = n - 1
    branch = n

    while expect <= n:
        if top >= 0 and a[top] == expect:
            a[top] = 0
            expect = expect + 1
            top = top - 1
        elif branch < n and a[branch] == expect:
            a[branch] = 0
            expect = expect + 1
            while branch < n and a[branch] == 0:
                branch = branch + 1
        else:
            if branch < n and a[top] > a[branch]:
                break
            branch = top
            top = top - 1

    if expect == n + 1:
        print("Y")
    else:
        print("N")

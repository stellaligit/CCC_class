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
        if top < 0:
            expect = n + 1
            break
        elif a[top] == expect:
            a[top] = 0
            top = top - 1
            expect = expect + 1
        elif branch == n or a[top] < a[branch]:
            branch = top
            top = top - 1
        elif a[branch] == expect:
            a[branch] = 0
            while branch < n and a[branch] == 0:
                branch = branch + 1
            expect = expect + 1
        else:
            break
    
    if expect == n + 1:
        print("Y")
    else:
        print("N")
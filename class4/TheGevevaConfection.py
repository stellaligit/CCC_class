t = int(input())

for i in range(t):
    n = int(input())
    a = []
    for j in range(n):
        k = int(input())
        a.append(k)

    expect = 1
    lake = []
    branch = []

    success = True

    while expect <= n:
        if expect in branch:
            if expect == branch[len(branch)-1]:
                lake.append(expect)
                del branch[len(branch)-1]
                expect = expect + 1
                continue
            else:
                success = False
                print("N")
                break
        else:
            if expect == a[len(a)-1]:
                lake.append(expect)
                del a[len(a)-1]
                expect = expect + 1
                continue
            else:
                branch.append(a[len(a)-1])
                del a[len(a)-1]
                continue
    
    if success:
        print("Y")
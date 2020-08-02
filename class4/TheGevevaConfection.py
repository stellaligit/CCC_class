n = int(input())

for i in range(n):
    t = int(input())
    a = []
    for j in range(t):
        k = int(input())
        a.append(k)

    expect = 1
    lake = []
    branch = []

    succsess = True

    for i in range(len(a)):
        if expect in branch:
            if expect == branch[len(branch)-1]:
                lake.append(expect)
                del branch[len(branch)-1]
                expect = expect + 1
                continue
            else:
                succsess = False
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
    
    if succsess:
        print("Y")
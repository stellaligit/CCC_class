n = int(input())

while True:
    n = n + 1
    a = list(str(n))
    t = []
    flag = False

    for i in a:
        if i in t:
            flag = True
            break
        else:
            t.append(i)
    
    if not flag:
        print(n)
        break   
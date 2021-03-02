import math

n = int(input())

for i in range(n):
    sum = []
    difference = []
    
    t = int(input())
    a = int(math.sqrt(t)) + 1
    for j in range(1, a):
        if t % j == 0:
            sum.append(j + t//j)
            difference.append(abs(j - t//j))
    flag = False
    for j in sum:
        if j in difference:
            flag = True
            print(t, "is nasty")
            break
    if not flag:
        print(t, "is not nasty")
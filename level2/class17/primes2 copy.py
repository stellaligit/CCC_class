import math
n, m = [int(i) for i in input().split()]

for i in range(n, m + 1):
    flag = True
    if i < 2:
        flag = False
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        print(i)
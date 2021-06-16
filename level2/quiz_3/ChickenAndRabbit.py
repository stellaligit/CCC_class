x, y = [int(i) for i in input().split()]

flag = True
if x * 4 < y:
    print("No")
    flag = False

dif = x * 4 - y
if dif % 2 == 0 and (x - dif // 2) >= 0 and flag == True:
    print("Yes")
elif flag == True:
    print("No")
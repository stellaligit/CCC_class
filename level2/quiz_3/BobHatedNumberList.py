x, n = [int(i) for i in input().split()]
hated_list = [int(i) for i in input().split()]

if x not in hated_list:
    print(x)
else:
    for i in range(1, x + 1):
        if x - i not in hated_list:
            print(x - i)
            break
        elif x + i not in hated_list:
            print(x + i)
            break
x, y, z = [int(i) for i in input().split()]

flag = False
for i in range(y):
    if (x * i) % y == z:
        print("YES")
        flag = True
        break

if not flag:
    print("NO")

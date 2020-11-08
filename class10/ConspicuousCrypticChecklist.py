n, m = [int(i) for i in input().split()]

backpack = []
for i in range(n):
    t = input()
    backpack.append(t)


ans = 0
for i in range(m):
    flag = True
    number = int(input())
    for j in range(number):
        stuff = input()
        if flag and stuff not in backpack:
            flag = False

    if flag:
        ans += 1

print(ans)

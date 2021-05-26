n = int(input())
emeralds = [int(i) for i in input().split()]

ans, sum = 0, 0
for i in emeralds:
    if i % 2 == 0:
        sum += i
    else:
        if sum > ans:
            ans = sum
        sum = 0

if sum > ans:
    ans = sum

print(ans)
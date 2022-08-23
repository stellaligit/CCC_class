n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

ans = 0

for i in range(len(a)):
    if a[i] > b[i]:
        ans += a[i] - b[i]

print(ans)
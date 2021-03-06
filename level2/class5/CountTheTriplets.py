n = int(input())
a = [int(i) for i in input().split()]
a.sort()

count = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        b = a[i] + a[j]
        if b in a:
            count += 1

if count == 0:
    print(-1)
else:
    print(count)
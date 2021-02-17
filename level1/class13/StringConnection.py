n, l = [int(i) for i in input().split()]

a = []
for i in range(n):
    a.append(input())

a.sort(reverse=True)

print(*a, sep='')

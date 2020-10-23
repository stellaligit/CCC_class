n = int(input())

a = []
for i in range(n):
    t = input()
    a.append(t)

a.sort(reverse=True)
print(*a, sep="")

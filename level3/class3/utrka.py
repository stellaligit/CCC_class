n = int(input())
names = []
for i in range(n):
    names.append(input())

for i in range(n-1):
    names.remove(input())

print(*names)
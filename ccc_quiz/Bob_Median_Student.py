# not for contest, just to check
n = int(input())

person = {}
a = []

for i in range(n):
    name, number = input().split()
    number = int(number)
    if number in person:
        person[number].append(name)
    else:
        person[number] = [name]
    a.append(number)
a.sort()

x = n // 2
b = a[x]
count = 0
for i in range(x - 1, -1, -1):
    if a[i] == b:
        count = count + 1
    else:
        break

person[b].sort()
print(person[b][count])

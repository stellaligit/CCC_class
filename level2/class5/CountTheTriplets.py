n = int(input())
a = [int(i) for i in input().split()]
a.sort()

list_1 = []
list_2 = []
for i in a:
    if i not in list_1:
        list_1.append(i)
    elif i not in list_2:
        list_2.append(i)
a = list_1

count = 0
for i in range(len(list_2)):
    if 2 * list_2[i] in a:
        count += 1

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        b = a[i] + a[j]
        if b in a:
            count += 1

if count == 0:
    print(-1)
else:
    print(count)
n = int(input())
a = [int(i) for i in input().split()]
a.sort()

list_1 = []
list_2 = []
previous = a[0] - 1
for i in a:
    if i != previous:
        list_1.append(i)
        previous = i
    elif i not in list_2:
        list_2.append(i)
a = list_1
n = len(a)

count = 0
for i in range(len(list_2)):
    if 2 * list_2[i] in a:
        count += 1

for i in range(n):
    for j in range(i + 1, n):
        b = a[i] + a[j]
        for k in range(j + 1, n):
            if a[k] == b:
                count += 1
            elif a[k] > b:
                break

if count == 0:
    print(-1)
else:
    print(count)
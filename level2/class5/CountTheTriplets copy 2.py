n = int(input())
a = [int(i) for i in input().split()]
# a.sort()

set_1 = set()
set_2 = set()
list_1 = []

for i in a:
    if i not in set_1:
        set_1.add(i)
        list_1.append(i)
    else:
        set_2.add(i)
a = list_1
n = len(a)

count = 0
for i in set_2:
    if 2 * i in set_1:
        count += 1

for i in range(n):
    j = i + 1
    while j < n:
        b = a[i] + a[j]
        if b in a:
            count += 1
        j = j + 1

if count == 0:
    print(-1)
else:
    print(count)
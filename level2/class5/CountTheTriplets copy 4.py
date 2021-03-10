n = int(input())
a = [int(i) for i in input().split()]
a.sort()

list_1 = []
set_2 = set()
previous = 0
for i in a:
    if i != previous:
        list_1.append(i)
        previous = i
    else:
        set_2.add(i)
a = list_1
n = len(a)

count = 0
for i in set_2:
    if 2 * i in a:
        count += 1

for i in range(n - 2):
    j = i + 1
    k = j + 1
    while True:
        t = a[i] + a[j]
        while k < n and a[k] < t:
            k += 1
        if k == n:
            # next i
            break
        if a[k] == t:
            # next j, k
            count += 1
            j += 1
            k += 1
        else:
            # next j
            j += 1

if count == 0:
    print(-1)
else:
    print(count)
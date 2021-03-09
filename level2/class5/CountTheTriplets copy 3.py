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
    for j in range(i + 1, n - 1):
        b = a[i] + a[j]
        has_larger = False
        for k in range(j + 1, n):
            if a[k] == b:
                count += 1
                break
            elif a[k] > b:
                has_larger = True
                break
        if not has_larger:
            break

if count == 0:
    print(-1)
else:
    print(count)
coins = input()
a = []
for i in coins:
    a.append(int(i))

count = 0
for i in range(len(a) - 1):
    if a[i] == 2 and a[i + 1] != 5:
        count += 1

if a[-1] == 2:
    count += 1

print(count)
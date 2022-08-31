n = int(input())
names = {}
for i in range(n * 2 - 1):
    k = input()
    v = names.get(k, 0)
    names[k] = v + 1

for k in names:
    if names[k] % 2 == 1:
        print(k)
        break
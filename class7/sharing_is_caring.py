n = [int(i) for i in input().split()]

m = {}
for i in range(n[1]):
    t = [int(i) for i in input().split()]
    s = input()
    if t[1] not in m:
        m[t[1]] = [s]
    else:
        m[t[1]].append(s)

p = int(input())
if p not in m:
    print()
else:
    for i in m[p]:
        print(i)
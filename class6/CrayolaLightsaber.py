n = int(input())
t = input()
a = list(t.split())

m = {}

for i in a:
    if i not in m:
        m[i] = 1
    else:
        m[i] = m[i] + 1

b = list(m.values())

preIdx = -1
ans = 0

while True:
    max = 0
    idx = -1
    for i in range(len(b)):
        if b[i] > max and i != preIdx:
            max = b[i]
            idx = i
    if max == 0:
        break

    ans = ans + 1
    b[idx] = b[idx] - 1
    preIdx = idx

print(ans)
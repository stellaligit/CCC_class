n = int(input())
t = [int(i) for i in input().split()]

m = {}
for i in t:
    if i not in m:
        m[i] = 1
    else:
        m[i] = m[i] + 1

max_mode = 0
ans = []

for i in m:
    if m[i] > max_mode:
        max_mode = m[i]

for i in m:
    if m[i] == max_mode:
        ans.append(i)

ans.sort()
for i in range(len(ans) - 1):
    print(ans[i], end = " ")

print(ans[-1])
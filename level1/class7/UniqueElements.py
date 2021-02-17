n = int(input())
m = {}

for i in range(n):
    t = int(input())
    if t not in m:
        m[t] = 1

print(len(m))

# maps are faster than lists when you are searching.
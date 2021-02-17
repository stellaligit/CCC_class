h, w = [int(i) for i in input().split()]

a = []
for i in range(h):
    t = input()
    a.append(t)

for i in range(w + 2):
    print("#", end = "")

print()
for i in range(h):
    print("#", end = "")
    print(a[i], end = "")
    print("#")

for i in range(w + 2):
    print("#", end = "")
n = int(input())
a = []

for i in range(n):
    t = int(input())
    if t != 0:
        a.append(t)
    else:
        del a[len(a)-1]

b = 0

for j in range(len(a)):
    b = b + a[j]

print(b)
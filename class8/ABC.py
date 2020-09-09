values = [int(i) for i in input().split()]
a, b, c = sorted(values)

m = {}
m["A"] = a
m["B"] = b
m["C"] = c

n = input()
for i in range(2):
    print(m[n[i]], end=" ")

print(m[n[2]])

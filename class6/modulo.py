a = []

for i in range(10):
    n = int(input())
    a.append(n % 42)

b = []

for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])

print(len(b))

# or another way:

a = []

for i in range(10):
    n = int(input())
    a.append(n % 42)

print(len(set(a)))

# or another way:

a = [0] *42

for i in range(10):
  n = int(input())
  a[n % 42] = 1

print(sum(a))
import math

n = int(input())
a = [int(i) for i in input().split()]
a.append(0)
b1 = [abs(a[0])]
for i in range(1, len(a)):
    minus1 = abs(a[i] - a[i - 1])
    b1.append(minus1)

b2 = [0]
b2.append(abs(a[1]))
for i in range(2, len(a)):
    minus2 = abs(a[i] - a[i - 2])
    b2.append(minus2)

sum = 0
for i in range(len(b1)):
    sum += b1[i]

for i in range(len(a) - 1):
    print(sum - b1[i] - b1[i + 1] + b2[i + 1])
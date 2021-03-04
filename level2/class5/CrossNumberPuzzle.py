import math

ans_1 = []
for i in range(1000, 10000):
    count = 1
    root = int(math.sqrt(i))
    for j in range(2, root + 1):
        if i % j == 0:
            count += j + i // j
    if i == count:
        ans_1.append(i)

print(*ans_1)

ans_2 = []
for i in range(100, 1000):
    a = i % 10
    b = (i // 10) % 10
    c = (i // 100)
    if i == a ** 3 + b ** 3 + c ** 3:
        ans_2.append(i)

print(*ans_2)
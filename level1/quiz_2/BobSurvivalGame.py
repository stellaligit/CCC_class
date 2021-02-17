n, t, m = [int(i) for i in input().split()]

if m < t:
    print(n)
else:
    w = {}

    for i in range(m):
        x = int(input())
        w[x] = w.get(x, 0) + 1

    count = 0
    for i in w:
        points = t - m + w[i]
        if points > 0:
            count += 1

    print(count)

# scores = []
# for i in range(n):
#     scores.append(t)

# for i in range(m):
#     x = int(input())

#     for j in range(n):
#         scores[j] -= 1
#     scores[x-1] += 1

# count = 0
# for i in scores:
#     if i > 0:
#         count += 1
# print(count)

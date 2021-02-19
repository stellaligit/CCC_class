n = int(input())
max_bid = 0
m = []
values = []

for i in range(n):
    a = input()
    b = int(input())
    m.append([b, a])
    values.append(b)

biggest = 0
for i in values:
    if i > biggest:
        biggest = i

for i in m:
    if i[0] == biggest:
        print(i[1])
        break
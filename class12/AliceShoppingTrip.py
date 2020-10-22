remain, n = [int(i) for i in input().split()]

a = []
for i in range(n):
    w = int(input())
    a.append(w)
a = sorted(a, key=lambda x: abs(x))

c_position = 0
count = 0

for i in range(n):
    # position
    o_position = c_position
    c_position = a.pop(0)
    # remain
    remain -= abs(o_position - c_position)
    # count
    if remain < 0:
        print(count)
        break
    else:
        count += 1

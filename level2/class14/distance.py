n = int(input())

curr = 1
direction = 1
for step in range(n-1, -1, -1):
    print(curr)
    curr += step * direction
    direction = 0 - direction
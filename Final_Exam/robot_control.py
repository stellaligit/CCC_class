n, m = [int(i) for i in input().split()]
p = sorted([int(i) for i in input().split()])

if n >= m:
    print(0)
else:
    dis = []
    for i in range(len(p) - 1):
        dis.append(p[i + 1] - p[i])
    
    dis.sort()
    total = 0
    for j in range(m - n):
        total += dis[j]
    print(total)
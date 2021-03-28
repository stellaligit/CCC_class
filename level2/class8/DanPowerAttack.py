import math
n, d, k = [int(i) for i in input().split()]
monsters = [int(i) for i in input().split()]

if k != 0:
    monsters.sort()
    monsters = monsters[:-k]

ans = 0
for i in monsters:
    ans += math.ceil(i/d)

print(ans)

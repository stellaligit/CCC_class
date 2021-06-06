import sys
import math
input = sys.stdin.readline
n, m = map(int, input().split())
limit = int(math.sqrt(m))
f, prime = [False]*(limit+1), []
for i in range(2, limit+1):
    if not f[i]:
        prime.append(i)
        for j in range(i*i, limit+1, i):
            f[j] = True
i, tmp, prime2 = max(limit+1, n), [False]*(limit+1), []
while i <= m:
    for p in prime:
        for q in range((p - i%p)%p, len(tmp), p):
            tmp[q] = True
    for x in range(len(tmp)):
        if not tmp[x]:
            prime2.append(x+i)
    i += len(tmp)
    tmp = [False]*(limit+1)
if n <= limit:
    for x in prime:
        if n <= x <= m:
            print(x)
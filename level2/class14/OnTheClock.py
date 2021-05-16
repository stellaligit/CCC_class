import sys
import math
input = sys.stdin.readline
n, m = map(int, input().split())
print(n + m - math.gcd(n, m))
for i in range(1, n + 1):
    lo = (i - 1) * m // n + 1
    hi = (i * m + n - 1) // n
    for j in range(lo, hi + 1):
        print(i, j)
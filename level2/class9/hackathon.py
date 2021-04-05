import sys
input = sys.stdin.readline
n, k = map(int, input().split())
for _ in range(k):
    s, t, r = map(int, input().split())
    time, count = 0, 0
    while n > count + s * t:
        time, count = time + t + r, count + s * t
    time += (n - count + s - 1) // s
    print(time)
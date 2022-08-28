n, m = [int(i) for i in input().split()]

if n > m:
    print(n - m)
else:
    print(m % n + 1)
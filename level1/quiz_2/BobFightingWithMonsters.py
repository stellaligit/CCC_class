n, k = [int(i) for i in input().split()]

if n % k < k - n % k:
    print(n % k)
else:
    print(k - n % k)

import math
n, m = [int(i) for i in input().split()]

a = [2]
def isPrime(x):
    if x == 1:
        return False
    for i in a:
        if x % i == 0 and x != i:
            return False
    a.append(x)
    return True

for i in range(3, int(math.sqrt(m + 1)) + 1, 2):
    isPrime(i)

for i in range(n, m + 1):
    if isPrime(i):
        print(i)
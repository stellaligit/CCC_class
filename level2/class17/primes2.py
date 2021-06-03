import math
n, m = [int(i) for i in input().split()]

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(n, m + 1):
    if isPrime(i):
        print(i)
import math
n, m = [int(i) for i in input().split()]

def isPrime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

for i in range(n, m + 1):
    if isPrime(i):
        print(i)
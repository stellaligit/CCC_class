import sys
import math
input = sys.stdin.readline

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(int(input())):
    n = int(input()) * 2
    for j in range(2, n + 1):
        if isPrime(j) and isPrime(n - j):
            print(j, n - j)
            break
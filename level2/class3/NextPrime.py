import math
n = int(input())

if n <= 2:
    print(2)
else:
    def isPrime(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        else:
            return True

    while True:
        if isPrime(n):
            print(n)
            break
        n += 1
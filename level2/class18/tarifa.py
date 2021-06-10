x = int(input())
n = int(input())
sum = 0

for i in range(n):
    p = int(input())
    sum += p

print(x * n - sum + x)
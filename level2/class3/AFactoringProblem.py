n = int(input())

ans = 0
for i in range(2, n//2 + 1):
    count = 0   
    while n % i == 0:
        n = n//i
        count += 1
    ans += i * count
    if n == 1:
        break

print(ans)

n = int(input())
copy = n

ans = 0
count = 0   
while n % 2 == 0:
    n = n//2
    count += 1
ans += 2 * count

for i in range(3, n//2 + 1, 2):
    count = 0
    while n % i == 0:
        n = n//i
        count += 1
    ans += i * count
    if n == 1:
        break

if ans == 0:
    ans = copy
print(ans)

# Mark: 2/3

n = int(input())
s1 = [int(i) for i in input().split()]
ans = []
sum1 = sum(s1)

for i in range(n):
    s2 = s1[i:n] + s1[0:i]
    dif = sum1
    previous_sum = 0
    for j in range(1, n):
        sum2 = previous_sum + s2[j - 1]
        previous_sum = sum2
        sum3 = sum1 - sum2
        dif2 = abs(sum3 - sum2)
        if dif > dif2:
            dif = dif2
    ans.append(dif)

print(*ans)
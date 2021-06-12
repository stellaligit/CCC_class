# Mark: 1/3

n = int(input())
s1 = [int(i) for i in input().split()]
ans = []
sum1 = sum(s1)

for i in range(n):
    s2 = s1[i:n] + s1[0:i]
    dif = sum1
    for j in range(1, n):
        sum2 = sum(s2[0:j])
        sum3 = sum(s2[j:n])
        dif2 = abs(sum3 - sum2)
        if dif > dif2:
            dif = dif2
    ans.append(dif)

print(*ans)
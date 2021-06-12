n = int(input())
s1 = [int(i) for i in input().split()]
ans = []

for i in range(n):
    s2 = s1
    dif = 0
    if i == 0:
        for j in range(s2):
            sum = 0
            for k in range(s2[j + 1:-1]):
                sum += k
        if dif > abs(sum - s2[0]):
            dif = abs(sum - s2[0])
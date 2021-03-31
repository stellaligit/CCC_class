for i in range(5):
    a = input().split()
    ans = []
    for j in a:
        j = [int(i) for i in j]
        j.reverse()
        j1 = j[::2]
        sum1 = 0
        for k in j1:
            k = k * 2
            if k >= 10:
                b = k % 10 + 1
                sum1 += b
            else:
                sum1 += k
        j2 = j[1::2]
        sum2 = 0
        for k in j2:
            sum2 += k
        sum3 = sum1 + sum2
        if sum3 % 10 == 0:
            ans.append(0)
        else:
            check_digit = 10 - (sum3 % 10)
            ans.append(check_digit)
    print(*ans, sep="")

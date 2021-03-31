for i in range(5):
    a = input().split()
    ans = []
    for j in a:
        j = [int(i) for i in j]
        j.reverse()
        j1 = j[::2]
        sum = 0
        for k in j1:
            k = k * 2
            if k >= 10:
                b = k % 10 + 1
                sum += b
            else:
                sum += k
        j2 = j[1::2]
        for k in j2:
            sum += k
        if sum % 10 == 0:
            ans.append(0)
        else:
            check_digit = 10 - (sum % 10)
            ans.append(check_digit)
    print(*ans, sep="")

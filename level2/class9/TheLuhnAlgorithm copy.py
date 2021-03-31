for i in range(5):
    a = [int(j) for j in input().split()]
    ans = []
    for j in a:
        sum = 0
        flag = True
        while j > 0:
            k = j % 10
            if flag:
                k = k * 2
            if k >= 10:
                sum += k % 10 + 1
            else:
                sum += k
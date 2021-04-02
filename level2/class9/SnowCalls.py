n = int(input())
for i in range(n):
    phone_num = input()
    ans = []
    count = 0
    for j in phone_num:
        if j == "-":
            continue
        if count == 3 or count == 6:
            ans.append("-")
        if j in "1234567890":
            ans.append(int(j))
            count += 1
        elif j in "ABC":
            ans.append(2)
            count += 1
        elif j in "DEF":
            ans.append(3)
            count += 1
        elif j in "GHI":
            ans.append(4)
            count += 1
        elif j in "JKL":
            ans.append(5)
            count += 1
        elif j in "MNO":
            ans.append(6)
            count += 1
        elif j in "PQRS":
            ans.append(7)
            count += 1
        elif j in "TUV":
            ans.append(8)
            count += 1
        elif j in "WXYZ":
            ans.append(9)
            count += 1
        if count >= 10:
            break
    print(*ans, sep="")
s = input()
L_count = 0
M_count = 0
S_count = 0

for i in range(len(s)):
    if s[i] == "L":
        L_count += 1
    elif s[i] == "M":
        M_count += 1
    else:
        S_count += 1

organized = str(L_count * "L") + str(M_count * "M") + str(S_count * "S")

if s == organized:
    print("0")
else:
    bad = []
    good = []
    for i in range(len(s)):
        if s[i] != organized[i]:
            bad.append(s[i])
            good.append(organized[i])
    
    bad.sort()
    count = 0
    count_2 = 0
    number = len(bad)
    while number > 0:
        if bad[count_2] == good[count_2]:
            count += 1
            count_2 += 1
            number -= 1
    
    print(count - 1)
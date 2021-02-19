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
    
    count = 0
    pos = 0
    replace = 0
    recent = bad[0]
    for i in range(len(bad) - 1):
        for j in range(len(good)):
            if good[i] == recent:
                pos = i
                replace = good[i]
                good[i] = bad[pos]
                bad[pos] = replace
                count += 1
            else:
                
    
    print(count + 1)

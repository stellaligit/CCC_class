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

expect = str(L_count * "L") + str(M_count * "M") + str(S_count * "S")

if expect == s:
    print("0")
else:
    ans = 0
    L_count2 = 0
    M_count2 = 0
    L_count3 = 0
    M_count3 = 0

    for i in range(L_count):
        if s[i] == "L":
            L_count2 += 1
        elif s[i] == "M":
            M_count3 += 1

    for i in range(L_count, L_count + M_count):
        if s[i] == "M":
            M_count2 += 1
        elif s[i] == "L":
            L_count3 += 1

    ans = L_count - L_count2 + M_count - M_count2

    if L_count3 > M_count3:
        ans -= M_count3
        print(ans)
    else:
        ans -= L_count3
        print(ans)

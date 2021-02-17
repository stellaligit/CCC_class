s = input().lower()

if s == "darcy_liu":
    print("real")
elif len(s) <= 9:
    print("other user")
elif s[:5] == "darcy" and s[-3:] == "liu":
    flag = True
    for ch in s[5:-3]:
        if ch != "_":
            flag = False
            break

    if flag:
        print("fake")
    else:
        print("other user")
else:
    print("other user")

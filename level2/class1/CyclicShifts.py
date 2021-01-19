t = input()
s = input()

L1 = len(t)
L2 = len(s)

found = False
for i in range(L1 - L2 + 1):
    for j in range(L2):
        if t[i] == s[j]:
            all_same = True
            for k in range(1, L2):
                if s[(j+k) % L2] != t[i+k]:
                    all_same = False
                    break
            if all_same:
                found = True
                break

    if found:
        break

if found:
    print("yes")
else:
    print("no")

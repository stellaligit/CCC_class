s1 = input()
s2 = input()
m1 = {}
m2 = {}

for ch in s1:
    if ch == " ":
        continue
    elif ch not in m1:
        m1[ch] = 1
    else:
        m1[ch] = m1[ch] + 1

for ch in s2:
    if ch == " ":
        continue
    elif ch not in m2:
        m2[ch] = 1
    else:
        m2[ch] = m2[ch] + 1
#############
match = True
if len(s1) != len(s2):
    match = False
else:
    for k in m2: 
        if k == "*":
            continue
        if k not in m1:
            match = False
            break
        elif m2[k] > m1[k]:
            match = False
            break

if match == True:
    print("A")
else:
    print("N")
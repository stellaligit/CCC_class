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

if m1 == m2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
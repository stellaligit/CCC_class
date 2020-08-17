s = input()

upperCount = 0
lowerCount = 0

for i in s:
    if i >= "A" and i <= "Z":
        upperCount = upperCount + 1 
    elif i >= "a" and i <= "z":
        lowerCount = lowerCount + 1

if upperCount == lowerCount:
    print(s)
elif upperCount > lowerCount:
    print(s.upper())
else:
    print(s.lower())
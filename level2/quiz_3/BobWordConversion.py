s1 = [char for char in input()]
s2 = [char for char in input()]

len_s1 = len(s1)
len_s2 = len(s2)

if len_s1 > len_s2:
    s1, s2 = s2, s1
    len_s1, len_s2 = len_s2, len_s1

if abs(len_s1 - len_s2) >= 2:
    print("No")
elif len_s1 == len_s2:
    count = 0
    for i in range(len_s1):
        if s1[i] != s2[i]:
            count += 1
        
        if count > 1:
            break

    if count > 1:
        print("No")
    else:
        print("Yes")
else:
    count = 0
    j = 0
    for i in range(len_s2):
        if s1[j] != s2[i]:
            count += 1
        else:
            j += 1
        
        if count > 1:
            break

    if count > 1:
        print("No")
    else:
        print("Yes")
# this is not for contest marks. I'm doing this to see if I'm right.
s = input()
t = input()

a = []
for ch in s:
    a.append(ch)

b = []
for ch in t:
    b.append(ch)

flag = True
for i in range(len(a)):
    if a[i] != b[i]:
        x = a[i]
        y = b[i]
        for j in range(i):
            if a[j] == x or a[j] == y:
                flag = False
                break
        if not flag:
            break
        for j in range(i, len(a)):
            if a[j] == y:
                a[j] = x
            elif a[j] == x:
                a[j] = y
       
if flag:
    print("Yes")
else:
    print("No")
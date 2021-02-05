a = list(input())
s = list(input())

count = 0
flag = False
while True:
    for i in range(len(a)):
        if a[i] == s[0]:
            s.remove(s[0])
        if len(s) == 0:
            flag = True
            break
    count += 1
    if flag:
        break

print(count)
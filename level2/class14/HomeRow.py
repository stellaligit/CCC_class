s = [i for i in input()]
t = [i for i in input()]

if s == t:
    print("0")
else:
    if len(s) < len(t):
        a = len(s)
    else:
        a = len(t)

    num = 0
    for i in range(a):
        if s[i] != t[i]:
            num = i
            break

    print(len(s) + len(t) - 2 * num)
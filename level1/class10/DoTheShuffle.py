s = ["A", "B", "C", "D", "E"]
while True:
    a = int(input())
    b = int(input())
    for i in range(b):
        if a == 1:
            s = s[1:] + s[0:1]
        elif a == 2:
            s = s[-1:] + s[:4]
        elif a == 3:
            s[0], s[1] = s[1], s[0]

    if a == 4:
        print(*s)
        break

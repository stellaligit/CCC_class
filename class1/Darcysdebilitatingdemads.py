t = int(input())
for i in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    if n<=c:
        a = 0
        b = 0
        c = n
        print ('%s %s %s' % (a, b, c))
    elif n<=b+c:
        a = 0
        b = n - c
        c = c
        print ('%s %s %s' % (a, b, c))
    elif n<=a+b+c:
        a = n - b - c
        b = b
        c = c
        print ('%s %s %s' % (a, b, c))
    else:
        print("-1")

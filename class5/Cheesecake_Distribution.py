n = int(input())

a = input().split()
a = [int(i) for i in a]

t = sum(a)

if t % n != 0:
    print("Impossible")
else:
    m = t // n
    s = 0
    for j in a:
        if j > m:
            s = s + j - m        

    print(s)
c = int(input())

max_c = 0
for f in range(c):
    s = input().split()
    w = int(s[0])
    l = int(s[1])
    t = w * l
    if t > max_c:
        max_c = t

n = int(input())

max_n = 0
for f in range(n):
    s = input().split()
    w = int(s[0])
    l = int(s[1])
    t = w * l
    if t > max_n:
        max_n = t

if max_n > max_c:
    print("Natalie")
elif max_n < max_c:
    print("Casper")
else:
    print("Tie")
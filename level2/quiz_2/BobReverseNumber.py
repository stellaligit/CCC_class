a, b = [int(i) for i in input().split()]
a_reverse = 0
b_reverse = 0

while a > 0:
    t = a % 10
    a_reverse = a_reverse * 10 + t
    a = a // 10

while b > 0:
    t = b % 10
    b_reverse = b_reverse * 10 + t
    b = b // 10

if a_reverse < b_reverse:
    print(a_reverse)
else:
    print(b_reverse)

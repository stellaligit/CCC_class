n = int(input())
a = [int(i) for i in input().split()]

even = 0
odd = 0
for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

if even > odd:
    num = odd * 2
else:
    num = even * 2

if even == odd:
    print(num)
elif even > odd:
    print(num + 1)
else:
    x = odd - even
    if x % 3 == 0:
        print(x * 2//3 + num)
    elif x % 3 == 1:
        print((x-1) * 2//3  + num - 1)
    elif x % 3 == 2:
        print((x+1) * 2//3 + num - 1)

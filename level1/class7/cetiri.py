s = input().split()
s = [int(i) for i in s]
s.sort()

result_1 = s[1] - s[0]
result_2 = s[2] - s[1]

if result_1 == result_2:
    print(s[2] + result_1)
elif result_1 > result_2:
    print(s[0] + result_2)
else:
    print(s[1] + result_1)
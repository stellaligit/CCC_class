a, b = input().split()

ans_1 = 0
for ch in a:
    ans_1 = ans_1 + int(ch)

ans_2 = 0
for ch in b:
    ans_2 = ans_2 + int(ch)
    
print(ans_1 * ans_2)
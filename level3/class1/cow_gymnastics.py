k, n = [int(i) for i in input().split()]

a = []
for i in range(k):
    b = [int(x) for x in input().split()]
    a.append(b)

count = 0
for firstNum in range(1, n):
    for secondNum in range(firstNum + 1, n + 1):
        danger = False
        for round in range(k):
            for pos in range(n):
                if a[round][pos] == firstNum:
                    pos1 = pos
                elif a[round][pos] == secondNum:
                    pos2 = pos
            if round == 0:
                if pos1 > pos2:
                    ascend = True
                else:
                    ascend = False
            else:
                if (pos1 < pos2 and ascend) or (pos1 > pos2 and not ascend):
                    danger = True
                    break
        if not danger:
            count += 1

print(count)

'''
3 4
4 1 2 3
4 1 3 2
4 2 1 3
'''
n = int(input())

a = [int(i) for i in input().split()]

search_num = 1
pos_1 = 0
pos_2 = len(a) - 1
6
dif = 0

for i in range(len(a)):
    if a[i] == search_num:
        pos_1 = i

        for j in range(pos_2, -1, -1):
            if a[j] == search_num:
                pos_2 = j
                break
    
        if pos_1 < pos_2:
            dif += 1
            search_num += 1

print(dif)
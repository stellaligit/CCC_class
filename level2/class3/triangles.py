n = int(input())

a = []
for i in range(n):
    t = [int(i) for i in input().split()]
    a.append(t)

max_area = 0
for i in range(len(a)):
    max_x = 0
    max_y = 0
    for j in a:
        if j[0] == a[i][0]:
            p = abs(j[1] - a[i][1])
            if p > max_y:
                max_y = p
        if j[1] == a[i][1]:
            q = abs(j[0] - a[i][0])
            if q > max_x:
                max_x = q
    
    if max_x * max_y > max_area:
        max_area = max_x * max_y

print(max_area)
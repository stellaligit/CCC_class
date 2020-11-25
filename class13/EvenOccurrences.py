s = input()

a_map = {}
for i in s:
    a_map[i] = a_map.get(i, 0) + 1

flag = True
for key in a_map:
    if a_map[key] % 2 != 0:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")

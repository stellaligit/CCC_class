n = int(input())
users = []
for i in range(n):
    t = int(input())
    users.append(t)

for i in users:
    if i == 2:
        print("2")
    else:
        print(i - 1)
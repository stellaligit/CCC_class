n = int(input())
students = []
for i in range(n):
    a, b = input().split()
    if a == "F":
        students.insert(0, b)
    elif a == "E":
        students.append(b)
    elif a == "R":
        students.remove(b)

for i in students:
    print(i)
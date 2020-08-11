n = int(input())
c = int(input())

a = []

for i in range(c):
    t = int(input())
    a.append(t)

a.sort()
b = 0

number = 0

while n - b >= a[number]:
    b = b + a[number]
    number = number + 1

print(number)
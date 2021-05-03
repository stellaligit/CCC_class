n = int(input())
for i in range(n):
    sides = [int(i) for i in input().split()]
    sides.sort()
    a = sides[0] * sides[0] + sides[1] * sides[1]
    b = sides[2] * sides[2]
    if a == b:
        print("R")
    elif a <= b:
        print("O")
    else:
        print("A")
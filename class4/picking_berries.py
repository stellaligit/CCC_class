s = input()
a = s.split()
w = int(a[0])
h = int(a[1])

leaf = "#"
edible_berry = "o"
poisonous_berry = "*"

b = 0

for i in range(h):
    t = input()
    for ch in t:
        if ch == edible_berry:
            print(" ", end = "")
            b = b + 1
        elif ch == poisonous_berry:
            print(" ", end = "")
        else:
            print(ch, end = "")
        
    print()

for j in range(b):
    print("o", end = "")
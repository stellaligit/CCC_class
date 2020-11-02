t = int(input())
s = int(input())
h = int(input())

for i in range(t):
    for j in range(2):
        print("*", end="")
        for k in range(s):
            print(" ", end="")
    print("*")

for i in range(3 + 2 * s - 1):
    print("*", end="")
print("*")

for i in range(h):
    for j in range(s + 1):
        print(" ", end="")
    print("*")

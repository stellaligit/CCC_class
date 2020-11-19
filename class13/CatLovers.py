n = int(input())

cats = 0
dogs = 0
for i in range(n):
    t = input()
    if t == "cats":
        cats += 1
    else:
        dogs += 1

if cats > dogs:
    print("cats")
elif cats < dogs:
    print("dogs")
else:
    print("equal")

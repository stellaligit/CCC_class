road = ["HOME"]
while True:
    d = input()
    road.append(d)
    p = input()
    if p == "SCHOOL":
        break
    road.append(p)

while True:
    d = road.pop()
    p = road.pop()
    if d == "R":
        direction = "LEFT"
    elif d == "L":
        direction = "RIGHT"
    if p == "HOME":
        print("Turn", direction, "into your HOME.")
        break
    print("Turn", direction, "onto", p, "street.")

c, r = [int(i) for i in input().split()]

position = [0, 0]
while True:
    x, y = [int(i) for i in input().split()]
    if x == 0 and y == 0:
        break

    # determining x
    test = position[0] + x
    if 0 < test <= c:
        position[0] =
    elif test > c:
        position[0] = c
    else:
        position[0] = 0

    # determining y
    test = position[1] + y
    if 0 < test <= r:
        position[1] = test
    elif test > r:
        position[1] = r
    else:
        position[1] = 0

    print(*position)

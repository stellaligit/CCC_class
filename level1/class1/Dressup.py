# get h from input
h = int(input())

# draw the upper side of the tie 
for i in range((h+1)//2):
    # print front *
    for j in range(2*i+1):
        print('*', end='')
    # print space
    for j in range(2*h-4*i-2):
        print(' ', end='')
    # print tail *
    for j in range(2*i+1):
        print('*', end='')
    print()
    

# draw the lower side of the tie 
for i in range((h+1)//2, h):
    k = h - 1 - i
    # print front *
    for j in range(2*k+1):
        print('*', end='')
    # print space
    for j in range(2*h-4*k-2):
        print(' ', end='')
    # print tail *
    for j in range(2*k+1):
        print('*', end='')
    print()


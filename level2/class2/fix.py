n = int(input())

for i in range(n):
    arr = [input() for i in range(3)]
    arr.sort()

    shortest = arr[0]
    medium = arr[1]
    largest = arr[2]

    prefix_free = True
    suffix_free = True

    if (medium[:len(shortest)] == shortest or largest[:len(shortest)] == shortest or
            largest[:len(medium)] == medium):
        prefix_free = False
    elif (medium[-1 * len(shortest):] == shortest or largest[-1 * len(shortest):] == shortest or
            largest[-1 * len(medium):] == medium):
        suffix_free = False

    if prefix_free and suffix_free:
        print("Yes")
    else:
        print("No")

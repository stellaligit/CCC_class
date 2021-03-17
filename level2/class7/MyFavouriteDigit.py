for i in range(5):
    n = [int(i) for i in input()]
    biggest = 0
    for j in n:
        if j > biggest:
            biggest = j
    print(biggest)
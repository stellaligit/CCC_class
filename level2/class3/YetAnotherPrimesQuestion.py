for i in range(5):
    n = int(input())

    count = 0
    for j in range(2, n//2 + 1):
        dividable = False
        while n % j == 0:
            n = n // j
            dividable = True
        
        if dividable:
            count += 1

    if count == 3:
        print("valid")
    else:
        print("not")
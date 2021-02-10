for i in range(5):
    n = int(input())
    
    a = 2
    count = 0
    flag = True

    while True:
        dividable = False
        while n % a == 0:
            n = n // a
            dividable = True
        
        if dividable:
            count += 1
        if count > 3:
            flag = False
            break
        a += 1

    if flag:
        print("valid")
    else:
        print("not")
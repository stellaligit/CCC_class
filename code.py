i = 1
while True:
    n = 37 * i
    copy_n = n
    sum = 0
    product = 1
    while copy_n > 0:
        num = copy_n % 10
        sum += num
        product *= num
        copy_n = copy_n // 10
    if product == 0:
        i += 1
        continue
    elif sum/product == 3/40:
        print(n)
        break
    i += 1

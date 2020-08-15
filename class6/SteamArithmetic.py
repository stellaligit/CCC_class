def arith(arg):
    # step 1: get operator
    item1 = arg.pop(0)

    # step 2: get num_a
    item2 = arg[0]
    if item2[0] in "-0123456789":
        a = int(item2)
        arg.pop(0)
    else:
        a = arith(arg)

    # step 3: get num_b
    item3 = arg[0]
    ans = 0
    if item3[0] in "-0123456789":
        b = int(item3)
        arg.pop(0)
    else:
        b = arith(arg)

    if item1 == "(+":
        ans = a + b
    elif item1 == "(-":
        ans = a - b
    elif item1 == "(*":
        ans = a * b
    elif item1 == "(q":
        ans = a // b
    elif item1 == "(r":
        ans = a % b

    return ans

for i in range(10):
    s = input().replace(")", "")
    arg = s.split()
    result = arith(arg)
    print(result)
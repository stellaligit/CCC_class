for i in range(10):
    s = input()
    s = s.replace("(", "( ")
    s = s.replace(")", " )")
    a = s.split()
    stack = []

    result = 0
    for j in range(len(a)):
        if a[j] in "+-*qr":
            stack.append(a[j])
        elif a[j] in "0123456789":
            stack.append(int(a[j]))
        elif a[j] == ")":
            n = stack[-2]
            m = stack[-1]
            if stack[-3] == "+":
                result = n + m
            if stack[-3] == "-":
                result = n - m
            if stack[-3] == "*":
                result = n * m
            if stack[-3] == "q":
                if n > 0 and m < 0:
                    result = -1 * (n // -m)
                elif n < 0 and m > 0:
                    result = -1 * (-n // m)
                else:
                    result = n // m
            if stack[-3] == "r":
                result = n % m
                if (n > 0 and m < 0) or (n < 0 and m > 0):
                    result *= -1
                    
            
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append(result)

    print(result)

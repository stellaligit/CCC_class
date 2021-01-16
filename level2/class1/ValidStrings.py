n = int(input())
for i in range(n):
    s = input()
    stack = []

    flag = True
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if len(stack) == 0:
                flag = False
            elif stack[-1] == "(":
                stack.pop()

    if flag and len(stack) == 0:
        print("YES")
    else:
        print("NO")

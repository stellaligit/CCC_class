n = int(input())

stack = []
for i in range(n):
    t = int(input())
    stack.append(t)
stack.sort()

if n <= 1:
    print(n)
elif n == 2:
    if stack[0] == stack[1]:
        print("1")
    else:
        print("2")
else:
    count = 2
    sum = stack[0] + stack[1]
    for i in stack:
        if sum <= i:
            count += 1
            sum += i
            if sum > stack[-1]:
                break

    print(count)

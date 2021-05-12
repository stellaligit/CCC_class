n = int(input())
if n % 2 == 0:
    for i in range(1, n // 2 + 1):
        print(i, end = " ")
        print(n - i + 1, end = " ")
else:
    print("1", end = " ")
    for i in range(1, (n - 1) // 2 + 1):
        print(n - i + 1, end = " ")
        print(i + 1, end = " ")
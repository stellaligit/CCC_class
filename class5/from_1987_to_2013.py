n = int(input())

while True:
    n = n + 1
    a = list(str(n))
     
    if len(a) == len(set(a)):
        print(n)
        break
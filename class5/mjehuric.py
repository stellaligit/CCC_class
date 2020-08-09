n = input()
a = [int(i) for i in n.split()]

while a != [1, 2, 3, 4, 5]:
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            t = a[i]
            a[i] = a[i + 1]
            a[i + 1] = t
            for j in range(len(a) - 1):
                print(a[j], end = " ")
            print(a[len(a) - 1])
n = int(input()) - 1
a = [int(i) for i in input().split()]

maxlength = 1
i = 0
while i < n:
    length = 1
    for j in range(i, n):
        if a[j] >= a[j + 1]:
            length += 1
        else:
            break

    if length > maxlength:
        maxlength = length

    i = j + 1

print(maxlength)

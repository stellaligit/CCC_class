n = int(input())
snowmen = [int(i) for i in input().split()]
snowmen.sort()

biggest = 0
difference = 0
for i in range(1, len(snowmen) - 1):
    a = snowmen[i]
    for j in range(i):
        b = snowmen[j]
        difference = a - b
        if a + difference in snowmen[i + 1:]:
            if 3 * a > biggest:
                biggest = 3 * a
                # print(b, a, a + difference, biggest)
            break

print(biggest)
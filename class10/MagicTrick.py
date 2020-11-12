for i in range(5):
    n = int(input())
    list_1 = [int(i) for i in input().split()]
    list_2 = [0] * n

    zero_count = n
    while zero_count > 0:
        found_zero = False
        for j in range(n):
            if list_1[j] == 0:
                found_zero = True

                list_2[j] = zero_count
                zero_count -= 1

                for k in range(j + 1):
                    list_1[k] -= 1
                break
        if not found_zero:
            print("IMPOSSIBLE")
            break

    if found_zero:
        print(*list_2)

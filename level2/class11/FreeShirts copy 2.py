for i in range(10):
    n, m, d = [int(j) for j in input().split()]
    events = [int(j) for j in input().split()]
    events.sort()
    clean_clothes = n
    total_clothes = n
    ans = 0
    for j in range(1, d + 1):
        if clean_clothes == 0:
            ans += 1
            clean_clothes = total_clothes
        clean_clothes -= 1
        while len(events) > 0 and events[0] == j:
            clean_clothes += 1
            total_clothes += 1
            events.pop(0)
    print(ans)
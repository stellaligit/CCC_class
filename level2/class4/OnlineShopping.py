t = int(input())

for i in range(t):
    a = {}
    n = int(input())
    for j in range(n):
        m = int(input())
        for k in range(m):
            s, p, q = input().split()
            info = a.get(s, [])
            info.append((int(p), int(q)))
            a[s] = info
    
    total = 0
    k = int(input())
    for j in range(k):
        t, r = input().split()
        r = int(r)
        info = a[t]
        info.sort(key=lambda x: x[0])
        for storeInventory in info:
            price = int(storeInventory[0])
            quantity = int(storeInventory[1])
            if r > quantity:
                r -= quantity
                total += price * quantity
            else:
                total += r * price
                break
    print(total)
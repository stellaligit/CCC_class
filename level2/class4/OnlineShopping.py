t = int(input())

a = {}
total = 0
for i in range(t):
    n = int(input())
    for j in range(n):
        m = int(input())
        for k in range(m):
            s, p, q = input().split()
            info = a.get(s, [])
            info.append((p, q))
            a[s] = info
    k = int(input())
    for j in range(k):
        t, r = input().split()
        r = int(r)
        info = a[t]
        for storeInventory in info:
            price = int(storeInventory[0])
            quantity = int(storeInventory[1])
            if r > quantity:
                r -= quantity
                total += price * quantity
            else:
                total += r * price

n, t = [int(i) for i in input().split()]

happy = []
cost = []
for i in range(n):
    c, v = [int(i) for i in input().split()]
    cost.append(c)
    happy.append(v)

for i in range(n):
    if cost[i] >= t:
        happy[i] = 0

happy.sort()

print(happy[n-1])
BobBuyingGifts.py

q = int(input())
n = int(input())

t = input()
b1 = t.split()
a1 = []
for s in b1:
    a1.append(int(s))
a1.sort()

t = input()
b2 = t.split()
a2 = []
for s in b2:
    a2.append(int(s))
a2.sort()

ans1 = 0
for i in range(n):
    if a1[i] > a2[i]:
        ans1 = ans1 + a1[i]
    else:
        ans1 = ans1 + a2[i]

a1.sort(reverse = True)
ans2 = 0

for i in range(n):
    if a1[i] > a2[i]:
        ans2 = ans2 + a1[i]
    else:
        ans2 = ans2 + a2[i]
            
if q == 1:
    print(ans1)
else:
    print(ans2)
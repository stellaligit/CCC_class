q = int(input())
n = int(input())

a_arr = []
for i in range(2):
    t = input()
    b = t.split()
    a = [int(s) for s in b]
    a.sort()
    a_arr.append(a)
            
if q != 1:
    a_arr[1].sort(reverse = True)

ans = 0
for i in range(n):
    if a_arr[0][i] > a_arr[1][i]:
        ans = ans + a_arr[0][i]
    else:
        ans = ans + a_arr[1][i]
print(ans)
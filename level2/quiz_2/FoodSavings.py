import sys
input = sys.stdin.readline
n, q = map(int, input().split())
psa = [0]
for x in list(map(int, input().split())):
    psa.append(psa[-1] + x)
for _ in range(q):
    a, b, c, d = map(int, input().split())
    ans1 = min(psa[b] - psa[a-1], 10) + (psa[d] - psa[c-1])/2
    ans2 = (psa[b]-psa[a-1])/2 + min(psa[d] - psa[c-1], 10)
    print("%.1f\n" % max(ans1, ans2))

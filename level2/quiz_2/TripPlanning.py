a, b, c = [int(i) for i in input().split()]
ans = (a/40000 + b/60000 + c/70000) * 60
print(round(ans, 2))
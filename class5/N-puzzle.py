scatter = 0
desire = {}

x = 0
y = 0

for alphabet in "ABCDEFGHIJKLMNO":
    desire[alphabet] = [y, x]
    x = x + 1
    if x == 4:
        y = y + 1
        x = 0

for i in range(4):
    s = input()
    for j in range(4):
        if s[j] != ".":
            y0, x0 = desire[s[j]]
            scatter = scatter + abs(i - y0) + abs(j - x0)

print(scatter)
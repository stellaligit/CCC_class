s = input()
a = s.split(":")
t = int(a[0]) * 60 + int(a[1])

if 0 <= t <= 300:
    x = t + 120
elif 300 < t < 400:
    x = t * 2 - 180
elif t == 400:
    x = 610
elif 420 <= t < 600:
    x = (t + 840) // 2
elif 600 <= t <= 780:
    x = t + 120
elif 780 < t <= 900:
    x = t * 2 - 660
elif 900 < t < 1140:
    x = (t + 23*60) // 2
elif 1140 <= t:
    x = t + 120
    if x >= 1440:
        x -= 1440

# print(f"{x // 60}:{x % 60}")
print("{0:02}:{1:02}".format(x // 60, x % 60))

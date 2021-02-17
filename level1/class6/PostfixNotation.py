n = input()
a = n.split()
b = []

for i in a:
    if i in "+-*/%^":
        x = b.pop()
        y = b.pop()
        if i == "+":
            r = y + x
        elif i == "-":
            r = y - x
        elif i == "*":
            r = y * x
        elif i == "/":
            r = y / x
        elif i == "%":
            r = y % x
        elif i == "^":
            r = y ** x

        b.append(r)
    else:
        b.append(int(i))

r = b.pop()
# print("%.1f" % float(r))
print("{0:.1f}".format(float(r)))
# my solution :)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

nikky = (s // (a + b)) * (a - b)
n1 = s % (a + b)
byron = (s // (c + d)) * (c - d)
b1 = s % (c + d)

if n1 < a:
    nikky += n1
else:
    nikky += 2 * a - n1

if b1 < c:
    byron += b1
else:
    byron += 2 * c - b1

# print(nikky, byron)
if nikky > byron:
    print("Nikky")
elif nikky < byron:
    print("Byron")
else:
    print("Tied")

# daddy's solution :)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())


def distance(x, y, s):
    dis = (s // (x + y)) * (x - y)
    n = s % (x + y)
    if n < x:
        dis += n
    else:
        dis += 2 * x - n
    return dis


nikky = distance(a, b, s)
byron = distance(c, d, s)

# print(nikky, byron)
if nikky > byron:
    print("Nikky")
elif nikky < byron:
    print("Byron")
else:
    print("Tied")

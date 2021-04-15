import math
p, c, v = [int(i) for i in input().split()]
print(math.ceil(p/3) + math.ceil(c/3) + math.ceil(v/3))
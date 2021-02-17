n = int(input())
a = [*input()]
b = [*input()]
c = list(map(lambda x: x[0] == x[1] and x[0] == "C", zip(a, b)))
print(sum(c))

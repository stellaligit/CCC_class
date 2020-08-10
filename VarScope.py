"e.g. num 1":

a = 10
def test(b):
    global a
    a = 15
    b = b + a
    return b

b = 6
print(a)
# result should be 10

print(test(b))
# result should be 21

print(a)
# result should be 15

"e.g. num 2":

a = 100*20
def test(b):
    global a
    a = a + 20
    b = b - a
    return b

b = 50
print(a)
# result should be...

print(test(b))
# result should be...

print(a)
# result should be...
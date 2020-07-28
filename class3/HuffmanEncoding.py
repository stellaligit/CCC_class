'''
# read how many rules will be defined.
k = int(input())

# read in all encoding rules
m = {}
for i in range(k):
    s = input()
    ch = s[0]
    code = s[2:]
    m[code] = ch

    # r = s.split()

    # r = input().split()
    # m[r[0]] = r[1]
# print(m)

# read encoded string
t = input()

# decode t to a string
testKey = ""
for j in range(len(t)):
    testKey = testKey.append(t[j])
'''

############################

n = int(input())

s = input()

letter = ""
code = ""

for i in range(n):
    l, s = input(s).split()
    letter.append(l)
    code.append(s)

a = ""

decodestr = input()

while len(decodestr) > 0:
    for j in range(n):
        if len(code[j]) <= len(decodestr) and decodestr[0:len(code[j])] == code[j]:
            a = a + letter[j]
            string = string[len(code[j]):]
        else:
            continue

print(a, end = "")
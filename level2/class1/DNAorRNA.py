n = int(input())
s = input()

DNA = False
RNA = False
NEITHER = False
for i in s:
    if i not in "ACGTU":
        NEITHER = True
        break
    elif i == "T":
        DNA = True
    elif i == "U":
        RNA = True

if NEITHER:
    print("neither")
elif DNA and RNA:
    print("neither")
elif DNA:
    print("DNA")
elif RNA:
    print("RNA")
else:
    print("both")

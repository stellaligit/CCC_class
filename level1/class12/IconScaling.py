k = int(input())

'''
icon = [
    "*x*",
    " xx",
    "* *"
]

def printBlock(line):
    for m in range(3):
        for i in range(k):
            for j in range(k):
                print(line[m][0], end="")
            for j in range(k):
                print(line[m][1], end="")
            for j in range(k - 1):
                print(line[m][2], end="")
            print(line[m][2])

printBlock(icon)
'''

def printBlock(line):
    for i in range(k):
        for j in range(k):
            print(line[0], end="")
        for j in range(k):
            print(line[1], end="")
        for j in range(k - 1):
            print(line[2], end="")
        print(line[2])


printBlock("*x*")
printBlock(" xx")
printBlock("* *")

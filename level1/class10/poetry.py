n = int(input())
for i in range(n):
    last_syllable = []
    for j in range(4):
        t = input().split()
        w = t[-1].lower()
        for k in range(-1, -len(w) - 1, -1):
            if w[k] in "aeiou":
                w = w[k:]
                last_syllable.append(w)
                break
        else:
            last_syllable.append(w)

    if last_syllable[0] == last_syllable[1] == last_syllable[2] == last_syllable[3]:
        print("perfect")
    elif last_syllable[0] == last_syllable[1] and last_syllable[2] == last_syllable[3]:
        print("even")
    elif last_syllable[0] == last_syllable[2] and last_syllable[1] == last_syllable[3]:
        print("cross")
    elif last_syllable[0] == last_syllable[3] and last_syllable[1] == last_syllable[2]:
        print("shell")
    else:
        print("free")

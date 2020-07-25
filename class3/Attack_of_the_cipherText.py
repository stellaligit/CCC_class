p = input()
c = input()
q = input()

for i in range(len(q)): 
    ch = q[i]
    ch_is_found = False
    for j in range(len(c)):
        if ch == c[j]:
            ch = p[j]
            ch_is_found = True
            break
    if ch_is_found == False:
        ch = "."
    print(ch, end="")
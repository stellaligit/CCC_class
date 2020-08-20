n = int(input())
s1 = input().split()
s2 = input().split()

m = {}
good = True

for i in range(n):
    if s1[i] == s2[i]:
        print("bad")
        good = False
        break
    
    if s2[i] in m:
        if m[s2[i]] != s1[i]:
            print("bad")
            good = False
            break
    else:
        m[s1[i]] = s2[i]

if good:
    print("good")
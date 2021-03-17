import sys
input = sys.stdin.readline

zodiac = ["Ox","Tiger","Rabbit","Dragon","Snake","Horse","Goat","Monkey","Rooster","Dog","Pig","Rat"]
cow = {}
cow['Bessie'] = ('Ox', 0)
for _ in range(int(input())):
    s = input().strip().split()
    year, age = cow[s[7]]
    id = zodiac.index(year)
    if s[3] == 'previous':
        while zodiac[id] != s[4]:
            id, age = id-1, age+1
            if id < 0:
                id += 12
        if year == s[4]:
            age += 12
    else:
        while zodiac[id] != s[4]:
            id, age = id+1, age-1
            if id >= 12:
                id -= 12
        if year == s[4]:
            age -= 12
    cow[s[0]] = (s[4], age)
print(abs(cow['Bessie'][1] - cow['Elsie'][1]))

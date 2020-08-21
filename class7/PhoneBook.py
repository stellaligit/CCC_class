n1 = int(input())

# find matching phone calls and person    
m = {}
for i in range(n1):
    t = input().split()
    m[int(t[1])] = t[0]

n2 = int(input())

# find how many phone calls were made to each person
a = {}
for i in range(n2):
    number = int(input())
    if number not in a:
        a[number] = 1
    else:
        a[number] = a[number] + 1

# find the phone call called most
max = 0
for i in a:
    if a[i] > max:
        max = a[i]
        number = i
    elif a[i] == max:
        if i < number:
            number = i

# find the person who got called most
print(m[number])
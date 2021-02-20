# s = input()
# L_count = 0
# M_count = 0
# S_count = 0

# for i in range(len(s)):
#     if s[i] == "L":
#         L_count += 1
#     elif s[i] == "M":
#         M_count += 1
#     else:
#         S_count += 1

# organized = str(L_count * "L") + str(M_count * "M") + str(S_count * "S")

# if s == organized:
#     print("0")
# else:
#     bad = []
#     good = []
#     for i in range(len(s)):
#         if s[i] != organized[i]:
#             bad.append(s[i])
#             good.append(organized[i])
    
#     if s[i] != organized[i]:
#         count += 1
    
#     print(count)

s = input()
L_count = 0
M_count = 0
S_count = 0

for i in range(len(s)):
    if s[i] == "L":
        L_count += 1
    elif s[i] == "M":
        M_count += 1
    else:
        S_count += 1

organized = str(L_count * "L") + str(M_count * "M") + str(S_count * "S")

count = 0
flag = False
number = len(s)
while number > 0:
    if s == organized:
        print("0")
        flag = True
        break
    elif s[i] != organized[i]:
        count += 1
    number -= 1

if not flag:
    print(count - 1)

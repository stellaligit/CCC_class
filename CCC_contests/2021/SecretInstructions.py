nums = []
while True:
    n = input()
    if n == "99999":
        break
    else:
        nums.append(n)

previous = ""
for i in nums:
    sum = int(i[0]) + int(i[1])
    integer = int(i[2:])
    if sum % 2 == 0 and sum != 0:
        previous = "right"
        print("right", integer)
    elif sum % 2 == 1 and sum != 0:
        previous = "left"
        print("left", integer)
    else:
        print(previous, integer)
s = input()
clubs = []
diamonds = []
hearts = []
spades = []
curr = ""

for i in s:
    if i == "C":
        curr = "C"
        continue
    elif i == "D":
        curr = "D"
        continue
    elif i == "H":
        curr = "H"
        continue
    elif i == "S":
        curr = "S"
        continue
    if curr == "C":
        clubs.append(i)
    elif curr == "D":
        diamonds.append(i)
    elif curr == "H":
        hearts.append(i)
    elif curr == "S":
        spades.append(i)

def points(arr):
    len_arr = len(arr)
    arr_sum = 0
    if len_arr == 0:
        arr_sum = 3
    elif len_arr == 1:
        arr_sum = 2
    elif len_arr == 2:
        arr_sum = 1
    
    for i in arr:
        if i == "A":
            arr_sum += 4
        elif i == "K":
            arr_sum += 3
        elif i == "Q":
            arr_sum += 2
        elif i == "J":
            arr_sum += 1
    
    return arr_sum

club_sum = points(clubs)
diamond_sum = points(diamonds)
heart_sum = points(hearts)
spade_sum = points(spades)

total_sum = club_sum + diamond_sum + heart_sum + spade_sum

print("Cards Dealt Points")
print("Clubs", *clubs, club_sum, sep=" ")
print("Diamonds", *diamonds, diamond_sum, sep=" ")
print("Hearts", *hearts, heart_sum, sep=" ")
print("Spades", *spades, spade_sum, sep=" ")
print(" Total", total_sum)
s = input()
clubs = []
diamonds = []
hearts = []
spades = []
curr = ""

for i in s:
    if i in "CDHS":
        curr = i
    else:
        if curr == "C":
            clubs.append(i)
        elif curr == "D":
            diamonds.append(i)
        elif curr == "H":
            hearts.append(i)
        elif curr == "S":
            spades.append(i)

def points(arr):
    arr_sum = 0
    if len(arr) < 3:
        arr_sum = 3 - len(arr)
    
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
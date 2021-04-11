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

club_sum = 0
diamond_sum = 0
heart_sum = 0
spade_sum = 0

len_clubs = len(clubs)
len_diamonds = len(diamonds)
len_hearts = len(hearts)
len_spades = len(spades)

if len_clubs == 0:
    club_sum = 3
elif len_clubs == 1:
    club_sum = 2
elif len_clubs == 2:
    club_sum = 1

if len_diamonds == 0:
    diamond_sum = 3
elif len_diamonds == 1:
    diamond_sum = 2
elif len_diamonds == 2:
    diamond_sum = 1

if len_hearts == 0:
    heart_sum = 3
elif len_hearts == 1:
    heart_sum = 2
elif len_hearts == 2:
    heart_sum = 1

if len_spades == 0:
    spade_sum = 3
elif len_spades == 1:
    spade_sum = 2
elif len_spades == 2:
    spade_sum = 1

for i in clubs:
    if i == "A":
        club_sum += 4
    elif i == "K":
        club_sum += 3
    elif i == "Q":
        club_sum += 2
    elif i == "J":
        club_sum += 1

for i in diamonds:
    if i == "A":
        diamond_sum += 4
    elif i == "K":
        diamond_sum += 3
    elif i == "Q":
        diamond_sum += 2
    elif i == "J":
        diamond_sum += 1

for i in hearts:
    if i == "A":
        heart_sum += 4
    elif i == "K":
        heart_sum += 3
    elif i == "Q":
        heart_sum += 2
    elif i == "J":
        heart_sum += 1

for i in spades:
    if i == "A":
        spade_sum += 4
    elif i == "K":
        spade_sum += 3
    elif i == "Q":
        spade_sum += 2
    elif i == "J":
        spade_sum += 1

total_sum = club_sum + diamond_sum + heart_sum + spade_sum

print("Cards Dealt Points")
print("Clubs", *clubs, club_sum, sep=" ")
print("Diamonds", *diamonds, diamond_sum, sep=" ")
print("Hearts", *hearts, heart_sum, sep=" ")
print("Spades", *spades, spade_sum, sep=" ")
print(" Total", total_sum)
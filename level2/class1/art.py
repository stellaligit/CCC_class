n = int(input())

smallest_x = 100
biggest_x = 0
smallest_y = 100
biggest_y = 0

for i in range(n):
    c = [int(i) for i in input().split(",")]

    if c[0] < smallest_x:
        smallest_x = c[0]
    if c[0] > biggest_x:
        biggest_x = c[0]
    if c[1] < smallest_y:
        smallest_y = c[1]
    if c[1] > biggest_y:
        biggest_y = c[1]

print(smallest_x - 1, smallest_y - 1, sep=",")
print(biggest_x + 1, biggest_y + 1, sep=",")

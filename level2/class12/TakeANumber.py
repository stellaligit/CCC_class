# Int 1 = Number of "takes" during that day
# Int 2 = Number of "takes" minus number of "serves" during that day
# Int 3 = N plus number of total "takes"

n = int(input())
num_of_takes = 0
total_num_of_takes = n
num_of_serves = 0
while True:
    s = input()
    if s == "EOF":
        break

    if s == "TAKE":        
        num_of_takes += 1
        total_num_of_takes += 1
    elif s == "SERVE":
        num_of_serves += 1
    else:
        print(num_of_takes, num_of_takes - num_of_serves, total_num_of_takes % 999)
        num_of_serves = 0
        num_of_takes = 0
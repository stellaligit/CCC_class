n, m = [int(s) for s in input().split()]

last_position = 0
leave_time = 0
for i in range(n):
    d, r, g = [int(s) for s in input().split()]
    arrive_time = leave_time + d - last_position
    mod = arrive_time % (r + g)

    wait_time = 0
    if mod < r:
        wait_time = r - mod
    leave_time = arrive_time + wait_time

    last_position = d

print(leave_time + m - last_position)

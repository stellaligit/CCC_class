n, m = [int(s) for s in input().split()]

last_position = 0
leave_time = 0
for i in range(n):
    d, r, g = [int(s) for s in input().split()]
    arrive_time = leave_time + d - last_position
    mod = arrive_time % (r + g)
    
    leave_time = arrive_time if mod >= r else arrive_time + r - mod

    last_position = d

print(leave_time + m - last_position)

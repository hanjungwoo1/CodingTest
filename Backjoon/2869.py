import math

day_time, night_time, goal = map(int, input().split())

count = 0
height = 0

new_goal = goal - day_time
count = 1
count += math.ceil(new_goal / (day_time - night_time))

print(count)
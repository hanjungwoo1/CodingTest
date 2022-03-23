x = int(input())
num_list = []

num = 0
num_count = 0

while num_count < x:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    i = x - num_count
    j = num - i + 1
else:
    i = num - (x - num_count) + 1
    j = x - num_count

print(f"{i}/{j}")
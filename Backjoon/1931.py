import sys

n = int(sys.stdin.readline())

data = []

for _ in range(n):
    x, y = sys.stdin.readline().split()
    data.append([int(x), int(y)])


#sorted_data = sorted(data, key=lambda item : item[0])
sorted_data = sorted(data, key=lambda item : (item[1], item[0]))
# 빨리 끝나면서, 빨리 시작하는 것

last = 0
count = 0

for x, y in sorted_data:
    if x >= last:
        count += 1
        last = y

print(count)
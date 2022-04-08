"""
입력 예시
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""

n = int(input())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

flag = True
for x, line in enumerate(data):

    if flag:
        flag = False
        continue

    for y, num in enumerate(line):
        # data[x, y]
        if y == 0:
            data[x][y] = data[x][y] + data[x-1][y]
        elif y == x:
            data[x][y] = data[x][y] + data[x-1][y-1]
        else:
            data[x][y] = data[x][y] + max(data[x-1][y-1], data[x-1][y])

result = 0

for a in data:
    for b in a:
        result = max(result, b)

print(result)

rows = 4
columns = 3



data = []
num = 1
for i in range(rows):
    now = []
    for j in range(columns):
        now.append(num)
        num += 1
    data.append(now)

print(data)

x1, y1, x2, y2 = 2, 1,2, 3

temp = []

for x in range(x1-1, x2):
    print(x)
    temp.append(data[x][y2-1])

print(temp)

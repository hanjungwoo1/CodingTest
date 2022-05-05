data = [1, 4, 3, 2]

data.sort()

sum = 0
pair = []
for x in data:
    pair.append(x)

    if len(pair) == 2:
        sum += min(pair)
        pair = []

print(sum)
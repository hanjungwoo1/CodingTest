data = input()
data = data.split('-')
for i, x in enumerate(data):
    minus = x.split('+')
    sum = 0
    for y in minus:
        sum += int(y)
    data[i] = sum

result = data[0]

for i in range(1, len(data)):
    result -= data[i]

print(result)
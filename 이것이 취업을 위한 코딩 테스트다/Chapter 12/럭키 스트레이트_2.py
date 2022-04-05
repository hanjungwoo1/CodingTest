data = input()

length = len(data)//2

left = data[:length]
right = data[length:]

result = 0

for x, y in zip(left, right):
    result += int(x)-int(y)

if result == 0:
    print("LUCKY")
else:
    print("READY")
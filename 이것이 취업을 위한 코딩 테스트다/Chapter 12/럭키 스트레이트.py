data = input()
length = len(data)//2

first = data[:length]
second = data[length:]

left = 0
right = 0
for x, y in zip(first, second):
    left += int(x)
    right += int(y)

if left == right:
    print("LUCKY")
else:
    print("READY")

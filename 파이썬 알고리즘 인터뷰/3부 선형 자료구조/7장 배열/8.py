data = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

length = len(data)

volume = 0
for i, x, in enumerate(data):
    if i == 0 or i == length-1:
        continue

    left = data[:i]
    right = data[i+1:]
    print(left, right)
    print(i, x)

    left_index = i-1
    right_index = i+1

    print("max left : ", max(left))
    print("max right : ", max(right))
    if max(left) > x and max(right) > x:
        volume += min(max(left), max(right)) - x


print("result : ", volume)
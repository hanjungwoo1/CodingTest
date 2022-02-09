a = int(input())

count = 0
data = a
while(True):
    if data<10:
        first = 0
        second = data
    else:
        first, second = str(data)

    new = int(first) + int(second)

    new_sec = str(new)[-1]

    data = int(str(second) + str(new_sec))
    count = count + 1


    if a == data:
        break

print(count)
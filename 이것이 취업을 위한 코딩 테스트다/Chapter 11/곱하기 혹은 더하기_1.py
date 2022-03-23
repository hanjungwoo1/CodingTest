data = input()

total = 0
for i, x in enumerate(data):
    if x == '0' or total == 0:
        total = total + int(x)
    else:
        total = total * int(x)

print(total)
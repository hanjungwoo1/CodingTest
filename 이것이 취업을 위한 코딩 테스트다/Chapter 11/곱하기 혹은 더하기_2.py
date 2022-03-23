data = input()

result = 0
for x in data:
    if x == 0 or result == 0:
        result = result + int(x)
    else:
        result = result * int(x)

print(result)

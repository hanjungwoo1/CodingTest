n = int(input())

for x in range(1, n+1):
    data = x
    for y in str(x):
        data += int(y)

    if n == data:
        print(x)
        break

    if x == n:
        print(0)
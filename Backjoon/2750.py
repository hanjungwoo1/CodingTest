n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))


array.sort()
for x in array:
    print(x)
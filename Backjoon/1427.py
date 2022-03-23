array = list(map(int, input()))
array.sort(reverse=True)

for x in array:
    print(x,end='')
n = int(input())

data = []

for _ in range(n):
    x, y = map(int, input().split())
    data.append([x, y])

sorted_data = sorted(data, key= lambda x: (x[0], x[1]))

for x,y in sorted_data:
    print(str(x) +" "+str(y))
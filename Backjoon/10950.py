
list = []

for _ in range(9):
    list.append(int(input()))

max = 0
index = 0
for i, x in enumerate(list):
    if max<x:
        max = x
        index = i+1

print(max)
print(index)
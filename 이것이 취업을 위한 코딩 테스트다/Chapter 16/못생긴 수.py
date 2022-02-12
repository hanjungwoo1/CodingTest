from itertools import product

data = []
for i1, i2, i3, i4 in product([1, 2, 3, 5], [1, 2, 3, 5], [1, 2, 3, 5], [1, 2, 3, 5]):
    data.append(i1 * i2 * i3 * i4)


data = list(set(data))
data.sort()

N = int(input())

print(data[N-1])
from itertools import product

data = [1,2,3,5]

count = 0
ugly = []
for x in product(data, data, data, data, data):
    print(x)
    ugly.append(x[0]*x[1]*x[2]*x[3]*x[4])
    count +=1

ugly = list(set(ugly))
print(len(ugly))

n = int(input())

print(ugly[n])
print(ugly)

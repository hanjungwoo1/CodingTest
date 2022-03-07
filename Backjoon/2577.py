a = int(input())
b = int(input())
c = int(input())

total = str(a*b*c)

for x in range(10):
    print(total.count(str(x)))
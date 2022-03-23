data = input().split()

one = str(data[0])
two = str(data[1])

one = one[::-1]
two = two[::-1]

print(max(int(one), int(two)))
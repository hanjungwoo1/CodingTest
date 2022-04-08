data1 = input()
data2 = input()

print(data1)
print(data2)


for x in data1:
    temp = data2.find(x)

    if temp != -1:
        data2 = data2[:temp] + data2[temp+1:]


print(len(data2))

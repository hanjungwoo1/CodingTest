food_time = [3,1,2]
k = 5
index = 0
length = len(food_time)
print(length)
while k > 0:
    if food_time[index] > 0:
        food_time[index] -= 1
        index += 1
        k -= 1
    else:
        index += 1

    index = index % length
    print(food_time, k, index)

print(index+1)


T = [73, 74, 75, 71, 69, 72, 76, 73]

result =[]

for i in range(len(T)):
    count = 0
    for j in range(i+1, len(T)):
        count+=1
        if T[i] < T[j]:
            break

        if j == len(T)-1:
            count = 0
    result.append(count)

print(result)
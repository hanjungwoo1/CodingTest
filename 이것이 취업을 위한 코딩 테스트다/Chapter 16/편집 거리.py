"""
입력 예시 1
cat
cut

출력 예시
1

입력 예시 2
sunday
saturday

출력 예시 2
3
"""
data1 = input()
data2 = input()

print(data1)
print(data2)


for x in data1:
    temp = data2.find(x)

    if temp != -1:
        data2 = data2[:temp] + data2[temp+1:]


print(len(data2))

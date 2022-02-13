"""
입력 예시 1
K1KA5CB7

출력 예시 1
ABCKK13

입력 예시 2
AJKDLSI412K4JSJ9D

출력 예시 2
ADDIJJJKKLSS20
"""
data = input()

list = []
total = 0
for x in data:
    if x.isdigit():
        total += int(x)
    else:
        list.append(x)

list = sorted(list)

answer =''
for x in list:
    answer += x

print(answer+str(total))
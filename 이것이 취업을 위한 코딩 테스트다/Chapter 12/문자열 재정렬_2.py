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
answer = ''
result = 0
string = ""
for x in data:
    if x.isdigit():
        result += int(x)
    else:
        string += x

for y in sorted(string):
    answer += y

print(answer + str(result))
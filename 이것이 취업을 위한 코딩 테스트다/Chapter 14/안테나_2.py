"""
입력 예시 1
4
5 1 7 9

출력 예시 1
5
"""

n = int(input())
data = sorted(list(map(int, input().split())))

# print(n)
# print(data)

result = 1e9
answer = 1e9
for x in range(1, data[-1]+1):

    total = 0

    for y in data:
        total += abs(x-y)

    if result>total:
        result = total
        answer = x

print(answer)
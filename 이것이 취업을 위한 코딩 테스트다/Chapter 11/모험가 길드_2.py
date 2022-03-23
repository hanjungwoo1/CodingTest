"""
입력 예시
5
2 3 1 2 2

출력 예시
2
"""

n = int(input())

data = sorted(list(map(int, input().split())))

result = 0
count = 0
for i in data:
    count +=1
    if count >= i:
        result +=1
        count = 0
print(result)
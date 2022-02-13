"""
입력 예시
5 3
1 3 2 3 2

출력 예시
8

입력 예시 2
8 5
1 5 4 3 2 4 5 2
25
"""

n, m = map(int, input().split())

data = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i,n):
        if i == j:
            continue
        if data[i] == data[j]:
            continue
        count += 1

print(count)
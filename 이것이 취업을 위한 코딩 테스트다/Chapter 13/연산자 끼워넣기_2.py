"""
예제 입력 1
2
5 6
0 0 1 0

예제 출력 1
30
30


예제 입력 2
3
3 4 5
1 0 1 0

예제 출력 2
35
17


예제 입력 3
6
1 2 3 4 5 6
2 1 1 1

예제 출력 3
"""

n = int(input())
data = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())

min_value = 1e9
max_value = -1e9


def dfs(i, now):
    global plus, minus, multi, div, min_value, max_value
    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, now+data[i])
            plus += 1

        if minus > 0:
            minus -= 1
            dfs(i+1, now-data[i])
            minus -= 1

        if multi > 0:
            multi -= 1
            dfs(i+1, now*data[i])
            multi +=1

        if div > 0:
            div -= 1
            dfs(i+1, now/data[i])
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)
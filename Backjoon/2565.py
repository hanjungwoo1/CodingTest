"""
전깃줄

예제 입력 1
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6

예제 출력 1
3
"""
from sys import stdin


n = int(stdin.readline())

lines = []

for _ in range(n):
    a, b = map(int, stdin.readline().split())

    lines.append((a, b))

lines.sort()

# a 전깃줄 번호를 기준으로 오름차순 정렬된 b 전깃줄 번호의 수열
a_to_b = list(map(lambda x: x[1], lines))

# LIS 알고리즘 구현
max_length = [1] * n

for i in range(1, n):
    for j in range(i):
        if a_to_b[i] > a_to_b[j]:
            max_length[i] = max(max_length[i], max_length[j] + 1)

# 없애야 하는 전깃줄의 최소 개수 = 현재 전깃줄의 개수 - 겹치치 않는 최대 전깃줄의 개수
print(n - max(max_length))
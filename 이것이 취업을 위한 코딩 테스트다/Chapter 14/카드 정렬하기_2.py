"""
입력 예시1
3
10
20
40

출력 예시 1
100

입력 예시 2
4
10
20
40
50

출력 예시
220
"""

import heapq

n = int(input())

card = []

for _ in range(n):
    heapq.heappush(card, int(input()))

result = 0

while len(card) != 1:
    one = heapq.heappop(card)
    two = heapq.heappop(card)

    data = one + two
    result += data
    heapq.heappush(card, data)

print(result)
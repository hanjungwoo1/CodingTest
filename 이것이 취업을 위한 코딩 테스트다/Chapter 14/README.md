# 정렬 문제

## Q 23. 국영수
### 1st, 22/2/20 solve
- https://www.acmicpc.net/problem/10825
- 국영수.py
```python 
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])) 
```

## Q 24. 안테나
### 1st, 22/2/20 solve
- https://www.acmicpc.net/problem/18310
- 안테나.py


## Q 25. 실패율
### 1st, 22/2/20 solve
- https://programmers.co.kr/learn/courses/30/lessons/42889
- 실패율_official.py

## Q 26. 카드 정렬하기
### 1st, 22/2/20 solve
- https://www.acmicpc.net/problem/1715
- 카드 정렬하기.py
```python
import heapq
...
card = []

for _ in range(n):
    heapq.heappush(card, int(input()))

result = 0

while len(card) != 1:
    one = heapq.heappop(card)
    two = heapq.heappop(card)
...
```
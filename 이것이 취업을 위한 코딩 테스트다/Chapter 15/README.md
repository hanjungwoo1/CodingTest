# 이진 탐색 문제

## Q 27. 정렬된 배열에서 특정 수의 개수 구하기
### 1st, 22/4/08

 - 정렬된 배열에서 특정 수의 개수 구하기(1).py
 - 정렬된 배열에서 특정 수의 개수 구하기(2).py
   - bisect
 ```python
from bisect import bisect_left, bisect_right

data = list(map(int, input().split()))

left = bisect_left(data, x) # 첫 x의 index
right = bisect_right(data, x) # x가 아닌 곳에 index
```


## Q 28. 고정점 찾기
### 1st, 22/4/08 -> perfect!!

- 고정점 찾기.py

## Q 29. 공유기 설치
### 1st, 22/4/08

- https://www.acmicpc.net/problem/2110
- 공유기 설치

## Q 30. 가사 검색
### 1st. 22/4/08 -> 유효성

- https://programmers.co.kr/learn/courses/30/lessons/60060
- 가사 검색.py

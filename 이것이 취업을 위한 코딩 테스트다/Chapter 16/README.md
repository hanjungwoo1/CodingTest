# 다이나믹 프로그래밍 문제

## Q 31. 금광
### 1st, 22/2/12

- 금광_official.py

## Q 32. 정수 삼각형
### 1st, 22/2/12

- 정수 삼각형_official.py

## Q 33. 퇴사
### 1st, 22/2/13
- 거꾸로 점화식 계산
- 퇴사_official.py

## Q 34. 병사 배치하기
### 1st, 22/2/13
- LIS 기법
```python
n = int(f())
a = [int(x) for x in f().split()]
dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(len(a) - max(dp))
```
- 병사배치하기.py
- 병사 배치하기_official.py

## Q 35. 못생긴 수
### 1st, 22/2/13 solve
- 중복순열, product
```python
from itertools import product

data = []
for i1, i2, i3, i4 in product([1, 2, 3, 5], [1, 2, 3, 5], [1, 2, 3, 5], [1, 2, 3, 5]):
    data.append(i1 * i2 * i3 * i4)
```
- 못생긴 수.py
- 못생긴 수_official.py

## Q 36. 편집 거리
### 1st, 22/2/13 solve

- 편집 거리.py
- 같은 문자 제거 : 필요한건 있는거에서 바꾸고, 없는건 채워 넣기 -> 2번째의 남는 문자의 갯수?
- 편집 거리_official.py
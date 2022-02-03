# CodingTest
for Coding Test in Python3

## 1. 이것이 취업을 위한 코딩 테스트다

### Chapter 4 구현
- 4-2.py, String에 char 파악
``` python
if '3' in str(i) + str(j) + str(k) :
# 03시 20분 35초이면, '032035'로 만들어 '3'이 포함되는지
```

- 4-3.py, 
``` python 
column = int(ord(input_data[0])) - int(ord('a')) + 1
# 소문자 input_data[0]이 몇번째 인지
# ex) b = 2
```

### Chapter 6 정렬
- 6-11.py, 파이썬 라이브러리 sorted by key=lambda
```python 
array = sorted(array, key=lambda student: student[1])
```
- 6-11.py 파이썬 괄호 차이
```
() = 튜플, 값이 변하지 않음 # 안쓰면 됨
[] = 리스트, 주로 사용
{} = 딕셔너리, Key = value
```

### Chapter 7 이진 탐색
- 7-4.py 빠르게 입력받기
```python
import sys
input_data = sys.stdin.readline().rstrip()
```

## 2. 프로그래머스

### level 1
``` python
from itertools import combinations
A = list(combinations(nums, 3))
# 3가지 선택하기
```

### level 2
```python
for x in range(x, y, z):
    print(x)
# x부터 y까지 z씩 상승
```
     

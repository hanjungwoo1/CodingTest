#APPENDIX A
## 자료형
### 수자료형
#### 정수형
#### 실수형
#### 수 자료형의 연산

### 리스트 자료형
#### 리스트 만들기
#### 리스트의 인덱싱과 슬라이싱
#### 리스트 컴프리헨션
#### 리스트 관린 기타 메서드

### 문자열 자료형
#### 문자열 초기화
#### 문자열 연산

### 튜플 자료형

### 사전 자료형
#### 사전 자료형 관련 함수

### 집합 자료형
#### 집합 자료형 소개
#### 집합 자료형의 연산
#### 집합 자료형 관련 함수

## 조건문
#### 비교 연산자
#### 논리 연산자
#### 파이썬 기타 연산자

## 반복문
### while문
### for문

## 함수

## 입출력


## 주요 라이브러의 문법과 유의점
표준 라이브러리 : 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해놓은 라이브러리

- 내장 함수 : print(), input(), sorted()
- itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리. 순열과 조합
- heapq : 힙(heap) 기능을 제공하는 라이브러리. 우선순위 큐
- bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리.
- collenctions : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리


#### 내장함수
sum()
```python
result = sum([1,2,3,4,5])
print(result)
# 15
```
min()
```python
result = min([7, 3, 5, 2])
print(result)
# 2
```
max()
```python
result = max([7, 3, 5, 2])
print(result)
# 7
```
eval()
```python
result = eval("(3+5)*7")
print(result)
# 56
```
sorted()
```python
result = sorted([9, 1, 8, 5, 4])
print(result)
# [1, 4, 5, 8, 9]
result = sorted([9, 1, 8, 5, 4], reverse= True)
print(result)
# [9, 8, 5, 4, 1]
```
sort()
```python
data = [9, 1, 8, 5, 4]
data.sort()
print(data)
# [1, 4, 5, 8, 9]
```

#### itertools
permutations
```python
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```
combinations
```python
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
```
product
```python
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))

print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')
```
combinations_with_replacement
```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))

print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
```

#### heapq
heapsort - Min Heap
```python
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Max heap
```python
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

#### bisect
- bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
# 2
# 4
```
count_by_range
```python
from bisect import bisect_left, bisect_right
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))
# 2
# 6
```

#### collections
deque
```python
from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))
# deque([1, 2, 3, 4, 5])
# [1, 2, 3,4, 5]
```
Counter
```python
from collections import Counter

count = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(count['blue'])
print(count['green'])
print(dict(count))
# 3
# 1
# {'red' : 2, 'blue' : 3, 'green' : 1}

```
#### math
factorial
```python
import math
print(math.factorial(5))
# 120
```
sqrt
```python
import math
print(math.sqrt(7))
# 2.6457513110645907
```
gcd
```python
import math
print(math.gcd(14, 21))
# 7
```
pi, e
```python
import math
print(math.pi)
print(math.e)
# 3.141592653589793
# 2.718281828459045
```

## 자신만의 알고리즘 노트 만들기
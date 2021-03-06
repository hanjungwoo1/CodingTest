# CodingTest
for Coding Test in Python3

## 1. 이것이 취업을 위한 코딩 테스트다

### Chapter 4 구현
- 4-2.py, String에 char 파악
``` python
if '3' in str(i) + str(j) + str(k) :
# 03시 20분 35초이면, '032035'로 만들어 '3'이 포함되는지
```

- 4-3.py, 문자를 숫자로
``` python 
column = int(ord(input_data[0])) - int(ord('a')) + 1
# 소문자 input_data[0]이 몇번째 인지
# ex) b = 2
```

- 4-4.py, 게임 개발

### Chapter 5 DFS/BFS
- 5-8.py DFS
- 5-9.py BFS
- 5-10.py 음료수 얼려먹기
- 5-11.py 미로 탈출

### Chapter 6 정렬
- 6-3.py 삽입 정렬 소스코드, 줄어드는 for
```python
for j in range(i, 0, -1):
```
- 6-11.py, 파이썬 라이브러리 sorted by key=lambda
```python
lambda 매개변수 : 표현식
```
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

- 7-8.py 

### Chpater 8 다이나믹 프로그래밍
- 8-5.py
```python
d[i] = min(d[i], d[i // 2] + 1)
```
- 8-6.py
```python
d[i] = max(d[i - 1], d[i - 2] + array[i])
```
- 8-7.py
```python
d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796
```
- 8-8.py
```python
d[j] = min(d[j], d[j - array[i]] + 1)
```

### Chapter 9 최단 경로
- 최소 힙을 최대 힙처럼 Tip: 음수 부호를 붙여서 넣었다가, 꺼낸 다음에 다시 음수 부호


### Chapter 14 정렬 문제
- Q. 23 국영수
- sort에 key=lamda를 적용, 내림차순 오름차순 순서대로 적용하는 법
```python
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
```

- Q 26. 카드 정렬하기
- 힙 구조 사용법
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
     


## 3. Backjoon

### A+B-4
 - 10951
 - 입력이 끝나지 않음, 언제 끝날지 모를때 try catch
```python
try:
    while(True):
        a, b = map(int, input().split())
        print(a+b)
except:
    exit()
```

### 최댓값
- 2562
```python
max(num_list)
num_list.index(data)
```

### 숫자의 개수
- 2577
```python
list.count(data)
```

### 평균은 넘겠지
 - 4344
```pythonn = int(input())
print('%.3f' %rate + '%')
# 40.000%
# 57.143%
```

### 색종이 만들기
 - 2630
 - 쿼드 트리 방식(+1992)

### 가장 긴 증가하는 부분 수열
 - 11053(n^2), 12015(nlogn), 11054(바이토닉)
 - LIS(Longest Increasing Subsequence) 알고리즘
 
### RGB거리
 - 1149
 - 최소 구하는 점화식

```python
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
```

### 수 정렬하기2
 - 2751
```python
int(input()) # timeout
int(sys.stdin.readline())

print(i) # timeout
sys.stdout.write(str(i)+'\n')
```

### DFS와 BFS
 - 1260(Ori, DFS BFS)
 - 2606, 2667, 1012, 2178, 7576, 7569, 1697, 2206*, 7562 






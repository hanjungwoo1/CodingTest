# Backjoon
## Cheat Sheet

### N과 M(9)
- 22/02/13
- 15663
```python
visited = [False] * n
```

### N-Queen
- 22/02/13
- 9663
- https://sso-feeling.tistory.com/415?category=913126

### 피보나치 함수
- 22/03/07
- 1003

2차원 리스트 초기화할 때는 반드시 리스트 컴프리헨션
```python
array = [[0] * m for _ in range(n)]
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
 - 쿼드 트리 방식

### 쿼드 트리
 - 1992
 - 쿼드 트리 방식

### 가장 긴 증가하는 부분 수열
 - 11053(n^2), 12015(nlogn), 11054(바이토닉)
 - LIS(Longest Increasing Subsequence) 알고리즘
```python
# 11053번
x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
```

```python 

# 12015번
import bisect

x = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))

```

```python
#11054

x = int(input())

case = list(map(int, input().split()))
reverse_case = case[::-1]

increase = [1 for i in range(x)] # 가장 긴 증가하는 부분 수열
decrease = [1 for i in range(x)] # 가장 긴 감소하는 부분 수열(reversed)

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease[x-i-1] -1

print(max(result))

```

### RGB거리
 - 1149

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
 - 2606, 2667, 1012, 2178, 7576, 7569, 1697, 2206*, 7562, 1707*


### 스택
 - 10828, 10773, 9012, 4949(출력 초과), 1874*
 - 17298*
```python
data = [3,4, 5, 6, 7]
print(*data)
# 3 4 5 6 7
```


### 큐, 덱
 - 18258, 2164, 11866
 - 

### 문자열
 - 11654, 11720, 10809, 2675, 1157, 1152, 2908, 5622*, 2941, 1316*

### 기본 수학 1
 - 1712, 2292, 1193

### 재귀
 - 10872, 10870, 2447*,11729

### 브루트 포스
 - 2798, 2231, 7568, 1018, 1436

### 정렬
 - 2750, 2751
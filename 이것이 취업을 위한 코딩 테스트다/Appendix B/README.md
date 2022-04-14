#기타 알고리즘

## 더 알아두면 좋은 알고리즘
### 소수의 판별
소수 : 2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수

```python
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True

print(is_prime_number(4))
print(is_prime_number(7))
# False
# True
```
제곱근으로 판별하는 소수
```python
import math

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True

print(is_prime_number(4))
print(is_prime_number(7))
# False
# True
```

### 에라토스테네스의 체 
다수의 소수를 찾아야하는 문제에서 자주 사용

1. 모든 짝수 제거
2. 소수의 배수를 순차적으로 제거
```python
import math

n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우(남은 수의 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
```

### 투 포인터
투 포인터 : 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리

**'특정한 합을 가지는 부분 연속 수열 찾기'**
1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)을 가르키도록 한다.
2. 현재 부분합이 M과 같으면 카운트한다.
3. 현재 부분합이 M보다 작으면 end를 1증가 시킨다.
4. 현재 부분합이 M보다 크거나 같으면 start를 1 증가시킨다.
5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다

```python
n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
    
print(count)
# 3
```

**'정렬되어 있는 두 리스트 합집합'**


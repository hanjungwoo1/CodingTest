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
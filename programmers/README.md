# Programmers

## Level 1


## Level 2

### 줄 서는 방법
- https://school.programmers.co.kr/learn/courses/30/lessons/12936
- 시간초과, Permutations -> 단순 연산 반복

### 가장 큰 정사각형 찾기
- DP



### 후보키

```
add(값) - 집합에 새로운 값을 추가한다. (중복된 값은 무시)
remove(값) - 전달받은 값을 삭제 (없을 때 에러 메시지를 출력)
discard(값) - 전달받은 값을 삭제 (없을 때 그냥 무시)
clear() - 집합에 있는 모든 값을 삭제

isdisjoint() - 두 집합이 공통 원소를 갖지 않는가?
issubset() - 부분집합(subset)인가?
issuperset() - 확대집합(superset)인가?
 - True or False

union() - 합집합을 만들어 리턴
update() - 합집합을 만들어 원본 데이터를 갱신(수정)
difference() - 차집합을 만들어 리턴
intersection() - 교집합을 만들어 리턴
```

### [3차] n진수 게임

- https://school.programmers.co.kr/learn/courses/30/lessons/17687
```python
#재귀함수 이용 - 10진수를 n진수로
def convert(n, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]
```


### 비밀지도
- https://programmers.co.kr/learn/courses/30/lessons/17681

2진법으로 변환
```python
bin(data)
oct(data) # 8진수
hex(data) # 16진수
```


문자열 바꾸기 / Not if 
```python
replace(old, new, [count])
```

### 짝지어 제거하기
- https://programmers.co.kr/learn/courses/30/lessons/12973
- 문자열 짝 제거 -> Stack
- ex) 문장 검사 -> Stack

### 더 맵게
- https://programmers.co.kr/learn/courses/30/lessons/42626
- 힙 사용 

index 처리, try except 사용
```python
try:
    print("1")
except IndexError:
    return -1
```

### 124 나라
- https://programmers.co.kr/learn/courses/30/lessons/12899
- 3진수 처럼 만들기, 수식 계산해서 처리하기

문자열 뒤집기
```python
string[::-1]
[start:stop:step]
```

### 기능 개발
- https://programmers.co.kr/learn/courses/30/lessons/42586 

### 2개 이하로 다른 비트
- https://programmers.co.kr/learn/courses/30/lessons/77885
- 내 풀이 시간 초과, 아이디어 떠올리기

### 피로도
- https://programmers.co.kr/learn/courses/30/lessons/87946
- 전형적인 DFS 문제

### 큰 수 만들기
- https://programmers.co.kr/learn/courses/30/lessons/42883
- stack을 사용한 문제

### 피보나치 수
- https://programmers.co.kr/learn/courses/30/lessons/12945
- 다이나믹, Easy

### 주식가격
- https://programmers.co.kr/learn/courses/30/lessons/42584
- 스택, 큐 / Easy / 시간 줄이는 방법 찾아야함

### 다리를 지나는 트럭
- https://programmers.co.kr/learn/courses/30/lessons/42583
- 스택, 큐 / Easy

### H-index
- https://programmers.co.kr/learn/courses/30/lessons/42747
- 정렬

### 구명보트
- https://programmers.co.kr/learn/courses/30/lessons/42885
- 반대로 생각하기!

### 숫자의 표현
- https://programmers.co.kr/learn/courses/30/lessons/12924
- for문 포인터 다루기




### 올바른 괄호
- https://programmers.co.kr/learn/courses/30/lessons/12909
- solve

### 최댓값과 최솟값
- https://programmers.co.kr/learn/courses/30/lessons/12939
- solve

### 최솟값 만들기
- https://programmers.co.kr/learn/courses/30/lessons/12941
- solve

### 행렬의 곱셈
- https://programmers.co.kr/learn/courses/30/lessons/12949
- solve

### 다음 큰 숫자
- https://programmers.co.kr/learn/courses/30/lessons/12911
- solve

### 프린터
- https://programmers.co.kr/learn/courses/30/lessons/42587
- solve

### N개의 최소공배수
- https://programmers.co.kr/learn/courses/30/lessons/12953
- solve
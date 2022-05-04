# 프로그래밍 언어 선택
수도코드(Pseudocde) : 컴퓨터 프로그램의 작동 원리 또는 알고리즘을 형식이 정해져 있지 않은 고차원(High-Level)언어로 기술

## 경진대회 통계로 알아본 언어 선호도
파이썬, C++

## 프로그래밍 언어 별 특징
C++, 자바, 파이썬, 고(Go), 타입스크립트(TypeScript)


### 루프
C++
```c++
int sum = 0
for (int i = 1; i <= 10; i++) {
    sum += i;
}
```
Java
```Java
int sum = 0
for (int i = 1; i <= 10; i++) {
    sum += i;
```
Python
```python
# 예시 1
sum = 0
for i in range(1, 10 + 1):
    sum += i
# 예시 2
sum = sum(i for i in range(1, 10 + 1))
# 예시 3
sum = sum(range(1, 10+1))
```
GO
```Go
var sum int = 0
for i := 1; i <= 10; i++ {
    sum += i
}
```
TypeScript
```TypeScript
let sum: number = 0;
for (let i = 1; i <= 10; i++){
    sum += i;
}
```
### 제네릭 프로그래밍
제네릭(Generic) : 파라미터의 타입이 나중에 지정(to-be-specified-later)되게 해서 재활용성을 높일 수 있는 프로그래밍 스타일

C++
```C++
template<class T, class U>
bool are_equal(T a, U b){
    return(a == b);
}
are_equal(10, 10.0)
```
Java
```java
public statc<T, U> boolean are_equal(T a, U b){
    return a == b;
}
are_equal(10, 10.0);
```
Python
```python
def are_equal(a, b):
    return a == b

are_equal(10, 10.0)
```
```python
from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def are_equal(a: T, b: U) -> bool:
    return a == b

are_equal(10, 10.0)
```
Go != Generic

TypeScript
```TypeScript
function are_equal<T, U>(a: T, b: U): boolean {
    return +a == +b;
}
are_equal<number, number>(10, 10.0);
```

### 배열 반복
continue

### 구조체

### 클래스


## 코딩 테스트에 최적인 프로그래밍 언어는?
파이썬
### 면접관이 쉽게 이해할 수 있는가?
얼랭(Erlang), 리스프(LISP)는 개성 강한 언어

C++, Java는 지나치게 산만(verbose)

### 코딩 플랫폼에서 지원하는가?
간혹 파이썬 빠진다.

### 유연한 언어인가?
C++, Java는 대표적인 정적 타이핑 언어로 유연함과 거리가 멀다.

### 언어 레벨에서 풍부한 기능을 지원하는가?
C++는 STL이 표준 라이브러리이기 때문에 강력한 자료구조, C는 없음




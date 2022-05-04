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



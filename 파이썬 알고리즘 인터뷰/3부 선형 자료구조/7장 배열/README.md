# 배열

공간 기반의 연속 방식 : 배열 등

포인터 기반의 연결 방식 : 연결 리스트 등

## 7. 두 수의 합
덧셈하여 타겟을만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

 - 7.py (my code)
 - 7-1.py (브루트 포스로 계산)
 - 7-2.py (in을 이용한 탐색)
 - 7-3.py (첫 번째 수를 뺀 결과 키 조회)
 - 7-4.py (조회 구조 개선)
 - 7-5.py (투 포인터 이용)
   - 정렬해야함, 정렬하면 index 못찾음 -> 풀이 불가

|풀이|방식|실행 시간|
|----|----|----|
|1|브루트 포스로 계산|5,284 밀리초|
|2|in을 이용한 탐색|864 밀리초|
|3|첫 번째 수를 뺀 결과 키 조회|48 밀리초|
|4|조회 구조 개선|44 밀리초|
|5|투 포인터 이용|풀이 불가|
|6|고(Go) 구현|8 밀리초|


## 8. 빗물 트래핑
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

 - 8.py (my code)
 - 8-1.py (투 포인터 최대로 이용)
 - 8-2.py (스택 쌓기) **fail**
 

## 9. 세수의 합
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

 - 9.py (my code)
 - 9-1.py (브루트 포스로 계산)
 - 9-2.py (투 포인터로 합 계산)

|풀이|방식|실행 시간|
|----|----|----|
|1|브루트 포스로 계산|타임 아웃|
|2|투 포인터로 합 계산|884밀리초|

## 10. 배열 파이션 1
n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

 - 10.py (my code)
 - 10-1.py (오름차순 풀이)
 - 10-2.py (짝수 번째 값 계산)
 - 10-3.py (파이썬다운 방식)

|풀이|방식|실행 시간|
|----|----|----|
|1|오름차순 풀이|332밀리초|
|2|짝수 번째 값 계산|308밀리초|
|2|파이썬다운 방식|284밀리초|

## 11. 자신을 제외한 배열의 곱
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.

 - 11.py (my code) **fail**
 - 11-1.py (왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈)

## 12. 주식을 사고팔기 가장 좋은 시점
한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

 - 12-1.py (브루트 포스로 계산)
 - 12-2.py (저점과 현재 값과의 차이 계산)
 
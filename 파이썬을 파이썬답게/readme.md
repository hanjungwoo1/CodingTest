# 파이썬을 파이썬 답게
## 프로그래머스 강의


## 파트1. Python 꿀팁

<details>
<summary></summary>

```python
def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(len(i))
    return answer
```

```python
def solution(mylist):
    return list(map(len, mylist))
```

</details>


## 파트2. 정수 다루기

<details>
<summary></summary>

### 몫과 나머지

```python
a = 7
b = 7
print(a//b, a%b)
```

```python
a = 7
b = 5
print(divmod(a, b))
```

```python
print(divmod(7, 4))
# (1, 3)
print(*divmod(7, 4))
# 1, 3
```

### 정수 다루기

```python
num = '3212'
base = 5

answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)
```

```python
num = '3212'
base = 5
answer = int(num, base)
```

</details>


## 파트3. str다루기

<details>
<summary></summary>


### 문자열 정렬하기

```python
### 우측 정렬 예
s = '가나다라'
n = 7

answer = ''
for i in range(n-len(s)): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s

```

```python
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬
```


### 알파벳 출력하기 - string 모듈

```python
answer = 'abcdefghijk (편의상 생략)'
```

```python
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
```

</details>


## 파트4. Iterable다루기

<details>
<summary></summary>

### 원본을 유지한채, 정렬된 리스트 구하기 - sorted

```python
list1 = [3, 2, 5, 1]
list2 = [i for i in list1] # 또는 copy.deepcopy를 사용
list2.sort()
```

```python
list1 = [3, 2, 5, 1]
list2 = sorted(list1)
```


### 2차원 리스트 뒤집기 - zip

```python
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [[], [], []]

for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        new_list[i].append(mylist[j][i])
```

```python
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
```

### i번째 원소와 i+1번째 원소 - zip

```python
def solution(mylist):
    answer = []
    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i] - mylist[i+1]))
    return answer
```

```python
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer
```

### 모든 멤버의 type 변환하기 - amp

```python
list1 = ['1', '100', '33']
list2 = []
for value in list1:
    list2.append(int(value))
```

```python
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
```

</details>

## 파트5. Sequence Types 다루기

<details>
<summary></summary>

### sequence 멤버를 하나로 이어붙이기 - join

```python
my_list = ['1', '100', '33']
answer = ''
for value in my_list:
    answer += value
```

```python
my_list = ['1', '100', '33']
answer = ''.join(my_list)
```

### 삼각형 별찍기 - sequence type의 * 연산

```python
answer = ''
n = 어쩌고
for _ in range(n):
    answer += 'abc'
```

```python
n = 어쩌고
answer = 'abc' * n
```

```python
n = 어쩌고
answer= [123, 456] * n
```

</details>

## 파트6. Itertools / Collections 모듈 

<details>
<summary></summary>

### 곱집합(Cartesian product) 구하기 - product

```python
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))
```

### 2차원 리스트를 1차원 리스트로 만들기 - from_iterable

```python
my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for element in my_list:
    answer += element
```

```python
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))

# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()
```

### 순열과 조합 - combinations, permutations

```python
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 순열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 순열 만들기
```

### 가장 많이 등장하는 알파벳 찾기 - Counter

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100])  # =  raise KeyError
```

```python
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0
```

</details>

## 파트7. 기타 

<details>
<summary></summary>

### for 문과 if문을 한번에 - List comprehension의 if 문

```python
mylist = [3, 2, 6, 7]
answer = []
for number in mylist:
    if number % 2 == 0:
        answer.append(number**2) # 들여쓰기를 두 번 함
```

```python
mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]
```

### flag 대신 for-else 사용하기

```python
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            print('found')
            break
    else:
        print('not found')
```

### 두 변수의 값 바꾸기 - swap

```python
a = 3
b = 'abc'

a, b = b, a # 참 쉽죠?
```

</details>
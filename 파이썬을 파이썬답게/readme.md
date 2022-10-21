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




</details>
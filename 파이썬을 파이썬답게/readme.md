# 파이썬을 파이썬 답게
## 프로그래머스 강의


## 파트1. Python 꿀팁

<summary>

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

</summary>


## 파트2. 정수 다루기

<summary>

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

</summary>
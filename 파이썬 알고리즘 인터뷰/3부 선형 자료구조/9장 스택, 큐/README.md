# 스택, 큐

## 스택
스택 : 다음과 같은 2가지 주요 연산을 지원하는 요소의 컬렉션으로 사용되는 추상 자료형이다.
 - push() : 요소를 컬렉션에 추가한다.
 - pop() : 아직 제거되지 않은 가장 최근에 삽입된 요소를 제거한다.

#### 연결 리스트를 이용한 스택 ADT 구현
```python
class Node:
    def __init__(self, item , next):
        self.item = item
        self.next = next
        
class Stack:
    def __init__(self):
        self.last = None
        
    def push(self, item):
        self.last = Node(item, self.last)
        
    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item
```

## 20. 유효한 괄호
괄호로 된 입력값이 올바른지 판별하라.

 - 20.py (my code)
 - 20-1.py (스택 일치 여부 판별) 

## 21. 중복 문자 제거
중복된 문자를 제거하고 사전식 순서(Lexicographical Order)로 나열하라.

 - 21-1.py // **have to**

## 22. 일일 온도
매일의 화씨 온도(F) 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

 - 22.py (my code)
 - 22-1.py (스택 값 비교)


## 큐
큐 : 스퀀스의 한쪽 끝에는 엔티티를 추가하고, 다른 반대쪽 끝에는 제거할 수 있는 엔티티 컬렉션이다.

## 23. 큐를 이용한 스택 구현
큐를 이용해 다음 연산을 지원하는 스택을 구현하라

 - push(x) : 요소 x를 스택에 삽입한다.
 - pop() : 스택의 첫 번째 요소를 삭제한다.
 - top() : 스택의 첫 번째 요소를 가져온다.
 - empty() : 스택이 비어 있는지 여부를 리턴한다.


 - 23.py (my code)
 - 23-1.py (push() 할 때 큐를 이용해 재정렬)

## 24. 스택을 이용한 큐 구현
스택을 이용해 다음 연산을 지원하는 큐를 지원하라.

 - push(x) : 요소 x를 큐 마지막에 삽입한다.
 - pop() : 큐 처음에 있는 요소를 제거한다.
 - peek() : 큐 처음에 있는 요소를 조회한다.
 - emtpy() : 큐가 비어 있는지 여부를 리턴한다

 - 24.py (my code)
 - 24-1.py (스택 2개 사용) **check**

## 25. 원형 큐 디자인
원형 큐를 디자인하라.

 - 25-1.py (배열을 이용한 풀이)

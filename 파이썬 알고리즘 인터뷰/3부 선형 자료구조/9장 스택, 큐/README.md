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

 - 21-1.py // **continue**

## 22. 일일 온도
매일의 화씨 온도(F) 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

 - 22.py (my code)
 - 22-1.py (스택 값 비교)
 - 
#개발형 코딩 테스트

## 알고리즘 코딩 테스트 vs 개발형 코딩 테스트
알고리즘 코딩 테스트 : 한정된 컴퓨터 자원, 정해진 시간 안에 동작하는 효율적인 프로그램 작성

개발형 코딩 테스트 : 정해진 목적에 따라서 동작하는 완성된 프로그램을 개발하는 것을 요구
 - 모바일 클라이언트 분야 : 안드로이드, iOS
 - 웹 서버 개발 분야 : 스프링, 장고

## 서버와 클라이언트
클라이언트 : 요청(Request)

서버 : 응답(Response)

#### 클라이언트
클라이언트 : 고객이라는 의미, 정보를 요청하는 측

클라이언트가 서보로 데이터를 보내는 것을 **요청(Request)**

#### 서버
서버 : 서비스를 제공해주는 컴퓨터, 정보를 제공

서버는 클라이언트로부터 요청을 받아서, 그에 맞는 **응답(Response)**


#### 파이썬으로 웹 요청하기
HTTP(HypterText Transfer Protocol) : 웹상에서 데이터를 주고받기 위한 프로토콜

|HTTP 메서드|설명|사용 예시|
|---|---|---|
|GET|특정한 데이터의 조회를 요청한다.|특정 페이지 접속, 정보 검색|
|POST|특정한 데이터의 생성을 요청한다.|회원가입, 글쓰기|
|PUT|특정한 데이터의 수정을 요청한다. |회원 정보 수정|
|DELETE|특정한 데이터의 삭제를 요청한다.|회원 정보 삭제|

```python
import requests

target = "http://google.com"
response = requests.get(url=target)
print(response.text)
```

## REST API란 ?

REST(REpresentational State Transfer) : 각 자원(Resource)에 대하여 자원의 상태에 대한 정보를 주고받는 개발 방식

API(Application Programming Interface) : 프로그램이 상호작용하기 위한 인터페이스
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

REST API : REST 아키텍처를 따르는 API를 의미

REST API 호출 : REST 방식을 따르고 있는 서버에 특정한 요청을 보내서 데이터를 가져오는 것

REST를 이용하는 방법 
 - HTTP URI(Uniform Resource Identifier)로 자원을 명시
 - HTTP 메서드(POST, GET, PUT, DELETE)를 통해 해당 자원을 어떻게 처리할지를 명시

REST의 구성 요소
 - 자원(Resource) : URI를 이용하여 표현
 - 행위(Verb) : HTTP 메서드를 이용하여 표현
 - 표현(Representations)

#### JSON

JSON(JavaScript Object Notation) : 데이터를 주고받는 데 사용하는 경량의 데이터 형식, 키-값 쌍으로 이루어진 데이터 객체

```json
{
  "id" : "gildong", 
  "password" : "192837", 
  "age" : 30,
  "hobby" : ["football", "programming"]
}
```

```python
import json

user = {
  "id" : "gildong", 
  "password" : "192837", 
  "age" : 30,
  "hobby" : ["football", "programming"]
}

# 인코딩 : 파이썬 변수를 JSON 객체로 변환(띄어쓰기 네 칸 들여쓰기 적용)
json_data = json.dumps(user, indent = 4)

# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent = 4)

# 디코딩 : JSON 객체를 파이썬 변수로 변환
data = json.loads(json_data)
```

#### 파이썬으로 REST API 호출 실습해보기
 - JSON 목킹 사이트를 이용
 - 목킹(Mocking) : 어떠한 기능이 있는 것처럼 흉내내어 구현하는 것을 의미

#### JSON Placeholder : https://jsonplaceholder.typicode.com
이 사이트는 일종의 서버 API중에서 회원(User), 게시물(Post)등에 대한 가짜 API 기능을 제공해준다

#### API 호출 실습(GET 메서드) 1
 - API 호출 경로 : https://jsonplaceholder.typicode.com/users/1
 - HTTP 메서드 : GET

#### API 호출 실습(GET 메서드) 2
 - API 호출 경로 : https://jsonplaceholder.typicode.com/users
 - HTTP 메서드 : GET

#### 회원 정보 처리 실습
파싱(Parsing) : 특정한 형식으로 저장된 데이터에 접근하여 원하는 정보만 찾아서 가공하는 작업

```python
import requests

# REST API 경로에 접속하여 응답(Response) 데이터 받아오기
target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

# 응답(Response) 데이터가 JSON 형식이므로 바로 파이썬 객체로 변환
data = response.json()

# 모든 사용자가(user) 정보를 확인하며 이름 정보만 삽입
name_list = []
for user in data:
    name_list.append(user['name'])
    
print(name_list)
```
"""
예제 입력 1
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

예제 출력 1
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
"""

n = int(input())
data = []

for _ in range(n):
    data.append(list(input().split()))

data.sort(key=lambda item: (-int(item[1]), int(item[2]), -int(item[3]), item[0]))

for x in data:
    print(x[0])
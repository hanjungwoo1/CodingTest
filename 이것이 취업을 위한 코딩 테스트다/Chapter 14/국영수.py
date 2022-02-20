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
students = []

for _ in range(n):
    students.append(input().split())

print(students)


students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for x in students:
    print(x[0])



# N을 입력받기
N = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(N):
    input_data = input().split()
    array.append([input_data[0], input_data[1]])

print(array)
# 키(key)를 이용하여, 점수를 기준으로 출력
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end = ' ')
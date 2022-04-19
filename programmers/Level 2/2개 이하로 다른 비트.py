def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'

        if number % 2 == 1:
            bin_number[idx + 1] = '0'

        answer.append(int(''.join(bin_number), 2))

    return answer


# 1) 짝수의 경우
# 만약, 4라면 이진수로 100 입니다. 4보다 크면서 2개 이하로 다른 수를 찾으면 101 입니다.
# 즉, 가장 뒤에 있는 0을 1로 바꿔주면 됩니다.
#
# 2) 홀수의 경우
# 만약, 7이라면 이진수로 0111 (바꿀때 편의를 위해 앞에 0을 붙입니다)
# 먼저 짝수의 경우처럼 가장 뒤에 있는 0의 인덱스(idx)를 찾아 1로 바꿉니다. 그럼 1111 이 됩니다.
# bin_number[idx] = '1'
# 그런 다음 idx+1 의 인덱스 값을 0으로 바꿉니다. 그럼 1011이 되고 답이 됩니다.
# bin_number[idx+1] = '0'







### 내 풀이 시간초과
# def solution(numbers):
#     answer = []
#
#     for data in numbers:
#         # print("data : ", data)
#         next_num = data + 1
#
#         while (True):
#             data2 = data
#             temp = next_num
#             count = 0
#
#             # 2진수 만들기
#             data2 = bin(data2)[2:]
#             temp = bin(temp)[2:]
#
#             if len(data2) != len(temp):
#                 count += 1
#                 temp = temp[1:]
#
#             for x, y in zip(data2, temp):
#                 if count > 2:
#                     break
#
#                 if x != y:
#                     count += 1
#
#             # print("count : ", count)
#             if int(count) < 3:
#                 answer.append(next_num)
#                 break
#
#             next_num = next_num + 1
#
#     return answer


numbers = [2,7]

print(solution(numbers))
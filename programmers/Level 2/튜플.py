def solution(s):
    answer = []
    s = s[2:-2]
    s = sorted(s.split("},{"), key = lambda x: len(x))

    print(s)
    for i in s:
        i_ = i.split(',')
        for j in i_:
            if int(j) not in answer:
                print(int(j))
                answer.append(int(j))
    return answer

### 정렬하는 이유가 문제에 기제되어 있지 않음

# def solution(s):
#     data = ''
#     answer = []
#     for x in s:
#         if x == '{':
#             continue
#
#         if x == ',' or x == '}':
#             if len(data) > 0:
#                 answer.append(data)
#                 data = ''
#             continue
#
#         if x.isdigit():
#             data += str(x)
#
#     answer = list(set(answer))
#     print(answer)
#
#     return answer
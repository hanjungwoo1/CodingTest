# def solution(files):
#     file_names = []
#     answer = []
#
#     for file in files:
#
#         for i, char in enumerate(file):
#             if char.isdigit():
#                 head, num_tail = file[:i], file[i:]
#                 break
#
#         for i, char in enumerate(num_tail):
#             if not char.isdigit():
#                 num, tail = num_tail[:i], num_tail[i:]
#                 break
#         file_names.append([head.lower(), int(num), tail, file])
#
#     file_names = sorted(file_names, key=lambda file: [file[0], file[1]])
#
#     for file in file_names:
#         answer.append(file[3])
#
#     return answer


def solution(files):
    answer = []

    for f in files:
        head, number, tail = '', '', ''

        number_check = False
        for i in range(len(f)):  # 문자열 자르기
            if f[i].isdigit():  # 처음 나오는 숫자부터는 NUMBER로
                number += f[i]
                number_check = True
            elif not number_check:  # NUMBER가 나오기 전까지는 HEAD
                head += f[i]
            else:  # NUMBER가 이미 나왔고, 숫자가 아닌 문자가 나오면 TAIL
                tail = f[i:]
                break
        answer.append((head, number, tail))  # HEAD, NUMBER, TAIL 하나의 튜플로 저장

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    print(answer)
    return [''.join(t) for t in answer]
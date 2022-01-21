def solution(id_list, report, k):
    user = {}   # 신고 횟수 딕셔너리
    name = {}   # 신고 결과 딕셔너리

    # 딕셔너리 초기화, for count
    for id in id_list:
        user[id] = 0
        name[id] = 0

    # report map으로 중복제거
    set_report = set(report)
    report = list(set_report)

    # 신고 당한 횟수 계산
    for data in report:
        _, second = data.split(' ')
        user[second] += 1

    # 각각 자신이 신고한 사람이 k를 넘었는지 판별, 신고 결과 만들기
    for data in report:
        first, second = data.split(' ')
        if user[second] >= k:
            name[first] += 1

    # 정답
    answer = []

    # for dictionary for loop
    for k, v in name.items():
        answer.append(v)

    return answer


# best Answer
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
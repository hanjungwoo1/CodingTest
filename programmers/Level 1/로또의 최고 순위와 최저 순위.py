# best Answer 참고 코드
def solution(lottos, win_nums):
    answer = [0, 0] # 결과 초기화
    rank = [6, 6, 5, 4, 3, 2, 1] #

    cnt = 0
    cntz = lottos.count(0) # 0의 갯수 count
    for i in lottos:
        if i in win_nums:
            cnt += 1       # lotts에 win_nus 있는지 파악

    answer[0], answer[1] = rank[cnt + cntz], rank[cnt]  # list의 순서로 결과생성

    return answer
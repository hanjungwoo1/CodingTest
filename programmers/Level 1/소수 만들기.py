# Combinations 기억하기!
from itertools import combinations
def solution(nums):
    answer = 0

    A = list(combinations(nums, 3))
    for x,y,z in A:
        total = x+y+z
        flag = True
        for i in range(2, total):
            if total % i==0:
                flag = False
        if flag:
            answer += 1

    return answer


# best answer
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:               # else 위치가 특이함
            answer += 1
    return answer
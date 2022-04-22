def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    answer = 0
    for x, y in zip(A, B):
        answer += x * y

    return answer
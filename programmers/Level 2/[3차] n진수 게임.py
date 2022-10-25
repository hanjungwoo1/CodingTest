def solution(n, t, m, p):

    #재귀함수 이용 - 10진수를 n진수로
    def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]

    answer = ''
    candidate = []

  # 모든 턴의 답
    for i in range(t*m):
        conv = convert(i, n)
        for c in conv:
            candidate.append(c)

    # 튜브의 답만 추출
    for i in range(p-1, t*m, m):
        answer += candidate[i]

    return answer
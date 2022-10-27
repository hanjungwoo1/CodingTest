def solution(n):
    answer = []
    array = [[0] * n for _ in range(n)]
    x, y = -1, 0  # 처음엔 무조건 아래로 향하게 해야 하므로 x=-1로 초기화
    num = 1

    for i in range(n):  # 방향 check
        for _ in range(i, n):
            if i % 3 == 0:  # 아래
                x += 1
            elif i % 3 == 1:  # 오른쪽
                y += 1
            elif i % 3 == 2:  # 위쪽 대각선
                x -= 1
                y -= 1
            array[x][y] = num
            num += 1
    for i in array:
        for j in i:
            if j:
                answer.append(j)
    return answer
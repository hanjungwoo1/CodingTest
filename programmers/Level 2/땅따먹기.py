def solution(land):
    answer = 0
    row = len(land)
    column = len(land[0])

    for i in range(1, row):
        for j in range(column):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    return max(land[len(land) - 1])
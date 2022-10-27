def possible(x, y, n, col):
    for i in range(x):
        # 같은 열에 위치하는지 or 같은 대각선에 위치하는지 확인
        if y == col[i] or abs(y - col[i]) == x - i:
            return False
    return True


def queen(x, n, col):
    # row가 끝까지 갔으면 성공!
    if x == n:
        return 1

    count = 0

    for y in range(n):
        # 다음 퀸을 놓을 수 있는 경우만 진행
        if possible(x, y, n, col):
            col[x] = y  # x번째 row의 col index 저장 ex) col[0] = 2 0번째 행의 2번째 col에 놓여져 있다.
            count += queen(x + 1, n, col)  # row index 증가 후 호출

    return count


def solution(n):
    col = [0] * n

    # 0은 세로축의 시작점
    # n은 맵의 크기
    # col은 row 의 index를 담기 위한 리스트
    answer = queen(0, n, col)

    return answer
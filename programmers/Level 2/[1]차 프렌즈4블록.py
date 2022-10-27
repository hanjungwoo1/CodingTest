def check_board(board: list):
    m = len(board)
    n = len(board[0])

    map_board = [[0] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            temp = board[i][j]

            if board[i - 1][j - 1] == temp and board[i][j - 1] == temp and board[i - 1][j] == temp and temp != "X":
                map_board[i][j] = 1
                map_board[i - 1][j] = 1
                map_board[i][j - 1] = 1
                map_board[i - 1][j - 1] = 1

    count = 0
    for row_board in map_board:
        count += sum(row_board)

    return map_board, count


def compress_board(board: list, map_board: list):
    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            if map_board[i][j] == 1:

                if i == 0:
                    board[i][j] = "X"
                else:
                    x = i
                    while x > 0:
                        board[x][j] = board[x - 1][j]
                        board[x - 1][j] = "X"
                        x -= 1

    return board


def solution(m, n, board):
    answer = 0
    new_board = [list(data) for data in board]

    while True:
        map_board, count = check_board(new_board)
        if count == 0:
            break

        answer += count
        new_board = compress_board(new_board, map_board)

    return answer
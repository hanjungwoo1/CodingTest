import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]


def quadtree(x, y, N):
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                print('(', end='')
                quadtree(x, y, N//2)
                quadtree(x, y+N//2, N//2)
                quadtree(x+N//2, y, N//2)
                quadtree(x+N//2, y+N//2, N//2)
                print(')', end='')
                return
    if color == 0:
        print('0', end='')
    else:
        print('1', end='')

quadtree(0,0,N)

"""
입력 예시 1
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

출력 예시 1
9

입력 예시 2
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

출력 예시 2
21

입력 예시 3
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L

출력 예시 3
13
"""

def check_grid(grid, new_pos):
    length = len(grid)


    # out of range
    if new_pos[0] >= length or new_pos[1] >= length or new_pos[0] < 0 or new_pos[1] < 0:
        return True

    # crush on snake
    if grid[new_pos[0]][new_pos[1]] > 0:
        return True

    return False

def down_grid(grid):

    length = len(grid)

    for x in range(length):
        for y in range(length):
            grid[x][y] -= 1

            # 일반적인 길의 위치
            if grid[x][y] == -1:
                grid[x][y] = 0

            # 사과의 위치, 다시 -1
            if grid[x][y] == -2:
                grid[x][y] = -1

            # 나머지는, 전체적인 뱀의 길이를 map을 다시 만들어 줌
    return grid

def crawl(grid, head_pos, snake_length, snake_dir):
    new_pos = head_pos
    if snake_dir == 1:
        new_pos[1] += 1       # 오른쪽 1칸
    elif snake_dir == 2:
        new_pos[0] += 1       # 아래로 1칸
    elif snake_dir == 3:
        new_pos[1] -= 1       # 왼쪽 1칸
    elif snake_dir == 0:
        new_pos[0] -= 1       # 위쪽 1칸
    else:
        print()
        # print(snake_dir)
        # print("direction error")


    # check, end of map (or) snake crash
    check = check_grid(grid, new_pos)

    if check:
        return grid, head_pos, snake_length, snake_dir, True

    # update new head
    snake_length += 1

    if grid[new_pos[0]][new_pos[1]] == -1:
        # head - updated to dir, tail - stop
        grid[new_pos[0]][new_pos[1]] = snake_length
        # print("eat")
    else:
        # 사과를 안먹었을 때, 현재 머리를 한칸 이동 후 tail이 2로 위치 이동
        # head- updated to dir, tail - updated toward 1
        grid[new_pos[0]][new_pos[1]] = snake_length
        snake_length -= 1
        down_grid(grid)
        # 전체 맵 -1

    return grid, head_pos, snake_length, snake_dir, False


from collections import deque

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수

grid = [[0]*n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    grid[x-1][y-1] = -1     # 사과의 위치 -1로 표시

dir = int(input())
direction = deque()

for _ in range(dir):
    x, y = input().split()
    direction.append([x, y])

grid[0][0] = 1
head_pos = [0,0]
snake_length = 1
snake_dir = 1           # 1 : east, 2 : south, 3 : west, 0 : north

second = 0
# print("second: ", second)
# print("grid : ", grid)
# print("direction :", snake_dir)
# print("head : ", head_pos)
# print()

while(direction):
    second = second + 1

    x, y = direction.popleft()

    grid, head_pos, snake_length, snake_dir, flag = crawl(grid, head_pos, snake_length, snake_dir)
    if flag == True:
        # print("End : ", second)
        exit()

    # check direction
    if second == int(x):

        if y == 'D':
            snake_dir += 1
        else:
            snake_dir -= 1

        # 4방향
        snake_dir = snake_dir % 4
    else:
        direction.appendleft([x, y])


    # print("second: ", second)
    # print("grid : ", grid)
    # print("direction :", snake_dir)
    # print("head : ", head_pos)
    #
    # print()

while(second < 100):
    second = second + 1
    # print("second: ", second)
    grid, head_pos, snake_length, snake_dir, flag = crawl(grid, head_pos, snake_length, snake_dir)
    if flag == True:
        print(second)
        exit()

    # print("grid : ", grid)
    # print("direction :", snake_dir)
    # print("head : ", head_pos)
    # print()


### add 나머지 시간


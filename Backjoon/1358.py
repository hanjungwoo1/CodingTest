import sys

input = sys.stdin.readline


W, H, X, Y, P = map(int, input().split())




# 사각형
def in_square(W, H, X, Y, target_x, target_y) -> bool:
    if target_x >= X and target_x <= X+W and target_y >= Y and target_y <= Y+H:
        #print("in_square")
        return True
    return False

# 왼쪽 써클
def left_circle(H, X, Y, target_x, target_y) -> bool:
    center_x = X
    center_y = Y + H//2

    if ((center_x - target_x)**2 + (center_y - target_y)**2)**0.5 <= (H//2):
        #print("left")
        return True
    return False

# 오른쪽 써클

def right_circle(W, H, X, Y, target_x, target_y) -> bool:
    center_x = X + W
    center_y = Y + H//2

    if ((center_x - target_x)**2 + (center_y - target_y)**2)**0.5 <= H//2:
        #print("right")
        return True
    return False



def check(W, H, X, Y, target_x, target_y):
    if in_square(W, H, X, Y, target_x, target_y) or left_circle(H, X, Y, target_x, target_y) or right_circle(W, H, X, Y, target_x, target_y):
        return True
    return False

count = 0
for _ in range(P):
    x, y = map(int, input().split())
    #print(x, y)
    if check(W, H, X, Y, x, y):
        count += 1
print(count)
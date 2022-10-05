import sys
input = sys.stdin.readline

axis_x = []
axis_y = []

for _ in range(3):
    x, y = map(int, input().split())

    if x not in axis_x:
        axis_x.append(x)
    else:
        axis_x.remove(x)

    if y not in axis_y:
        axis_y.append(y)
    else:
        axis_y.remove(y)

print(axis_x[0], axis_y[0])



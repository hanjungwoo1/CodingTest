from itertools import combinations

def intersection_point(line1, line2):
    a, b, e = line1
    c, d, f = line2
    if a * d == b * c:
        return None
    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)
    if x == int(x) and y == int(y):
        return (int(x), int(y))

def solution(line):
    points = set()

    for left, right in combinations(line, 2):
        point = intersection_point(left, right)

        if point:
            points.add(point)

    # 교점의 x좌표들
    xs = [p[0] for p in points]
    x_min = min(xs)
    x_max = max(xs)

    # 교점의 y좌표들
    ys = [p[1] for p in points]
    y_min = min(ys)
    y_max = max(ys)

    # 모두 . 으로 초기화
    answer = ['.' * (x_max - x_min + 1)] * (y_max - y_min + 1)
    # 각 좌표마다 * 그리기
    for point in points:
        x, y = point
        answer[y_max - y] = answer[y_max - y][:x - x_min] + '*' + answer[y_max - y][x - x_min + 1:]

    return [''.join(ans) for ans in answer]
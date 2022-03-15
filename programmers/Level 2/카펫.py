def solution(brown, yellow):
    answer = []
    total = brown + yellow

    for x in range(1, yellow + 1):
        if yellow % x == 0:
            y = yellow // x
            if x * y == yellow:
                data = (x + 2) * (y + 2) - brown
                if yellow == data:
                    answer = [x + 2, y + 2]
                    break
    answer.sort(reverse=True)
    return answer
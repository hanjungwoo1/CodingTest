def solution(n, s):
    if n > s:
        return [-1]

    num = s // n

    data = [num] * n

    remain = s - sum(data)
    index = 0
    while True:
        if remain == 0:
            break

        data[index] += 1
        remain -= 1
        index += 1
        index %= n

    return sorted(data)
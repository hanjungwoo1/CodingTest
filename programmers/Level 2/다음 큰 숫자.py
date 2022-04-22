def solution(n):
    answer = 0

    start = n
    cnt = bin(n).count('1')

    flag = True
    while (flag):

        start += 1
        if cnt == bin(start).count('1'):
            answer = start
            break

    return answer
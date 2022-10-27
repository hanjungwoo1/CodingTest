from collections import deque


def divide(string: str):
    left = 0
    right = 0

    queue = deque(string)
    temp_string = ''
    while True:

        temp = queue.popleft()
        if temp == "(":
            temp_string += "("
            left += 1
        else:
            temp_string += ")"
            right += 1

        if left == right:
            break

    return temp_string, ''.join(queue)


def check(string: str):
    temp = ''

    for data in string:
        if data == "(":
            temp += "("
        else:
            temp = temp[:-1]

    if temp == "":
        return True
    return False


def solution(p):
    answer = ''

    if len(p) == 0:
        return ''

    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"

        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

    return answer
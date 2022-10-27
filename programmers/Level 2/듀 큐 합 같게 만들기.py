# from collections import deque
#
#
# def solution(queue1, queue2):
#     q1 = deque(queue1)
#     q2 = deque(queue2)
#     total = len(q1) + len(q2)
#
#     answer = 0
#
#     while sum(q1) != sum(q2):
#         if answer == total:
#             answer = -1
#             break
#
#         if sum(q1) > sum(q2):
#             q2.append(q1.popleft())
#             answer += 1
#         elif sum(q1) < sum(q2):
#             q1.append(q2.popleft())
#             answer += 1
#
#     return answer

from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1)) * 4
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    total = tot1 + tot2

    if total % 2 != 0:
        return -1

    while True:
        if tot1 > tot2:
            target = queue1.popleft()
            queue2.append(target)
            tot1 -= target
            tot2 += target
            answer += 1
        elif tot1 < tot2:
            target = queue2.popleft()
            queue1.append(target)
            tot1 += target
            tot2 -= target
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break
    return answer
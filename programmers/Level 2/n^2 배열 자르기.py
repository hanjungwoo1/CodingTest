# def solution(n, left, right):

#     graph = [[0] * n for _ in range(n)]
#     answer = []
#     count = 0

#     for i in range(n):
#         for j in range(n):
#             count += 1

#             if i > j:
#                 graph[i][j] = i+1
#             else:
#                 graph[i][j] = j+1

#             if count > left and count <= right+1:
#                 answer.append(graph[i][j])

#     return answer


def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer
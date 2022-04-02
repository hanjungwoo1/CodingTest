from itertools import combinations  # 조합 함수

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []

# 조합으로 가능한 팀 생성해주기
for team in list(combinations(members, N // 2)):
    possible_team.append(team)

min_stat_gap = 10000  # 갭이 가장 작은 값을 찾기 위하여
for i in range(len(possible_team) // 2):
    # A 팀
    team = possible_team[i]
    stat_A = 0  # A팀 능력치
    for j in range(N // 2):
        member = team[j]  # 멤버
        for k in team:
            stat_A += S[member][k]  # 멤버와 함께할 경우의 능력치들

    # A를 제외한 나머지 팀
    team = possible_team[-i - 1]
    stat_B = 0
    for j in range(N // 2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]

    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))

print(min_stat_gap)


########################################################################################

# import sys
#
# input = sys.stdin.readline
#
# def dfs(idx, cnt):
#     global ans
#     if cnt == n // 2:
#         start, link = 0, 0
#         for i in range(n):
#             for j in range(n):
#                 if select[i] and select[j]:
#                     start += a[i][j]
#                 elif not select[i] and not select[j]:
#                     link += a[i][j]
#         ans = min(ans, abs(start - link))
#
#     for i in range(idx, n):
#         if select[i]:
#             continue
#         select[i] = 1
#         dfs(i + 1, cnt + 1)
#         select[i] = 0
#
#
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
#
# select = [0 for _ in range(n)]
# ans = sys.maxsize
# dfs(0, 0)
# print(ans)

# https://chldkato.tistory.com/155
"""
LCS

예제 입력 1
ACAYKP
CAPCAK

예제 출력 1
4
"""


import sys

string_a = ' ' + sys.stdin.readline().rstrip()
string_b = ' ' + sys.stdin.readline().rstrip()
dp = [[0] * len(string_b) for _ in range(len(string_a))]

for i in range(1, len(string_a)):
    for j in range(1, len(string_b)):
        if string_a[i] == string_b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])